#!/bin/python3
import sys

if len(sys.argv) != 2:
	print("Using: ./removeSpacesAndNewLineFromFile file.txt")
	exit()

fileName = str(sys.argv[1])

with open(fileName, 'r') as f:
    lines = f.readlines()

lines = [line.replace(' ', '').rstrip("\n") for line in lines]

with open(fileName, 'w') as f:
    f.writelines(lines)
    
print("Done!")