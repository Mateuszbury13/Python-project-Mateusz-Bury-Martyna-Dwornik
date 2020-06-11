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
    
     # t, d

  elif slowo[-3]=='t' or slowo[-3]=='d':
    #print("3 opcja")
    #ich
    slowo = slowo[0:len(slowo)-2]
    slowo = slowo + "e"
    print("Ich",slowo)

    # du
    slowo = slowo[0:len(slowo)-1]
    slowo = slowo + "est"
    print("Du",slowo)

    # er/sie/es
    slowo = slowo[0:len(slowo)-3]
    slowo = slowo + "et"
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
    
     # chn, ffn, kn, tm

  elif (slowo[-4]=='c' and slowo[-3]=='h'and slowo[-2]=='n') or (slowo[-5]=='f' and slowo[-4]=='f' and slowo[-3]=='n') or (slowo[-4]=='k' and slowo[-3]=='n') or (slowo[-4]=='t' and slowo[-3]=='m'):
    #print("4 opcja")
    #ich
    slowo = slowo[:-1]
    print("Ich",slowo)

    # du
    slowo = slowo[0:len(slowo)-1]
    slowo = slowo + "est"
    print("Du",slowo)

    # er/sie/es
    slowo = slowo[0:len(slowo)-2]
    slowo = slowo + "t"
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