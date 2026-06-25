import sys,os
file_name = input("enter file name:")
if os.path.isfile(file_name):
    print("file is existed")
    file = open(file_name,mode = 'r',encoding='utf-8')   
else:
    print("file is not existed:",file_name)
    sys.exit()
lcount= wcount = ccount = 0
for line in file:
    lcount = lcount + 1
    words = line.split()
    wcount = wcount + len(words)
    ccount = ccount + len(line)
print("Number of lines:",lcount)
print("Number of charectors:",ccount)
print("Number of words:",wcount)      