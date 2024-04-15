import numpy as np
import open3d as o3d


def read_rgbd_image(color_file, depth_file, convert_rgb_to_intensity, config):
    print(color_file)
    print(depth_file)
    color = o3d.io.read_image(color_file)
    depth = None
    # if depth_file ends with .exr
    if depth_file.endswith('.exr'):
        # enable openexr support for cv2
        import os
        os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"
        import cv2
        depth = cv2.imread(depth_file, cv2.IMREAD_UNCHANGED)
        numpy_depth = np.array(depth)
        depth = o3d.geometry.Image(numpy_depth)
    else:
        depth = o3d.io.read_image(depth_file)
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color,
        depth,
        depth_scale=config["depth_scale"],
        depth_trunc=config["depth_max"],
        convert_rgb_to_intensity=convert_rgb_to_intensity)
    return rgbd_image
