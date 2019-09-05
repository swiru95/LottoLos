import random as r
from sys import argv
import operator
import os
import time
stat=time.time()
print("Started\n...")
f=open("los.txt",'w')
for i in range(int(argv[1])):
    s=str(sorted(r.sample(range(1,49),6)))
    f.write(s+"\n")
f.close()
f=open("los.txt")
first=True
for i in range(int(argv[1])):
    line=f.readline().strip('\n')
    #print(f"RRR Read {line}")
    if first:
        #print(f"FFF First: {first}")
        list={line:1}
        first=False
        continue
    if line in list:
        x=list[line]
        list[line]+=1
        #print(f"TTT There is a line {line} with {list[line]}, was {x}")
    else:
        list[line]=1
        #print(f"NNN New line: {line} with {list[line]}")
os.system("cls")
sorted_x = sorted(list.items(), key=operator.itemgetter(1))
pr=argv[2]=="all"
for x in sorted_x:
    if pr:
        print(x)
    a=x
f.close()
tin=time.time()-stat
print(f"{a}\n#!FINISH!#\nExecute in: ----{tin}----")
