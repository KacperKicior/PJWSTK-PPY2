print("Podaj Imie i Nazwisko: ")
name = input()
print("odpowiedz: " + name+"\n")

#Pytanie1
print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: \n")

question1 = {
    "a": "ogladanie telewizji/filmow",
    "b": "czytanie ksiazek",
    "c": "sluchanie muzyki\n",
}

for choice in question1:
    print(choice, question1[choice])

choice = input("Podaj odp: ")
answear1 = question1[choice]
print("odpowiedz: " + answear1+"\n")

#Pytanie2
print("pytanie: W jakich okolicznościach czytasz książki najczęściej? \n")

question2 = {
    "a": "podczas podrozy",
    "b": "w czasie wolnym",
    "c": "w ogole nie czytam\n",
}

for choice in question2:
    print(choice, question2[choice])

choice = input("Podaj odp: ")
answear2 = question2[choice]
print("odpowiedz: " + answear2 +"\n")

#Pytanie3
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? \n")

question3 = {
    "a": "chec poszerzenia wiedzy",
    "b": "czytanie to moje hobby",
    "c": "czytanie jest modne\n",
}

for choice in question3:
    print(choice, question3[choice])

choice = input("Podaj odp: ")
answear3 = question3[choice]
print("odpowiedz: " + answear3 +"\n")

#Pytanie4
print("pytanie: Po książki w jakiej formie sięgasz najczęściej? \n")

question4 = {
    "a": "papierowej",
    "b": "e-booki na komputerze",
    "c": "e-booki na tablecie\n",
}

for choice in question4:
    print(choice, question4[choice])

choice = input("Podaj odp: ")
answear4 = question4[choice]
print("odpowiedz: " + answear4 +"\n")

#Pytanie5
print("pytanie: Ile książek czytasz średnio w ciągu roku? \n")

question5 = {
    "a": "Mniej niz 5",
    "b": "Okolo 5",
    "c": "Wiecej niz 5\n",
}

for choice in question5:
    print(choice, question5[choice])

choice = input("Podaj odp: ")
answear5 = question5[choice]
print("odpowiedz: " + answear5 +"\n")

#Pytanie6
print("pytanie: Jak często średnio czytasz książki?  \n")

question6 = {
    "a": "codziennie",
    "b": "raz w tygodniu",
    "c": "raz w miesiacu\n",
}

for choice in question6:
    print(choice, question6[choice])

choice = input("Podaj odp: ")
answear6 = question6[choice]
print("odpowiedz: " + answear6 +"\n")

#Pytanie7
print("pytanie: W jakim języku książki czytasz?  \n")

question7 = {
    "a": "Polskim",
    "b": "Angielskim",
    "c": "Niemieckim\n",
}

for choice in question7:
    print(choice, question7[choice])

choice = input("Podaj odp: ")
answear7 = question7[choice]
print("odpowiedz: " + answear7+"\n")

print("Odpowiedzi: \n"+answear1+"\n"+answear2+"\n"+answear3+"\n"+answear4+"\n"+answear5+"\n"+answear6+"\n"+answear7+"\n")
print("\n KONIEC ANKIETY\n")



