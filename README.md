# PointCloud-Generation-from-Stereo-imageso
Stereo Vision 3D Point Cloud Generation: A Python project to generate 3D point clouds from stereo images using OpenCV and Open3D. Includes stereo rectification, disparity map computation with SGBM, and depth-to-3D projection. Visualize point clouds for applications in robotics, AR, and 3D modeling.
Results
1.Standard StereoSGBM (OpenCV):
![Screenshot 2025-01-08 144820](https://github.com/user-attachments/assets/de183b22-4fc6-44e5-bb12-8beb22c9c394)

The project successfully generates a 3D point cloud from stereo image pairs using the StereoSGBM algorithm provided by OpenCV. The point cloud visualization shows detailed 3D reconstructions of objects, as seen in the example output below:


3D reconstruction of a bicycle using standard StereoSGBM.

  Algorithm: Stereo Semi-Global Block Matching (SGBM)
    Output Format: Point cloud saved as .ply file.
    Performance:
        Clear depth perception of complex objects.
        Real-time rendering with ~81 FPS using Open3D viewer.

The example showcases the robustness of the algorithm in capturing intricate details like the bicycle frame and wheels. Further tuning of stereo matching parameters can improve accuracy and reduce noise.
2.Custom Implementation (From Scratch):
![Screenshot 2025-01-08 145029](https://github.com/user-attachments/assets/ee24d089-7b6d-42f9-99d1-2ae1d45c4e85)



3D reconstruction of a bicycle using the custom disparity algorithm.

   Performance:
        Provides an alternate approach to stereo vision processing.
        Achieves comparable results but requires optimization for better detail and reduced noise.
        Visualization at ~20 FPS.

------------------------------------------------------------------------------------------------------------------------------------------------
Point Clouds Generation

After obtaining the disparity maps, we perform triangulation to compute the corresponding depths, which are used to create point clouds that represent the 3D scene. For a detailed explanation of the point cloud construction process, refer to the report.
Point Clouds from Basic Block Matching:

    Straight View
    Rotated View

Noise filtering and smoothing techniques can enhance the quality of the point clouds. Using more advanced algorithms like StereoSGBM can further improve the point cloud structure, resulting in cleaner and more cohesive 3D models.
Point Cloud from Semi-Global Block Matching (SGBM):

By leveraging stereo vision techniques, 3D scenes like these can be reconstructed from 2D images, providing mobile robots with an understanding of their environment.

To run the standard StereoSGBM library, execute the "main.py" file. For output from the customized code, run all the files to compare the results from both algorithms and observe the differences.
