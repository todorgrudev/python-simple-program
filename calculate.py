import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-in','--input', help='Name of input txt file', required=True)
parser.add_argument('-out','--output', help='Name of output file', required=True)
args = vars(parser.parse_args())

# Global var
sep = '\t'
name_table = set()
in_time = ""
out_time = ""
count_in = 0
count_out = 0
 
# Get file names
input_file_name = args['input']
output_file_name = args['output'] 

# Open input file and read all lines in lines
target = open(input_file_name, 'r')
lines = target.readlines()
target.close()

file_result = open(output_file_name, 'w')

# Get all persons
for line in lines:
    line = line.replace('\n', '')
    words = line.split(sep)
    name_table.add(words[3])
        
for person in name_table:
    in_time = ""
    out_time = ""
    for line in lines:
        line = line.replace('\n', '')
        words = line.split(sep)
        
        # Match person
        if words[3] == person: 
            # First check-in 
            if in_time == "":
                if words[2].find("vhod") >= 0:
                    in_time = words[0]
                else: 
                    in_time = "error"
                
            # Last check-in 
            if words[2].find("izhod") >= 0: # match
                out_time = words[0]
            
    print("%s\t%s\t%s" % (person, in_time, out_time))
    file_result.write ("%s\t%s\t%s\n" % (person, in_time, out_time))
file_result.close()     
