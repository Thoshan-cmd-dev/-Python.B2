import os.path
import sys
fname = input("Enter the filename to sort: ")
if not os.path.isfile(fname):
    print("file",fname,"doesn't exist")
    sys.exit(0)
infile = open(fname,"r")
lines = infile.readlines()
infile.close()
linelist = []
for line in lines :
    linelist.append(line.strip())
linelist.sort()
outfile = open("sorted.txt","w+")
if not os.path.isfile(fname):
    print("Not able to create sorted.txt")
    sys.exit(0)
for line in linelist:
    outfile.write(line+"\n")
outfile.seek(0,0)
fstr=outfile.read()
print("stored.txt contains",len(linelist),"lines")
outfile.close()