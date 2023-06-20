# zodynas = {
#     "kzodis": "kzodis",
#     "kitas": "kitas",
#     "dar": "dar"
# }
# zodis = input("Iveskite zodi ")
#
# if zodis in zodynas:
#         reiksme = [zodis]
#         print("jusu zodis", ['reiksme'])
# else:
#         print("jusu zodis nerastas " )


# 1. Užduotis: Parašykite programą, kuri paprašytų vartotojo įvesti žodį ir atspausdintų jį atbulai.
# zodis = input("Iveskite zodi: ")
# atbulai = zodis[::-1]
# print("zodis atbulai", atbulai)

# 2. Užduotis: Parašykite programą, kuri patikrintų, ar duotas skaičius yra pirminis.

# def ar_pirminis(skaicius):
#     if skaicius < 2:
#         return False
#     for i in range(2, skaicius):
#         if skaicius % i == 0:
#             return False
#     return True
#
# skaicius = int(input("Įveskite skaičių: "))
# if ar_pirminis(skaicius):
#     print("Skaičius yra pirminis.")
# else:
#     print("Skaičius nėra pirminis.")


# Užduotis: Parašykite programą, kuri rastų didžiausią skaičių iš duoto sąrašo.

# sarasas = [1, 5, 2, 8]
# suma = max(sarasas)
# print("Didziausia ", suma)

# Užduotis: Parašykite programą, kuri apverčia duotą sąrašą atbulai.

# sarasas = [1, 2, 3, 5, 6, 7]
# skaicius = sarasas[::-1]
# print("Atgal ", skaicius)

# Užduotis: Parašykite programą, kuri iš duotų žodžių sąrašo rastų ilgiausią žodį.

# zodziai = ["Obuolys", "Bananas", "Kriause"]
# ilgiausias_zodis = max(zodziai, key=len)
# print("Ilgiausias ", ilgiausias_zodis)

# def zaidimo_lenta(lenta):
#     print("---------")
#     for eilute in lenta:
#         print("|", end=" ")
#         for langelis in eilute:
#             print(langelis, end=" ")
#         print("|")
#         print("---------")
#
# def ar_laimejo(lenta, zaidejas):
#     # Tikriname horizontalias eilutes
#     for eilute in lenta:
#         if eilute.count(zaidejas) == 3:
#             return True
#
#     # Tikriname vertikalias eilutes
#     for stulpelis in range(3):
#         if lenta[0][stulpelis] == zaidejas and lenta[1][stulpelis] == zaidejas and lenta[2][stulpelis] == zaidejas:
#             return True
#
#     # Tikriname įstrižaines
#     if lenta[0][0] == zaidejas and lenta[1][1] == zaidejas and lenta[2][2] == zaidejas:
#         return True
#     if lenta[0][2] == zaidejas and lenta[1][1] == zaidejas and lenta[2][0] == zaidejas:
#         return True
#
#     return False
#
# def ar_lygiosios(lenta):
#     for eilute in lenta:
#         if " " in eilute:
#             return False
#     return True
#
# def zaisti():
#     lenta = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#     zaidejas = "X"
#
#     while True:
#         zaidimo_lenta(lenta)
#
#         # Prašome įvesti koordinates
#         eilute = int(input("Pasirinkite eilutę (1-3): ")) - 1
#         stulpelis = int(input("Pasirinkite stulpelį (1-3): ")) - 1
#
#         # Patikriname ar langelis yra tuščias
#         if lenta[eilute][stulpelis] != " ":
#             print("Šis langelis jau užimtas. Bandykite dar kartą.")
#             continue
#
#         # Užimame langelį
#         lenta[eilute][stulpelis] = zaidejas
#
#         # Patikriname ar yra laimėtojas
#         if ar_laimejo(lenta, zaidejas):
#             zaidimo_lenta(lenta)
#             print("Žaidėjas", zaidejas, "laimėjo!")
#             break
#
#         # Patikriname ar yra lygiosios
#         if ar_lygiosios(lenta):
#             zaidimo_lenta(lenta)
#             print("Lygiosios!")
#             break
#
#         # Keičiame žaidėją
#         zaidejas = "O" if zaidejas == "X" else "X"
#
# zaisti()

# class Calculator:
#     def __init__(self):
#         self.result = 5
#
#     def sudetis(self, skaicius):
#         self.result += skaicius
#
#     def atimtis(self, skaicius):
#         self.result -= skaicius
#
#     def daugyba(self, skaicius):
#         self.result *= skaicius
#
#     def dalyba(self, skaicius):
#         if skaicius != 0:
#             self.result /= skaicius
#         else:
#             print("Dalyba iš nulio negalima!")
#
#     def isvalyti(self):
#         self.result = 0
#
#     def get_result(self):
#         return self.result
#
# skaiciuoklis = Calculator()
#
# while True:
#     print("Pasirinkite norimą veiksmą:")
#     print("1. Sudėtis")
#     print("2. Atimtis")
#     print("3. Daugyba")
#     print("4. Dalyba")
#     print("5. Išvalyti")
#     pasirinkimas = input("Įveskite pasirinkimo numerį: ")
#
#     if pasirinkimas == "1":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.sudetis(skaicius)
#
#     elif pasirinkimas == "2":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.atimtis(skaicius)
#
#     elif pasirinkimas == "3":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.daugyba(skaicius)
#
#     elif pasirinkimas == "4":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.dalyba(skaicius)
#
#     elif pasirinkimas == "5":
#         skaiciuoklis.isvalyti()
#
#     else:
#         print("Neteisingas pasirinkimas")
#
#     print("Result: ", skaiciuoklis.get_result())
#     print()

# class Calculator:
#     def __init__(self):
#         self.result = 5
#
#     def sudėtis(self, skaicius):
#         self.result += skaicius
#
#     def atimtis(self, skaicius):
#         self.result -= skaicius
#
#     def daugyba(self, skaicius):
#         self.result *= skaicius
#
#     def dalyba(self, skaicius):
#         if skaicius != 0:
#             self.result /= skaicius
#         else:
#             print("Dalyba iš nulio negalima!")
#
#     def išvalyti(self):
#         self.result = 0
#
#     def gauti_rezultatą(self):
#         return self.result
#
# skaiciuoklis = Calculator()
#
# while True:
#     print("Pasirinkite norimą veiksmą:")
#     print("1. Sudėtis")
#     print("2. Atimtis")
#     print("3. Daugyba")
#     print("4. Dalyba")
#     print("5. Išvalyti")
#     pasirinkimas = input("Įveskite pasirinkimo numerį: ")
#
#     if pasirinkimas == "1":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.sudėtis(skaicius)
#
#     elif pasirinkimas == "2":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.atimtis(skaicius)
#
#     elif pasirinkimas == "3":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.daugyba(skaicius)
#
#     elif pasirinkimas == "4":
#         skaicius = int(input("Įveskite skaičių: "))
#         skaiciuoklis.dalyba(skaicius)
#
#     elif pasirinkimas == "5":
#         skaiciuoklis.išvalyti()
#
#     else:
#         print("Neteisingas pasirinkimas")
#
#     print("Rezultatas:", skaiciuoklis.gauti_rezultatą())
#     print()

# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def sudetis(self, skaicius1, skaicius2):
#         self.result = skaicius1 + skaicius2
#
#     def atimtis(self, skaicius1, skaicius2):
#         self.result = skaicius1 - skaicius2
#
#     def gauti_rezultata(self):
#         return self.result
#
# skaiciuoklis = Calculator()
#
# while True:
#     print("Pasirinkite norimą veiksmą:")
#     print("1. Sudėtis")
#     print("2. Atimtis")
#     print("3. Baigti programą")
#     pasirinkimas = input("Įveskite pasirinkimo numerį: ")
#
#     if pasirinkimas == "1":
#         skaicius1 = int(input("Įveskite pirmą skaičių: "))
#         skaicius2 = int(input("Įveskite antrą skaičių: "))
#         skaiciuoklis.sudetis(skaicius1, skaicius2)
#         print("Rezultatas:", skaiciuoklis.gauti_rezultata())
#
#     elif pasirinkimas == "2":
#         skaicius1 = int(input("Įveskite pirmą skaičių: "))
#         skaicius2 = int(input("Įveskite antrą skaičių: "))
#         skaiciuoklis.atimtis(skaicius1, skaicius2)
#         print("Rezultatas:", skaiciuoklis.gauti_rezultata())
#
#     elif pasirinkimas == "3":
#         break
#
#     else:
#         print("Neteisingas pasirinkimas")
#
#     print()

# class Automobilis:
#     def __init__(self, marke, metai):
#         self.marke = marke
#         self.metai = metai
#
#     def gauti_info(self):
#         return "Automobilis: " + self.marke + ", Pagaminimo metai: " + str(self.metai)
#
# auto = Automobilis("Volvo", 2020)
# print(auto.gauti_info())

# def suma(a, b):
#     rezultatas = a + b
#     return rezultatas
#
# rezultatas = suma (1,6)
# print(rezultatas)

# class Manoklase:
#     def pasisveikinimas(self, vardas):
#         print("Labas, " + vardas + " Mano vardas " + self.vardas)
#
# obijaktas = Manoklase()
# obijaktas.vardas = "Jonas"
# obijaktas.pasisveikinimas("Petras")
#
# class ManoKlase:
#     def pasisveikinti(self, vardas):
#         print("Labas, " + vardas + "! Mano vardas yra " + self.vardas)
#
# objektas = ManoKlase()
# objektas.vardas = "Jonas"
# objektas.pasisveikinti("Petras")

# skaicius = 1
# while skaicius <= 5:
#     print(skaicius)
#     skaicius += 1

# class Masyvas:
# #     def __init__(self):
# #         self.elementai = []
# #
# #     def prideti_elementa(self, elementas):
# #         self.elementai.append(elementas)
# #
# #     def gauti_elementus_didesnius_uz(self, skaicius):
# #         rezultatas = []
# #         for elementas in self.elementai:
# #             if elementas > skaicius:
# #                 rezultatas.append(elementas)
# #         return rezultatas
# #
# #
# # # Sukuriamas objektas ir pridedami elementai
# # masyvas = Masyvas()
# # masyvas.prideti_elementa(10)
# # masyvas.prideti_elementa(5)
# # masyvas.prideti_elementa(15)
# # masyvas.prideti_elementa(8)
# # masyvas.prideti_elementa(20)
# #
# # # Gauti elementai didesni už 10
# # didziu_uz_10 = masyvas.gauti_elementus_didesnius_uz(10)
# # print(didziu_uz_10)

# def ar_pirminis(self,sk):
#     if sk >= 2:
#         return False
#     for i in range(2, sk):
#         if sk % 2 ==0:
#             return False
#     return True
#
# skaicius = int(input("Įveskite skaicių: "))
# if ar_pirminis(skaicius):
#     print(f"{skaicius} yra pirminis")
# else:
#     print(f"{skaicius} nėra pirminis")

# def ar_pirminis(sk):
#     if sk < 2:
#         return False
#     for i in range(2, sk):
#         if sk % i == 0:
#             return False
#     return True
#
# skaicius = int(input("Įveskite skaičių: "))
# if ar_pirminis(skaicius):
#     print(f"{skaicius} yra pirminis skaičius.")
# else:
#     print(f"{skaicius} nėra pirminis skaičius.")
# import random
#
# def zaidimas():
#     paslaptis = random.randint(1, 100)
#     spejimai = 0
#     atspejimas = False
#
#     print("Sveiki! Aš pasirinkau skaičių nuo 1 iki 100. Jūs turite jį atspėti.")
#
#     while not atspejimas:
#         spejimas = int(input("Įveskite savo spėjimą: "))
#         spejimai += 1
#
#         if spejimas < paslaptis:
#             print("Daugiau!")
#         elif spejimas > paslaptis:
#             print("Mažiau!")
#         else:
#             atspejimas = True
#
#     print(f"Teisingai! Atspėjote skaičių {paslaptis} iš {spejimai} bandymų.")
#
# zaidimas()
# skaicius = int(input("įveskite skaičiu: "))
# if skaicius < 0:
#     print(f"{skaicius} Neigiamas")
# elif skaicius > 0:
#     print(f"{skaicius} Teigiamas ")
# else:
#     print(f"{skaicius} Lygus nuliui")
# skaicius = int(input("įsekite skaičių: "))
# if skaicius % 2 == 1:
#     print(f"{skaicius} yra lyginis")
# else:
#     print(f"{skaicius} nelyginis")
#
# skaicius = int(input("Įveskite skaičių: "))
#
# lyginis_nelyginis = ["nelyginis", "lyginis", "dar"]
# pranešimas = lyginis_nelyginis[skaicius % 2 == 0]
# print(f"Jūsų skaičius yra {pranešimas}")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Amžius negali būti neigiamas")
#
# person = Person("Jonas", 15)
#
# print("Persona:", person.get_name())
# print("Amžius:", person.get_age())
#
# person.set_name("Petras")
# person.set_age(20)
#
# print("Nauja persona:", person.get_name())
# print("Naujas amžius:", person.get_age())
#
# class Student:
#     def __init__(self, student_id, name, age):
#         self.student_id = student_id
#         self.name = name
#         self.age = age
#
#     def get_student_id(self):
#         return self.student_id
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# class StudentManagementSystem:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#         print("Naujas studentas pridėtas.")
#
#     def remove_student(self, student_id):
#         for student in self.students:
#             if student.get_student_id() == student_id:
#                 self.students.remove(student)
#                 print("Studentas pašalintas.")
#                 return
#         print("Studentas su nurodytu ID nerastas.")
#
#     def get_student_info(self, student_id):
#         for student in self.students:
#             if student.get_student_id() == student_id:
#                 print("Studento ID:", student.get_student_id())
#                 print("Vardas:", student.get_name())
#                 print("Amžius:", student.get_age())
#                 return
#         print("Studentas su nurodytu ID nerastas.")
#
#     def show_all_students(self):
#         if len(self.students) == 0:
#             print("Nėra studentų duomenų.")
#             return
#         for student in self.students:
#             print("Studento ID:", student.get_student_id())
#             print("Vardas:", student.get_name())
#             print("Amžius:", student.get_age())
#             print("-----------")
#
#     def run(self):
#         while True:
#             print("-------------")
#             print("Komandos:")
#             print("1 - Pridėti naują studentą")
#             print("2 - Pašalinti studentą")
#             print("3 - Gauti informaciją apie studentą pagal ID")
#             print("4 - Rodyti visus studentus")
#             print("5 - Baigti programą")
#
#             command = input("Įveskite komandos numerį: ")
#
#             if command == "1":
#                 student_id = input("Įveskite studento ID: ")
#                 name = input("Įveskite studento vardą: ")
#                 age = input("Įveskite studento amžių: ")
#                 student = Student(student_id, name, age)
#                 self.add_student(student)
#             elif command == "2":
#                 student_id = input("Įveskite studento ID, kurį norite pašalinti: ")
#                 self.remove_student(student_id)
#             elif command == "3":
#                 student_id = input("Įveskite studento ID, apie kurį norite gauti informaciją: ")
#                 self.get_student_info(student_id)
#             elif command == "4":
#                 self.show_all_students()
#             elif command == "5":
#                 print("Programa baigta.")
#                 break
#             else:
#                 print("Nevalidi komanda. Bandykite dar kartą.")
#
#
# # Pagrindinė programa
# sistema = StudentManagementSystem()
# sistema.run()

# class Studentas:
#     def __init__(self, studento_id, vardas, amzius):
#         self.studento_id = studento_id
#         self.vardas = vardas
#         self.amzius = amzius
#
#     def get_studento_id(self):
#         return self.studento_id
#
#     def get_vardas(self):
#         return self.vardas
#
#     def get_amzius(self):
#         return self.amzius
#
#
# class SarasoValdymas:
#     def __init__(self):
#         self.studentai = []
#
#     def prideti_studenta(self):
#         self.studentai.append(studentas)
#         print("Studentas pridėtas")
#
#     def istrinti_studenta(self):
#         for studentas in self.studentai:
#             if studentas.get_studento_id() == studento_id:
#                 self.studentai.remove(studentas)
#                 print("Studentas pašalintas")
#                 return
#         print("Studentas su nurodytu ID nerastas")
#
#     def get_studento_info(self):
#         for studentas in self.studentai:
#             if studentas.get_studento_id() == studento_id:
#                 print("Studento ID ", studentas.get_studento_id())
#                 print("Vardas ", studentas.get_vardas())
#                 print("Amzius ", studentas.get_amzius())
#                 return
#         print("Studentas su nurodytu ID nerastas")
#
#     def parodyti_visus_studentus(self):
#         if not self.studentai:
#             print("Studentų sąraše nerasta")
#             return
#         for studentas in self.studentai:
#             print("Studento ID ", studentas.get_studento_id())
#             print("Vardas ", studentas.get_vardas())
#             print("Amzius ", studentas.get_amzius())
#
#     def paleisti(self):
#         while True:
#             print("1 - Pridėti naują studentą")
#             print("2 - Pašalinti studentą")
#             print("3 - Gauti informaciją apie studentą pagal ID")
#             print("4 - Rodyti visus studentus")
#             print("5 - Baigti programą")
#
#             komanda = input("Iveskite komanda: ")
#
#             if komanda == "1":
#                 studento_id = input("Iveskite studento ID ")
#                 vardas = input("Iveskite varda ")
#                 amzius = input("Iveskite amziu ")
#                 studentas = Studentas(studento_id, vardas, amzius)
#                 self.prideti_studenta()
#
#             elif komanda == "2":
#                 studento_id = input("Iveskite studento ID kuri norite pašalinti ")
#                 self.istrinti_studenta()
#
#             elif komanda == "3":
#                 studento_id = input("Iveskite studento ID, apie kuri norite gauti informacija ")
#                 self.get_studento_info()
#
#             elif komanda == "4":
#                 self.parodyti_visus_studentus()
#
#             elif komanda == "5":
#                 print("Programa baigta")
#                 break
#
#             else:
#                 print("Komanda neteisinga, bandykite dar kartą")
#
# sistema = SarasoValdymas()
# sistema.paleisti()

# class Studentas:
#     def __init__(self, studento_id, vardas, amzius):
#         self.studento_id = studento_id
#         self.vardas = vardas
#         self.amzius = amzius
#
#     def get_studento_id(self):
#         return self.studento_id
#
#     def get_vardas(self):
#         return self.vardas
#
#     def get_amzius(self):
#         return self.amzius
#
# class SarasoValdymas:
#     def __init__(self):
#         self.studentai = []
#
#     def prideti_studenta(self, studentas):
#         self.studentai.append(studentas)
#         print("Studentas pridėtas")
#
#     def istrinti_studenta(self, studento_id):
#         for studentas in self.studentai:
#             if studentas.get_studento_id() == studento_id:
#                 self.studentai.remove(studentas)
#                 print("Studentas pašalintas")
#                 return
#         print("Studentas su nurodytu ID nerastas")
#
#     def get_studento_info(self, studento_id):
#         for studentas in self.studentai:
#             if studentas.get_studento_id() == studento_id:
#                 print("Studento ID:", studentas.get_studento_id())
#                 print("Vardas:", studentas.get_vardas())
#                 print("Amžius:", studentas.get_amzius())
#                 return
#         print("Studentas su nurodytu ID nerastas")
#
#     def parodyti_visus_studentus(self):
#         if not self.studentai:
#             print("Studentų sąraše nerasta")
#             return
#         for studentas in self.studentai:
#             print("Studento ID:", studentas.get_studento_id())
#             print("Vardas:", studentas.get_vardas())
#             print("Amžius:", studentas.get_amzius())
#
#     def paleisti(self):
#         while True:
#             print("1 - Pridėti naują studentą")
#             print("2 - Pašalinti studentą")
#             print("3 - Gauti informaciją apie studentą pagal ID")
#             print("4 - Rodyti visus studentus")
#             print("5 - Baigti programą")
#
#             komanda = input("Įveskite komandą: ")
#
#             if komanda == "1":
#                 studento_id = input("Įveskite studento ID: ")
#                 vardas = input("Įveskite vardą: ")
#                 amzius = input("Įveskite amžių: ")
#                 studentas = Studentas(studento_id, vardas, amzius)
#                 self.prideti_studenta(studentas)
#
#             elif komanda == "2":
#                 studento_id = input("Įveskite studento ID, kurį norite pašalinti: ")
#                 self.istrinti_studenta(studento_id)
#
#             elif komanda == "3":
#                 studento_id = input("Įveskite studento ID, apie kurį norite gauti informaciją: ")
#                 self.get_studento_info(studento_id)
#
#             elif komanda == "4":
#                 self.parodyti_visus_studentus()
#
#             elif komanda == "5":
#                 print("Programa baigta")
#                 break
#
#             else:
#                 print("Komanda neteisinga, bandykite dar kartą")
#
# sistema = SarasoValdymas()
# sistema.paleisti()
# -----------------------------------------------------------------------------------------------------------
# 1. Parašykite programą, kuri atspausdina visus lyginius skaičius nuo 1 iki 10.
# for skaicius in range(1, 11):
#     if skaicius % 2 == 0:
#         print(skaicius)
# sarasas = [1, 2, 3, 4, 5, 7, 8, 9, 10]
# for skaicius in sarasas:
#     if skaicius % 2 ==0:
#         print(skaicius)
# antras būdas:
# sarasas = range(1,11)
#     if skaicius % 2 ==0:
#         print(skaicius)
#
# trečias būdas
# for skaicius in range(2, 11, 2):
#     print(skaicius)
# ---------------------------------------------------------------------------------------------------
#
# 2. Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą.
#
# sarasas = [1, 2, 3, 4, 5, 7, 8, 9, 10]
# sum = 0
# for skaicius in sarasas:
#     sum += skaicius
# print("Suma", sum)
#
#
# 3.Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20,
# tačiau jei skaičius yra dalijamas iš 3, atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz";
# sarasas = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for skaicius in sarasas:
#     if skaicius % 5 == 0 and skaicius % 3 == 0:
#         print("BuzzFizz")
#     elif skaicius % 5 == 0:
#         print("Buzz")
#     elif skaicius % 3 == 0:
#         print("Fizz ")
#     else:
#         print(skaicius)
#
# 4.Sukurkite klasę "KnygosBiblioteka", turinčią atributą "knygos" (sąrašą) ir metodus "pridėti_knygą" ir "rodyti_knygas".
# Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas bibliotekoje esančias knygas.
#
# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga (self, knyga):
#         self.knygos.append(knyga)
#         for knyga in self.knygos:
#             print("Knyga pridėta sėkminga ", knyga)
#
#     def rodyti_knyga (self):
#         if self.knygos:
#             print("Bibliotekos knygos")
#             for knyga in self.knygos:
#                 print(knyga)
#         else:
#             print("Biblioteka tuscia ")
#
# pridedamknyga = KnygosBiblioteka()
# pridedamknyga.prideti_knyga("Pamote")
# pridedamknyga.prideti_knyga("Pimpackiukai")
# pridedamknyga.rodyti_knyga()

# 5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą,
# kuri suskaičiuoja ir atspausdina visų prekių kainų sumą.
#
# produktai = {
#     "Obuolys" : 2,
#     "Pienas" : 1,
#     "Duona" : 1
# }
#
# suma = sum(produktai.values())
# print(suma)

#Antras būdas
# produktai = {
#     "Obuolys" : 2,
#     "Pienas" : 1,
#     "Duona" : 1
# }
# suma = 0
# for preke in produktai.values():
#     suma += preke
# print(suma)

# aukstis = 5
# eilutes = aukstis+1
# for i in range(1, eilutes +1):
#     print(" " * (eilutes - i), end="")
#     print("*" * (2 * i - 1))
# print(" " * (eilutes - 1),end="")
# print("|")



