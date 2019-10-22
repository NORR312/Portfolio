import argparse
import sys

def createParser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('filename', type=argparse.FileType('r'), help='<filename.txt>') # open file for reading
    parser.add_argument('operation', choices=['sum', 'avg', 'median'], help='sum, average, median ') # choose the operation for data
    parser.add_argument('comporison', choices=['gt', 'lt', 'eq'], type=str, nargs='?', help='gt: greater than, lt: less than, eq: equal') # check if condition is true, optional 
    parser.add_argument('n', type=int, nargs='?', help='integer for comporison') 
    args = parser.parse_args()
    return args
  
    
        
    
