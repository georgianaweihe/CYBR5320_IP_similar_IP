Python 3.10.9 (v3.10.9:1dd9be6584, Dec  6 2022, 14:37:36) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import csv
import argparse 
import pandas as pd
import numpy as np
from collections import defaultdict
from scipy.spatial import distance

parser = argparse.ArgumentParser()
parser.add_argument('--inputfile', type=str, required=True, help="The file with the features and labels.")

FLAGS = parser.parse_args()

my_df = pd.read_csv(FLAGS.inputfile) #read in file as pandas df

my_dict = {} #create a dictionary

feature_names = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"]

for index, row in my_df.iterrows():
    src_ip = row.loc["src"]
    for name in feature_names:
        feature = row.loc[name]
        print("feature is ",feature)
...         if src_ip not in my_dict:
...             my_dict[src_ip] = {}
...         if name not in my_dict[src_ip]:
...             my_dict[src_ip][name] = []
...         my_dict[src_ip][name].append(feature)
...         print("for source IP ",src_ip," and feature ",name)
...         print(my_dict[src_ip][name])
... 
... dict_of_numpyarrays = {}
... arr0 = []
... arr1 = []
... arr2 = []
... 
... #for i in my_dict:
... #    for j in my_dict:
... #            num_ips = len(my_dict)
... #            my_array = np.zeros((num_ips,num_ips))
... #            dict_of_numpyarrays[i][j] = my_array
... 
... for name in feature_names:
...     num_ips = len(my_dict)
...     my_array = np.zeros((num_ips,num_ips))
...     dict_of_numpyarrays[name] = my_array
... 
... for name in feature_names:
...     for ip1 in my_dict:
...         print("this is ip1 in my_dict:",ip1)
...         for ip2 in my_dict:
...             print("this is ip2 in my_dict:",ip2)
...             l1 = my_dict[ip1][name]
...             l2 = my_dict[ip2][name]
...             print("this is l1:",l1)
...             print("this is l2:",l2)
...             score = distance.jensenshannon(l1,l2)
...             print("the JS score is",score)
... 
...             print("this is name:",name)
...             print("this is ip1:",ip1)
...             print("this is ip2:",ip2)
