//Import Frameworks
import PlaygroundSupport
import RealityKit
import SwiftUI
import ARKit
import Foundation
import Network

//
class Main {
    init(hostName: String, port: Int) {
        let host = NWEndpoint.Host(hostName)
        let port = NWEndpoint.Port("\(port)")!
        self.connection = NWConnection(host: host, port: port, using: .tcp)
    }
    
    let connection: NWConnection
    //Start connection to server
    func start() {
        NSLog("will start")
        self.connection.start(queue: .main)
    }
    //Stop connection to server
    func stop() {
        self.connection.cancel()
        NSLog("did stop")
    }
    //Send collected data to server as a string
    func send(line: String) {
        var timestamp = NSDate().timeIntervalSince1970.description
        let data = Data(("|"+timestamp+";"+line).utf8)
        self.connection.send(content: data, completion: NWConnection.SendCompletion.contentProcessed { error in
            if let error = error {
                NSLog("did send, error: %@", "\(error)")
                self.stop()
            } else {
                NSLog("did send, data: %@", data as NSData)
            }
        })
    }
}

let m = Main(hostName: "IP Address", port: 'PORT NUMBER')
m.start()

//Creation of BodySkeleton for visualization and updating joint pose
class BodySkeleton: Entity{
    var joints: [String: Entity] = [:] // jointNames mapped to jointEntities
    
    required init(for bodyAnchor: ARBodyAnchor) {
        super.init()
        
        //Entity creation for each joint
        for jointName in ARSkeletonDefinition.defaultBody3D.jointNames{
            //Default values for joint appearance
            var jointRadius: Float = 0.03
            var jointColor: UIColor = .green
            
            //Set color and size based on specific jointName
            switch jointName {
            case "neck_1_joint", "neck_2_joint", "neck_3_joint", "neck_4_joint", "head_joint", "left_shoulder_1_joint", "right_shoulder_1_joint":
                jointRadius *= 0.5
            case "jaw_joint", "chin_joint", "left_eye_joint", "left_eyeLowerLid_joint", "left_eyeUpperLid_joint", "left_eyeball_joint", "nose_joint", "right_eye_joint", "right_eyeLowerLid_joint", "right_eyeUpperLid_joint", "right_eyeball_joint":
                jointRadius *= 0.2
                jointColor = .yellow
            case _ where jointName.hasPrefix("spine_"):
                jointRadius *= 0.75
            case "left_hand_joint", "right_hand_joint":
                jointRadius *= 1
                jointColor = .green
            case _ where jointName.hasPrefix("left_hand") || jointName.hasPrefix("right_hand"):
                jointRadius *= 0.25
                jointColor = .yellow
            case _ where jointName.hasPrefix("left_toes") || jointName.hasPrefix("right_toes"):
                jointRadius *= 0.5
                jointColor = .yellow
            default:
                jointRadius = 0.05
                jointColor = .green
            }
            // To add to joint dictioanry, and bodySkeleton
            let jointEntity = makeJoint(radius: jointRadius, color: jointColor)
            joints[jointName] = jointEntity
            self.addChild(jointEntity)
        }
        self.update(with: bodyAnchor)
    }

    required init() {
        fatalError("init() has not been implemented")
    }
    
    //Helper method to create a sphere-shaped entity with specified radius and color for a joint
    func makeJoint(radius: Float, color: UIColor) -> Entity {
        let mesh = MeshResource.generateSphere(radius: radius)
        let material = SimpleMaterial(color: color, roughness: 0.8, isMetallic: false)
        let modelEntity = ModelEntity(mesh: mesh, materials: [material])
        return modelEntity
    }
    
    
    //Update the position and orientation of each jointEntity
    func update(with bodyAnchor: ARBodyAnchor) -> String {
        let rootPosition = simd_make_float3(bodyAnchor.transform.columns.3)
        var positions = ""
        for jointName in ARSkeletonDefinition.defaultBody3D.jointNames{
            if let jointEntity = joints[jointName], let jointTransform = bodyAnchor.skeleton.modelTransform(for: ARSkeleton.JointName(rawValue: jointName)){
                let jointOffset = simd_make_float3(jointTransform.columns.3)
                jointEntity.position = rootPosition + jointOffset
                jointEntity.orientation = Transform(matrix: jointTransform).rotation
                positions += jointName + ":" + jointOffset[0].description + "," + jointOffset[1].description + "," + jointOffset[2].description + ";"
            }
        }
        return positions
    }
}

//Global Variables for BodySkeleton
var bodySkeleton: BodySkeleton?
var bodySkeletonAnchor = AnchorEntity()
var pos_array = [String]()


//Creating ARViewContainer
struct ARViewContainer: UIViewRepresentable {
    typealias UIViewType = ARView
    
    func makeUIView(context: UIViewRepresentableContext<ARViewContainer>) -> ARView {
        let arView = ARView(frame: .zero , cameraMode: .ar, automaticallyConfigureSession: true)
        arView.setupForBodyTracking()
        //Add bodySkeletonAnchor to the scene
        arView.scene.addAnchor(bodySkeletonAnchor)
        return arView
    }
    
    func updateUIView(_ uiView: ARView, context: UIViewRepresentableContext<ARViewContainer>) {
    }
}

//Implement body tracking function
extension ARView: ARSessionDelegate {
    //Configuration of ARView for body tracking
    func setupForBodyTracking(){
        let config = ARBodyTrackingConfiguration()
        self.session.run(config)
        self.session.delegate = self
    }
    
    //didUpdate anchors delegate method
    public func session(_ session: ARSession, didUpdate anchors: [ARAnchor]){
        for anchor in anchors {
            if let bodyAnchor = anchor as? ARBodyAnchor {
                // Create or update BodySkeleton
                if let skeleton = bodySkeleton {
                    // BodySkeleton already exists, update position of all joints
                    var pos_t = skeleton.update(with: bodyAnchor) 
                    m.send(line: pos_t)
                    pos_array.append(pos_t)
                } else {
                    //Seeing Body for the first time 
                    let skeleton = BodySkeleton(for: bodyAnchor)
                    bodySkeleton = skeleton
                    bodySkeletonAnchor.addChild(skeleton)
                }
            }
        }
    }
}


// 2b.Set ContentView as LiveView
PlaygroundPage.current.setLiveView(ARViewContainer())
