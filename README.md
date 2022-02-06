# Portable Real-Time Body Tracking Using iPad LiDAR and ARKit

<p>Table of Contents</p>

- [1. What is this project?](#1-what-is-this-project)
- [2. Installation](#2-installation)
- [3. Usage](#3-usage)
- [4. Example Graphs](#4-example-graphs)
<hr>

# 1. What is this project

- Foundation for the usage of ARKit for Body Tracking
- Contains a Swift Playgrounds program which utilizes iPad's LiDAR and ARKit for body tracking. It shows a live feed on the iPad along with an AR Body Skeleton overlaying the body in the feed.
- Contains a python program which recieves the joint names and joint coordinates for all 92 pre-defined joints via TCP. The data is processed and stored as a CSV file and a few graphs are plotted displaying the joints movement.

<hr>

# 2. Installation
Ensure that you have a iPad Pro and a Computer with Python already installed

<hr>

## 2.1 Ensure the required python modules are installed:
- socket 
- pandas 
- matplotlib 
- time
  
## 2.2 Clone the repository
- Setup the swift program in swift playground on the iPad
- Setup the python program on the computer
  
## 2.3 Program configuration
- In Line 58 in the Python program, enter the IP address of the computer within the " " along with a port number ranging from 1 - 65,535
  - ``` s.bind(('XXX.XXX.XX.XX', XXXXX)) ```
- In Line 43 in the Swift program, enter the IP address of the computer within the " " along with the same port number entered previously in the python program
  - ``` let m = Main(hostName: "XXX.XXX.XX.XX", port: XXXXX ) ```  

<hr>

# 3. Usage
  1. Run Python Program
  2. Run Swift Playgrounds Program
  3. Stop Swift Playgrounds Program after body tracking
- After body tracking has stopped, the data will be processed and saved to a CSV file with timestamp and graphs will be plotted

<hr>

# 4. Example Graphs
<p align = "center">
<img width="800" src="https://github.com/sag-stack/BodyTracking/blob/main/Armmovement1.png" alt="Hand Movement">
<br>
Hand Movement
<br><br>
<img width = "800" src="https://github.com/sag-stack/BodyTracking/blob/main/shoulderuparmmovement.png" alt="Elbow and Hand Movement">
<br>
Elbow and Hand Movement
<br><br>
<img width = "800" src="https://github.com/sag-stack/BodyTracking/blob/main/legmovement.png" alt="Leg Movement">
<br>
Leg Movement
</p>
