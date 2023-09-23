import io
import csv
import sys

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def csv_to_idx(path,delimiter,criterion):
    population_idx = []
    with io.open(path,"r",encoding = "utf-8") as infile:
        reader = csv.reader(infile, delimiter=delimiter)
        for row in reader:
            if row[6] == "P":
                population_idx.append((int(row[criterion]),row[1]))
        population_idx.sort()
    return population_idx

def create_BST(criteria_idx,min,max):
    median = (min+max)//2
    node = Node(int(criteria_idx[median][0]),criteria_idx[median][1])
    if min > max:
        return None
    node.right = create_BST(criteria_idx,median+1,max)
    node.left = create_BST(criteria_idx,min,median-1)
    return node

def BST_search(node, key):
    if node == None:
        return None
    if node.key == key:
        yield node.value
    if key <= node.key:
        yield from BST_search(node.left, key)
    if key >= node.key:
        yield from BST_search(node.right,key)


L = csv_to_idx("C:/Users/dario/OneDrive - Kantonsschule Romanshorn/School/06_TALIT/HS23/Darta/allCountries.txt","\t",14)
print(len(L))
root = create_BST(L,0,len(L)-1)
print(root.key,root.value)
for e in BST_search(root,8956):
    print(e)