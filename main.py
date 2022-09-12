
print("Övning 1")

print("1.- Vad blir utskriften när följande programrader körs? ")

print(10+3, 6*3, 7%2, 3+4*5, (5*2)%3)
print("5+6")
print("a>b = A är stor än B")
print("a*b<a = a gånger b är minda än a")
print("a==b = a och b är lika")
print("b==a or b==3 = b och a är lika eftersom har samma nummer (3)")
print("8"+"12")
print("6-8")
#print("3"-"10") #Kommer unsupported operand type(s) for -: 'str' and 'str'

print("2.- I denna uppgift ska ni testa att skapa och tilldela variabler av olika datatyper.")

value_int = 10 # eller int = 10
print(value_int)

value_string = "Python" # eller str = "Python"
print(value_string)

value_float = 12.43 # eller float = 12.43
print(value_float)

print("3. or 4.- Skriv ett program som tar in ett tal från användaren./"
      "Programmet ska sedan skriva ut om talet är negativt eller positivt./"
      "Du kan utgå från att talet som skrivs in är en siffra./"
      "Bygg på ditt program från uppgift3. När programmet har angivet/"
      "om talet är negativt eller positivt skall användare få frågan ” En gång till?”./"
      "Om användaren svara ”Nej” avslutas programmet.")

tal = int(input("Skriv talet: "))
if tal < 0:
    print("Negative")
else:
   print("Positiv")

nan = input("Engång till? ")

while nan != "nej":
        tal = int(input("Skriv talet: "))
        if tal < 0:
            print("Negativ ")
            nan = input("Engång till? ")
        else:
            print("Positiv ")
            nan = input("Engång till? ")

#Jag kommit inte ihåg hur ni har gjort while loop. Jag byggt den while loop i min egen hand./
#Det inte snyggt fast det fungerar.