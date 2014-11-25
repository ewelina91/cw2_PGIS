'''
Created on 23 lis 2014

@author: Ewcia
'''

plik=open("owoce.txt","r")
dic={}
for word in plik.read().split():
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
tupleList = sorted(dic.items(), key=lambda(k,v):(v,k), reverse = True)
statystyki=open("statystyki.txt","w")
for i,val in enumerate(tupleList):
    statystyki.write(str(val)+"\n")
plik.close(); 
statystyki.close()