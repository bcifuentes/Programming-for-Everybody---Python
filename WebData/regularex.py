import re
files=input("Escriba el nombre del archivo:")
textfile=open(files)

numbers=list()
for line in textfile:
    N=re.findall("[0-9]+",line)
    for ii in N:
        numbers.append(int(ii))
    
print(sum(numbers))
