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

def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    ##Function takes in a file and reads line by line using a generator/iterator
    ##Step 1 get file, open file, read file line by line
    ##Step 2: split the lines \n, split at the separator
    ##Step 3: implementing next()
    try:
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
