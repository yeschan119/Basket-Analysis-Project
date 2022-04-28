#!/usr/bin/env python
# coding: utf-8

import sys
from sys import argv
import pandas as pd
from itertools import combinations # to get combinations of candidate items
import time # to measure execution time
start = time.time()
minimum_support = int(sys.argv[1])
input_path = sys.argv[2]
output_path = sys.argv[3]
input_file = open(input_path,'r')
output_file = ''
original_list = []
int_list = []

# make list with each transaction after remove \n and \t
for temp in input_file:
    temp = temp.rstrip()   # remove \n
    temp = temp.split('\t') # make the list using \t
    int_list = [(int(item_id)) for item_id in temp]  # make the int item
    original_list.append(int_list)
# make dataframe using list transactions
# and remove none value
df = pd.DataFrame(original_list)
df = df.replace([None], [''])
# get number of transactions
num_of_line = len(df.index.tolist())
# get minimum support
min_sup =(num_of_line*minimum_support)//100
# basic size of item sets
k = 1

# get frequencies for all items
def get_frequency(candidate_list):
    frequent_set  = {}
    if k <= 1: # if item_set is one
        for items in candidate_list:
            for item in items:
                if item in frequent_set:
                    frequent_set[item] += 1
                else:
                    frequent_set[item] = 1
    else: # if item_set is bigger than 2
        for items in candidate_list:
            for transaction in original_list:
                # to find frequency in each transaction
                # use union between item_set and each transaction
                temp_set = set(items) & set(transaction)
                # if the size of item_set is same with the result of union
                # item set must be in the transaction
                if len(temp_set) == len(items) and tuple(items) in frequent_set:
                    frequent_set[tuple(items)] += 1  #increase frequency for candidate
                elif len(temp_set) == len(items) and tuple(items) not in frequent_set:
                    frequent_set[tuple(items)] = 1
                else:
                    continue
    return frequent_set
# remove items have smaller frequency than mininum support
def generate_candidate(frequent_list):
    candidate_list = {}
    for key in frequent_list.keys():
        if frequent_list[key] < min_sup:
            continue
        else: # candidate_list is the list for support and confidence
            candidate_list[key] = frequent_list[key]
    return candidate_list

# after getting candidate, make combinations using k(size of items_set)
def get_combinations(candidate_list, k):
    combination_list = []
    if k <= 2: # if item_set is smaller than 2, just can use combination modul.
        candidate = list(candidate_list.keys())
        combination_list = list(combinations(candidate, k))
    else: # if item_set is larger than 2, use each item to avoid duplication.
        for key in candidate_list.keys():
            for i in key:
                if i not in combination_list: # to avoid duplication item
                    combination_list.append(i)
        combination_list = list(combinations(combination_list,k))
    return combination_list

# find support and confidence using candidate set
# make output file using item_set and support and confidence
def output_candidate(candidate_set):
    output_file = ''
    #candidate_set.keys are the candidata list
    support_items = list(candidate_set.keys())
    for items in support_items:
        size = 1 # the unit to group by combinations
        while size < len(items):
            temp_item_set = list(combinations(items, size))
            for item_set in temp_item_set:
                # To avoid duplicated check, use difference of sets
                # And check all possible set to get confidence.
                associative_item_set = set(items) - set(item_set)
                output_file += '{}\t'.format(set(item_set))
                output_file += '{}\t'.format(associative_item_set)
                item_set_frequency = get_item_set_frequency(item_set)
                support, confidence = get_support_confidence(candidate_set[items], item_set_frequency)
                output_file += '{}\t{}\n'.format(support, confidence)
            size += 1
    return output_file

# get frequency of each candidate item_set
def get_item_set_frequency(items):
    item_frequency = 0
    for original in original_list:
        temp_set = set(items) & set(original)
        if len(temp_set) == len(items):
            item_frequency += 1
    return item_frequency

# get support and confidence
def get_support_confidence(group, item_frequency):
    # round to two decimal places
    confidence = format((group/item_frequency * 100),".2f")
    support = format((group/num_of_line * 100),".2f")
    return support, confidence

if __name__ == '__main__':
    candidate_set = original_list[:]
    # repeat until size of candidate_set is zero
    while len(candidate_set)!= 0:
        # get frequent list using candidate_set
        frequent_set = get_frequency(candidate_set)
        k +=1
        # find candidate using frequent set
        candidate_set = generate_candidate(frequent_set)
        # if k > 2, write output file
        if k > 2:
            output_file += output_candidate(candidate_set)
        # make combinations using candidate set
        candidate_set = get_combinations(candidate_set, k)
    f = open(output_path,'w')
    # To remove space for whole data, use replace
    f.write(output_file.replace(' ',''))
    f.close()
    input_file.close()
    print("File output completed!!")
    print("execution time :", str(round((time.time() - start),1))+"s")
