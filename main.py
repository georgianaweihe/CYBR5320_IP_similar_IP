### Python3 v3.10.9:1dd9be6584

import csv
import argparse 
import pandas as pd
import numpy as np
from collections import defaultdict
from scipy.spatial import distance

### Parse input file
parser = argparse.ArgumentParser()
parser.add_argument('--inputfile', type=str, required=True, help="The file with the features and labels.")
FLAGS = parser.parse_args()

### Read data from input file into pandas dataframe
my_df = pd.read_csv(FLAGS.inputfile) #read in file as pandas df

### Create two empty dictionarys
my_dict = {} #dictionary 1
dict_of_numpyarrays = {} #dictionary 1
### Create list of feature names
feature_names = ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"] #NOTE feature names are hard coded - fix this in future versions

### Store feature data from each IP in dictionary 1
for index, row in my_df.iterrows():
    src_ip = row.loc["src"]  #call the source IP
    for name in feature_names:
        feature = row.loc[name]
        if src_ip not in my_dict:  #if the IP is new, create an empty dictionary 
            my_dict[src_ip] = {}
        if name not in my_dict[src_ip]: #if the IP exists in the dict, create an array for the feature
            my_dict[src_ip][name] = []
        my_dict[src_ip][name].append(feature)
        # print("for source IP ",src_ip," and feature ",name)
        # print(my_dict[src_ip][name])

### Optional different direction
#for i in my_dict:
#   for j in my_dict:
#       num_ips = len(my_dict)
#       my_array = np.zeros((num_ips,num_ips))
#       dict_of_numpyarrays[i][j] = my_array

### Store data from dictionary 1 in dictionary 2 (a dictionary of ten arrays where key value = feature name)
for name in feature_names:
    num_ips = len(my_dict)
    my_array = np.zeros((num_ips,num_ips))
    dict_of_numpyarrays[name] = my_array

### Run analysis
for name in feature_names:
    for ip1 in my_dict:
        for ip2 in my_dict:
            l1 = my_dict[ip1][name] #grab the first vector
            l2 = my_dict[ip2][name] #grab the secoond vector
            score = distance.jensenshannon(l1,l2) #determine jenson-shannon divergence
            dict_of_numpyarrays[name][ip1][ip2] = score #store the similarity score
