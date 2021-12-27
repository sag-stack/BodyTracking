#Import modules
import socket
import pandas as pd
import matplotlib.pyplot as plt
import time
#Socket configuration
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Initialize variables
total_data  = joint_name = total_data = []
temp_data = string_data = ""
alt_heading = ['Timestamp','X_1', 'Y_1', 'Z_1', 'X_2', 'Y_2', 'Z_2', 'X_3', 'Y_3', 'Z_3', 'X_4', 'Y_4', 'Z_4', 'X_5', 'Y_5', 'Z_5', 'X_6', 'Y_6', 'Z_6', 'X_7', 'Y_7', 'Z_7', 'X_8', 'Y_8', 'Z_8', 'X_9', 'Y_9', 'Z_9', 'X_10', 'Y_10', 'Z_10', 'X_11', 'Y_11', 'Z_11', 'X_12', 'Y_12', 'Z_12', 'X_13', 'Y_13', 'Z_13', 'X_14', 'Y_14', 'Z_14', 'X_15', 'Y_15', 'Z_15', 'X_16', 'Y_16', 'Z_16', 'X_17', 'Y_17', 'Z_17', 'X_18', 'Y_18', 'Z_18', 'X_19', 'Y_19', 'Z_19', 'X_20', 'Y_20', 'Z_20', 'X_21', 'Y_21', 'Z_21', 'X_22', 'Y_22', 'Z_22', 'X_23', 'Y_23', 'Z_23', 'X_24', 'Y_24', 'Z_24', 'X_25', 'Y_25', 'Z_25', 'X_26', 'Y_26', 'Z_26', 'X_27', 'Y_27', 'Z_27', 'X_28', 'Y_28', 'Z_28', 'X_29', 'Y_29', 'Z_29', 'X_30', 'Y_30', 'Z_30', 'X_31', 'Y_31', 'Z_31', 'X_32', 'Y_32', 'Z_32', 'X_33', 'Y_33', 'Z_33', 'X_34', 'Y_34', 'Z_34', 'X_35', 'Y_35', 'Z_35', 'X_36', 'Y_36', 'Z_36', 'X_37', 'Y_37', 'Z_37', 'X_38', 'Y_38', 'Z_38', 'X_39', 'Y_39', 'Z_39', 'X_40', 'Y_40', 'Z_40', 'X_41', 'Y_41', 'Z_41', 'X_42', 'Y_42', 'Z_42', 'X_43', 'Y_43', 'Z_43', 'X_44', 'Y_44', 'Z_44', 'X_45', 'Y_45', 'Z_45', 'X_46', 'Y_46', 'Z_46', 'X_47', 'Y_47', 'Z_47', 'X_48', 'Y_48', 'Z_48', 'X_49', 'Y_49', 'Z_49', 'X_50', 'Y_50', 'Z_50', 'X_51', 'Y_51', 'Z_51', 'X_52', 'Y_52', 'Z_52', 'X_53', 'Y_53', 'Z_53', 'X_54', 'Y_54', 'Z_54', 'X_55', 'Y_55', 'Z_55', 'X_56', 'Y_56', 'Z_56', 'X_57', 'Y_57', 'Z_57', 'X_58', 'Y_58', 'Z_58', 'X_59', 'Y_59', 'Z_59', 'X_60', 'Y_60', 'Z_60', 'X_61', 'Y_61', 'Z_61', 'X_62', 'Y_62', 'Z_62', 'X_63', 'Y_63', 'Z_63', 'X_64', 'Y_64', 'Z_64', 'X_65', 'Y_65', 'Z_65', 'X_66', 'Y_66', 'Z_66', 'X_67', 'Y_67', 'Z_67', 'X_68', 'Y_68', 'Z_68', 'X_69', 'Y_69', 'Z_69', 'X_70', 'Y_70', 'Z_70', 'X_71', 'Y_71', 'Z_71', 'X_72', 'Y_72', 'Z_72', 'X_73', 'Y_73', 'Z_73', 'X_74', 'Y_74', 'Z_74', 'X_75', 'Y_75', 'Z_75', 'X_76', 'Y_76', 'Z_76', 'X_77', 'Y_77', 'Z_77', 'X_78', 'Y_78', 'Z_78', 'X_79', 'Y_79', 'Z_79', 'X_80', 'Y_80', 'Z_80', 'X_81', 'Y_81', 'Z_81', 'X_82', 'Y_82', 'Z_82', 'X_83', 'Y_83', 'Z_83', 'X_84', 'Y_84', 'Z_84', 'X_85', 'Y_85', 'Z_85', 'X_86', 'Y_86', 'Z_86', 'X_87', 'Y_87', 'Z_87', 'X_88', 'Y_88', 'Z_88', 'X_89', 'Y_89', 'Z_89', 'X_90', 'Y_90', 'Z_90', 'X_91', 'Y_91', 'Z_91']
jointcoord_heading = [['X_1','Y_1','Z_1'],['X_2', 'Y_2', 'Z_2'],['X_3', 'Y_3', 'Z_3'],['X_4', 'Y_4', 'Z_4'],['X_5', 'Y_5', 'Z_5'],['X_6', 'Y_6', 'Z_6'],['X_7', 'Y_7', 'Z_7'],['X_8', 'Y_8', 'Z_8'],['X_9', 'Y_9', 'Z_9'],['X_10', 'Y_10', 'Z_10'],['X_11', 'Y_11', 'Z_11'],['X_12', 'Y_12', 'Z_12'],['X_13', 'Y_13', 'Z_13'],['X_14', 'Y_14', 'Z_14'],['X_15', 'Y_15', 'Z_15'],['X_16', 'Y_16', 'Z_16'],['X_17', 'Y_17', 'Z_17'],['X_18', 'Y_18', 'Z_18'],['X_19', 'Y_19', 'Z_19'],['X_20', 'Y_20', 'Z_20'],['X_21', 'Y_21', 'Z_21'],['X_22', 'Y_22', 'Z_22'],['X_23', 'Y_23', 'Z_23'],['X_24', 'Y_24', 'Z_24'],['X_25', 'Y_25', 'Z_25'],['X_26', 'Y_26', 'Z_26'],['X_27', 'Y_27', 'Z_27'],['X_28', 'Y_28', 'Z_28'],['X_29', 'Y_29', 'Z_29'],['X_30', 'Y_30', 'Z_30'],['X_31', 'Y_31', 'Z_31'],['X_32', 'Y_32', 'Z_32'],['X_33', 'Y_33', 'Z_33'],['X_34', 'Y_34', 'Z_34'],['X_35', 'Y_35', 'Z_35'],['X_36', 'Y_36', 'Z_36'],['X_37', 'Y_37', 'Z_37'],['X_38', 'Y_38', 'Z_38'],['X_39', 'Y_39', 'Z_39'],['X_40', 'Y_40', 'Z_40'],['X_41', 'Y_41', 'Z_41'],['X_42', 'Y_42', 'Z_42'],['X_43', 'Y_43', 'Z_43'],['X_44', 'Y_44', 'Z_44'],['X_45', 'Y_45', 'Z_45'],['X_46', 'Y_46', 'Z_46'],['X_47', 'Y_47', 'Z_47'],['X_48', 'Y_48', 'Z_48'],['X_49', 'Y_49', 'Z_49'],['X_50', 'Y_50', 'Z_50'],['X_51', 'Y_51', 'Z_51'],['X_52', 'Y_52', 'Z_52'],['X_53', 'Y_53', 'Z_53'],['X_54', 'Y_54', 'Z_54'],['X_55', 'Y_55', 'Z_55'],[ 'X_56', 'Y_56', 'Z_56'],['X_57', 'Y_57', 'Z_57'],['X_58', 'Y_58', 'Z_58'],['X_59', 'Y_59', 'Z_59'],[ 'X_60', 'Y_60', 'Z_60'],['X_61', 'Y_61', 'Z_61'],['X_62', 'Y_62', 'Z_62'],['X_63', 'Y_63', 'Z_63'],[ 'X_64', 'Y_64', 'Z_64'],['X_65', 'Y_65', 'Z_65'],['X_66', 'Y_66', 'Z_66'],['X_67', 'Y_67', 'Z_67'],['X_68', 'Y_68', 'Z_68'],['X_69', 'Y_69', 'Z_69'],['X_70', 'Y_70', 'Z_70'],['X_71', 'Y_71', 'Z_71'],['X_72', 'Y_72', 'Z_72'],['X_73', 'Y_73', 'Z_73'],['X_74', 'Y_74', 'Z_74'],['X_75', 'Y_75', 'Z_75'],['X_76', 'Y_76', 'Z_76'],['X_77', 'Y_77', 'Z_77'],['X_78', 'Y_78', 'Z_78'],['X_79', 'Y_79', 'Z_79'],['X_80', 'Y_80', 'Z_80'],['X_81', 'Y_81', 'Z_81'],['X_82', 'Y_82', 'Z_82'],['X_83', 'Y_83', 'Z_83'],['X_84', 'Y_84', 'Z_84'],['X_85', 'Y_85', 'Z_85'],['X_86', 'Y_86', 'Z_86'],['X_87', 'Y_87', 'Z_87'],['X_88', 'Y_88', 'Z_88'],['X_89', 'Y_89', 'Z_89'],['X_90', 'Y_90', 'Z_90'],['X_91', 'Y_91', 'Z_91']]
total_dataframe = temp_df = pd.DataFrame(columns=alt_heading)
count = internal_counter = 0

#Process received data and create a dataframe
def Create_Dataframe(string_data):
    global count, internal_counter, total_dataframe
    total_data = string_data
    total_data = total_data.split('|')
    total_data.pop(0)
    for instance in total_data:
        df = pd.DataFrame(columns = alt_heading)
        instance = instance.split(';')
        time_val = instance.pop(0)
        df.loc[count,'Timestamp'] = float(time_val)
        instance.pop()
        for joint_data in instance:
            joint_data = joint_data.split(":")
            joint_name = joint_data.pop(0)
            joint_data = joint_data[0].split(",")
            df.loc[count,jointcoord_heading[internal_counter][0]] = float(joint_data[0])
            df.loc[count,jointcoord_heading[internal_counter][1]] = float(joint_data[1])
            df.loc[count,jointcoord_heading[internal_counter][2]] = float(joint_data[2])
            internal_counter += 1
        total_dataframe =pd.concat([total_dataframe,df], verify_integrity=True, ignore_index=True)
        internal_counter = 0
        count += 1
    return total_dataframe

#Plot scatterplot graph to show movement of joint
def Scatterplot_graph(joint,total_dataframe,position):
    label = ("Movement of " + str(joint))
    x_pos = position
    y_pos = x_pos + 1
    X_val = total_dataframe.iloc[:,x_pos]
    Y_val = total_dataframe.iloc[:,y_pos]
    plt.xlim(-1.25,1.25)
    plt.ylim(-1.25,1.25)
    plt.title(label)
    plt.scatter(X_val,Y_val, color = 'r', zorder = 1)
    plt.plot(X_val,Y_val, color = 'b', zorder = 2)
    plt.xlabel = "X - Coordinate"
    plt.ylabel = "Y - Coordinate"
    plt.show()


s.bind(('IP Address', 'PortNumber')) #Bind socket to address
s.listen(1) #Setup TCP listener
conn, addr = s.accept() #Accept connection
print("The IP address is",addr)
try:
    while 1:
        data = conn.recv(16392) #Receive data from socket
        if data:
            temp_data = data.decode("utf-8") #Decode binary data
            string_data = string_data + temp_data
except:
    Create_Dataframe(string_data) #Calling function to process data
    time_val = str(time.time())
    csv_label = time_val+'.csv'
    total_dataframe.to_csv(path_or_buf=csv_label, index = False, float_format='%20f') #Creating a CSV file from dataframe
    Scatterplot_graph('root',total_dataframe,1) #Plotting graph of root joint
    Scatterplot_graph('left_hand_joint',total_dataframe,66) #Plotting graph of left_hand_joint
    Scatterplot_graph('right_hand_joint',total_dataframe,199) #Plotting graph of right_hand_joint
    Scatterplot_graph('head_joint',total_dataframe,154) #Plotting graph of head_joint
    Scatterplot_graph('right_Leg_joint',total_dataframe,25) #Plotting graph of right_Leg_joint
    Scatterplot_graph('left_Leg_joint',total_dataframe,10) #Plotting graph of left_Leg_joint
