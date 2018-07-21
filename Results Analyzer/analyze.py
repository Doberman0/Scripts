'''
Making a script which analyzes the results of 3rd year CS students @ UCL
The analysis is based on the 2016-2017 result (obtained via Moodle)
Ranks subjects according to the average mark obtained
'''

import csv, sys

'''
Module_info contains the module code (E.g. COMP3011) as key
and a 2-list [module_score, number_of_people_who_took_it] as value.
The idea is then to go through module_info and workout the mean
for each module. Then, we rank the results.
'''
module_info = {}
file = 'SampleResults.csv'

def workOutAverages():
    module_averages = []
    for module in module_info.keys():
        module_averages.append((module, int(module_info[module][0])/int(module_info[module][1])))
    return module_averages

def outputOrder(module_averages):
    module_averages.sort(key = lambda x: x[1]) #sorts module_averages by average score
    module_averages.reverse()
    for pair in module_averages:
        print('The module %s has an average score of %i' % pair)

def extractValuesFromFile():
    with open(file, newline = '') as results:
        file_reader = csv.reader(results)
        while True:
            #Extracting module codes and marks
            try:
                modules = next(file_reader)[:-1]
                marks = next(file_reader)[:-1]
            except StopIteration: #i.e. you get to the end of the file
                break

            #Putting these modules & scores into the
            for module in range(len(modules)): #module is an index
                cur_module = modules[module] #E.g. COMP3011
                if cur_module in module_info:
                    module_info[cur_module] = [int(module_info[cur_module][0]) + int(marks[module]),
                                               int(module_info[cur_module][1]) + 1]
                else:
                    module_info[cur_module] = [int(marks[module]), 1]


if __name__ == '__main__':
    extractValuesFromFile()
    outputOrder(workOutAverages())
