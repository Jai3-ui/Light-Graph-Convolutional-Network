#Open jester.txt and split it into two files, train.txt and test.txt. Randomly split 80% to train_jester.txt and 20% to test_jester.txt.
#
import random
import numpy as np
import pandas as pd
import os
import sys
import csv
import shutil
import time

# Open jester.txt 
f = open("BXBOOK.txt", "r")
# Read jester.txt
lines = f.readlines()
# Close jester.txt
f.close()
print(len(lines))
#Now randomly split 80% to train_jester.txt and 20% to test_jester.txt.
# Open train_jester.txt
f = open("train_book.txt", "w")
# Open test_jester.txt
f1 = open("test_book.txt", "w")
# Write to train_jester.txt and test_jester.txt
for line in lines:
    r = random.random()
    if r < 0.8:
        f.write(line)
    else:
        f1.write(line)

# Close train_jester.txt
f.close()
# Close test_jester.txt
f1.close()

#Print the no. of lines in train_jester.txt and test_jester.txt
# Open train_jester.txt
f = open("train_book.txt", "r")
# Read train_jester.txt
lines = f.readlines()
# Close train_jester.txt
f.close()
# Print the no. of lines in train_jester.txt
print(len(lines))

# Open test_jester.txt
f = open("test_book.txt", "r")
# Read test_jester.txt
lines = f.readlines()
# Close test_jester.txt
f.close()
# Print the no. of lines in test_jester.txt
print(len(lines))
