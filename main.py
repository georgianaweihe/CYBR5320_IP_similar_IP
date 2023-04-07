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

# Mapping from ip address to integer id
ip2int = {}
numips = 0
for index, row in my_df.iterrows():
    src_ip = row.loc["src"]
    if src_ip not in ip2int:
        ip2int[src_ip] = numips
        numips += 1

for index, row in my_df.iterrows():
    src_ip = row.loc["src"] #call the source IP
    for name in feature_names: 
        feature = row.loc[name]
        print("feature is ",feature)
        if src_ip not in my_dict: #if the IP is new, create an empty dictionary 
            my_dict[src_ip] = {}
        if name not in my_dict[src_ip]: #if the IP exists in the dict, create an array for the feature
            my_dict[src_ip][name] = []
        my_dict[src_ip][name].append(feature)
        print("for source IP "+src_ip+" and feature "+name)
        print(my_dict[src_ip][name])

# create a dictionary of ten arrays (key value = feature name)
dict_of_numpyarrays = {}
for name in feature_names:
    num_ips = len(my_dict)
    my_array = np.zeros((num_ips,num_ips))
    dict_of_numpyarrays[name] = my_array

for name in feature_names:
    for ip1 in my_dict:
        ip1_int = ip2int[ip1]
        for ip2 in my_dict:
            l1 = my_dict[ip1][name]
            l2 = my_dict[ip2][name]
            # Creating histograms
            hist, bin_edges = np.histogram(l1 + l2)
            hist1, _ = np.histogram(l1, bins=bin_edges)
            hist2, _ = np.histogram(l2, bins=bin_edges)
            score = 1 - distance.jensenshannon(hist1, hist2)
            
            # Translating from ip address to integer identifier
            ip2_int = ip2int[ip2]
            dict_of_numpyarrays[name][ip1_int][ip2_int] = score
