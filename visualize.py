import numpy as np
import matplotlib.pyplot as plt

def load_ply(file_path):
    points = []
    with open(file_path, 'r') as f:
        header = True
        for line in f:
            if header:
                if line.startswith("end_header"):
                    header = False
                continue
            values = line.strip().split()
            points.append([float(values[0]), float(values[1]), float(values[2])])
    return np.array(points)

def visualize_ply(file_path):
    points = load_ply(file_path)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
    plt.show()

# Replace with your file paths
visualize_ply('E:\computer vision\praxis.ply')
visualize_ply('E:\computer vision\reconstructed.ply')
