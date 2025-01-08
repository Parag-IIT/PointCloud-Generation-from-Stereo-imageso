
# Factor for downscaling of test images
SCALE = 0.5
#Specify image paths
img_path1 = r'E:\computer vision\PointCloud_stereo\bikeL.png'
img_path2 = r'E:\computer vision\PointCloud_stereo\bikeR.png'


###################
# CAMERA PARAMS
###################
# The focal length of the two cameras, taken from calib.txt
FOCAL_LENGTH =  5299.313 #3979.911
               
# The distance between the two cameras, taken from calib.txt
X_A= 1263.818 #1244.772
X_B= 1438.004        #1369.115
Y= 977.763 #1019.507
DOFFS = X_B-X_A
CAMERA_DISTANCE = 177.288 # 193.001