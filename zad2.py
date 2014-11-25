'''
Created on 23 lis 2014

@author: Ewcia
'''
menu={}
content={}
with open("menu.txt") as menu2:
    content = menu2.readlines()
    
for linia in content:
    potrawa = linia.split(":")[0]
    cena = float(linia.split(":")[1])
    menu[potrawa] = cena

def zamowienie(zamowienie):
    cena = 0
    for i in zamowienie:
        if i in menu:
            cena+=menu[i]
    return cena*1.10
print ("Cena zamowienia = " + str(zamowienie(["zurek", "ser smazony", "frytki", "surowka", "sok pomaranczowy"])))