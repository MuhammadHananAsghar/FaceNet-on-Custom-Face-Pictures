"""
@author: Muhammad Hanan Asghar
"""

import pickle
import os
import glob

images_folders = glob.glob("cropped/*")
paths = {}
for face_cat in images_folders:
	folder_path = face_cat
	face_cat = face_cat.split("/")[-1]
	paths[face_cat] = "./"+folder_path

file = open("path_dict.p", "wb")
pickle.dump(paths, file)
