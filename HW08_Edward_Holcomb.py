"""
@Author: Edward Holcomb
Homework 08
This is an assignment that is part of the homework assignment
"""
from typing import Any, List, Tuple, DefaultDict, Optional, Sequence, Iterator
import collections
from collections import defaultdict
from datetime import datetime
import prettytable

""" HW08 implementation file layout template"""
def date_arithmetic() -> Tuple[datetime, datetime, int]:
    #This function will return a calculate the length of time between dates using Python's datetime module.
    #tda = three_days_after
    d02272020: datetime = datetime.datetime(2020, 2, 27)
    d02272019: datetime = datetime.datetime(2019, 2, 27)
    d02012019: datetime = datetime.datetime(2019, 2, 1)
    d09302019: datetime = datetime.datetime(2019, 9, 30)
    tdelta: timedelta = datetime.timedelta(days=3)
    tda_02272020: datetime =  d02272020 + tdelta
    tda_02272019: datetime = d02272019 + tdelta
    days_passed_02012019_09302019: int = d09302019 - d02012019
    return (tda_02272020, tda_02272019, days_passed_02012019_09302019)

def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    ##Function takes in a file and reads line by line using a generator/iterator
    ##Step 1 get file, open file, read file line by line
    ##Step 2: split the lines \n, split at the separator
    ##Step 3: implementing next()
    try:
        path = "~/student_majors.txt"
        f = open(path, "r")
        #i to track which line of file
        i = 1
        while True:
            #Returns a list of strings
            line = f.readline()
            #We've reached end of file
            if not line:
                break
            line = line.strip("\n").split(sep)
            if len(line) != fields:
                #path - filename
                #fields - intended fields
                #len(line) - might need to be variable, actual fields
                raise ValueError(
                    f"{path} + {fields} +{len(line)} + {i} + Value Error!")
            else:
                i += 1
                yield line
        f.close()
    except:
        FileNotFoundError(f"Can not find " + {path} + " File not found Error!")

class FileAnalyzer:
    #This class, given a directory name, will search for python files. For each file information will be collected.
    def __init__(self, directory: str) -> None:
        #This initializes the class.
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()  #summerize the python files data


def analyze_files(self) -> None:
    #Function to analyze files
    pass  #implement your code here

def pretty_print(self) -> None:
    #This function will print a Pretty Table showing the data.
    pass  #implement your code here
