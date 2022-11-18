#!/usr/bin/python

import os
import open3d as o3d
import numpy as np


def rotate_z_axis(pcd_file_name, r):

    print("start rotation process :{}".format(pcd_file_name))
    pcd_load = o3d.io.read_point_cloud(pcd_file_name)
    # o3d.io.write_point_cloud("sink_pointcloud.pcd", pcd)

    # o3d.visualization.draw_geometries([pcd_load])

    # rotate pointcloud
    # https://stackoverflow.com/questions/65581304/rotate-a-pointcloud-in-z-axis
    R = pcd_load.get_rotation_matrix_from_xyz(r)
    pcd_load = pcd_load.rotate(R, center=(0, 0, 0))

    o3d.io.write_point_cloud(pcd_file_name, pcd_load)
    print("finish")


def get_pcd_file_name_list(tag_dir_path):

    files = os.listdir(tag_dir_path)
    file_list = [
        f for f in files if os.path.isfile(
            os.path.join(
                tag_dir_path, f))]

    print(file_list)

    return file_list


def process():

    target_dir_path = "./"
    file_name_list = get_pcd_file_name_list(target_dir_path)

    r_euler = (np.pi, 0, 0)

    for file_name in file_name_list:

        rotate_z_axis(file_name, r_euler)


if __name__ == '__main__':

    process()
