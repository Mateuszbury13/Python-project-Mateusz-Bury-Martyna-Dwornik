# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:03:58 2020

@author: Mateusz
"""


t = 0
while t<1:
  slowo = input("\nPodaj słowo którego odmiane chcesz otrzymać: ")
  print("\n")

  temp2=slowo

  #odmiana regularna
  dlugosc = len(slowo)-2
  #print(dlugosc)
  
   #len

  if (slowo[-3]=='e' and slowo[-2]=='l' and slowo[-1]=='n'):
    #print("2 opcja")
    #ich
    slowo = slowo[0:len(slowo)-3]
    slowo = slowo + "le"
    print("Ich",slowo)

    # du
    slowo = slowo[0:len(slowo)-2]
    slowo = slowo + "elst"
    print("Du",slowo)

    # er/sie/es
    slowo = slowo[0:len(slowo)-4]
    slowo = slowo + "elt"
    print("Er / sie / es",slowo)

    #wir
    print("Wir",temp2)

    # Ihr
    slowo = slowo[0:len(slowo)-1]
    temp = "t"
    ihr = slowo + temp
    print("Ihr",ihr)

    #Sie
    print("Sie",temp2)