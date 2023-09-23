import io
import csv
import json
import bisect
import operator

file = None
counter = 0
places = {}
criteria = {"population 1000000+":None}
myset = set()

with io.open("cities500.txt", "r",encoding="utf-8") as infile:
    file = csv.reader(infile,delimiter="\t")
    for row in file:
        counter += 1
        places[int(row[0])] = {"name":row[1],"asciiname":row[2],"alternatenames":row[3],"latitude":row[4],"longitude":row[5],"feature class":row[6],"feature code":row[7],"country code":row[8],"cc2":row[9],"admin1 code":row[10],"admin2 code":row[11],"admin3 code":row[12],"admin4 code":row[13],"population":row[14],"elevation":row[15],"dem":row[16],"timezone":row[17],"modification date":row[18]}

def create_secondary_idx(dictionary, attribute): 
    idx = {}
    for key,value in dictionary.items():
        id = key
        idx.setdefault(value[attribute],set()).add(id)
    return idx

names = create_secondary_idx(places,"latitude")
for key,entry in names.items():
    if len(entry) > 3:
        #print(key, [(places[x]["name"],places[x]["country code"])  for x in entry])
        pass

def sorted_list_by_attribute(dictionary, attribute):
    tuple_list = []
    for key,value in dictionary.items():
        tuple_list.append((int(value["population"]),int(key)))
    tuple_list.sort()

def range_query(dictionary, range_lower, range_upper):
    population_idx = []
    for key,value in dictionary.items():
        if value["feature class"] == "P":
            population_idx.append((int(value["population"]), int(key)))
    population_idx.sort()

    lower = bisect.bisect_left(population_idx,range_lower,key=operator.itemgetter(0))
    upper = bisect.bisect_right(population_idx,range_upper,key=operator.itemgetter(0))

    for idx in range(lower,upper):
        entity = places[population_idx[idx][1]]
        print(entity["name"],entity["population"])


sorted_list_by_attribute(places,"population")
range_query(places, 10e6, 15e6)

# with io.open("places.json", "r",encoding="utf-8") as infile:
#     dictionary = json.load(infile)
#     print(population_more_less_than_x(dictionary,100000, True))