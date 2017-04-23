# Herzlich willkommen! Dies ist eine Python-Programmdatei

# Die Zeilen, die mit einem Hash (#) beginnen, sind Kommentare
# Du kannst sie lesen, aber sie werden von Python ignoriert

# Wenn du 'GO!' siehst, speichere und führe die Datei aus, um die Ausgabe zu sehen
# Wenn Du eine Zeile mit einem # siehst, folge den Anweisungen
# Einige Zeilen sind Python-Code mit einem # davvor
# Dies bedeutet, dass sie auskommentiert wurden - entferne die # um sie zu aktivieren
# Mache einen Schritt nach dem anderen, speichere und führe das Programm bei jesem Schritt aus!

# 1. Dies ist die Textausgabe

print("Hallo Welt")

# GO!

# 2. Dies ist eine Variable

message = "Level zwei"

# Füge eine Zeile unten hinzu, um diese Variable auszugeben

# GO!

# 3. Die Variable oben wird als String bezeichnet
# Du kannst einzelne oder doppelte Anführungszeichen verwenden
# Du kannst Python fragen, von welcher Art eine Variable ist. Versuche die nächste Zeile auszuführen:
# print(type(message))
# GO!

# 4. Eine andere Variable ist eine Integer-Variable (eine ganze Zahl)
a = 123
b = 654
c = a + b

# Versuche den Wert von c auszugeben
# GO!

# 5. Du kannst auch andere Operationen wie Subtraktion (-) und Multiplikation (*)
# verwenden.
# Probiere ein paar aus, Du musst dazu das Wort mit dem richtigen Operator-Zeichen
# ersetzen

# a mal b
# b minus a
# 12 mal 4
# 103 plus 999

# GO!

# 6. Variablen behalten ihren Wert bis Du ihn änderst

a = 100
# print(a)  # Denk nach - ist das 123 oder 100?

c = 50
# print(c)  # Denk nach - ist das 50 oder 777?

d = 10 + a - c
# print(d)  # Denk nach - Wieviel ist das?

# GO!

# 7. Du kannst auch '+' verwenden um zwei Strings zu verbinden

greeting = 'Hi '
name = ''  # Schreibe Deinen Namen in diesen String

message = greeting + name
# print(message)

#GO!

# 8. Versuche eine Zahl und einen String zu addieren

# age =   # fülle Dein Alter hier als Zahl ein

# print(name + ' ist ' + age + ' Jahre alt')

# GO!

# Siehst Du den Fehler? Man kann nicht Variablen mit verschiedenen
# Typen auf diese Weise mischen.
# Siehst Du auch, wie Dir angezeigt wird, in welcher Zeile der Fehler
# ist?
# Kommentiere die Zeile aus, damit bei der Ausführung kein Fehler mehr
# auftritt.

# 9. Wir können Zahlen in Strings konvertieren:

# print(name + ' ist ' + str(age) + ' Jahre alt')

# GO!

# Hoffentlich gibt das jetzt keinen Fehler?

# Oder wir können den Wert gleich als String in die Variable schreiben:

# age =   # Trage Dein Alter als String ein

# GO!

# Wieder sollte es hoffentlich keinen Fehler geben ;-)

# 10. Ein anderer Typ von Variablen heißt Boolean.
# Diese Variable können den Wert True (wahr) oder False (falsch) annehmen

raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False

# Wir können die beiden Variablen mit == vergleichen

bobs_age = 15
# your_age =    # Trage Dein Alter ein

# print(your_age == bobs_age)  # Hier wird entweder True oder False ausgegeben

# GO!

# 11. Wir können auch größer und kleiner verwenden - mit > und <

# bob_is_older = bobs_age > your_age

# print(bob_is_older)   # Erwartest Du True oder False?

# GO!

# 12. Mit einer If-Anweisung können wir dem Programm Fragen stellen

money = 500
phone_cost = 240
tablet_cost = 200

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:
    message = "Du hast genug Geld für beides"
else:
    message = "Du kannst Dir nicht beide Geräte leisten"

# print(message)  # Welche Ausgabe erwartest Du hier?

# GO!

# Jetzt ändere den Wert von tablet_cost zu 260 und lasse es nochmal laufen.
# Welche Ausgabe siehst Du jetzt?

# GO!

# Ist das richtig? Vielleicht musst Du den Vergleichsoperator to >=
# ändern. Das bedeutet 'größer oder gleich'

raspberry_pi = 25
pies = 3 * raspberry_pi

total_cost = total_cost + pies

if total_cost <= money:
    message = "Du hast auch genug Geld für 3 Raspberry Pis"
else:
    message = "Du kannst Dir keine 3 Raspberry Pis kaufen"

# print(message)   # Welche Ausgabe erwartest Du hier?

# GO!

# 13. Du kannst viele Dinge in einem Variablentypen speichern, den man
# Liste nennt:

colours = ['Rot', 'Orange', 'Gelb', 'Grün', 'Blau', 'Indigo', 'Violett']

# Du kannst überprüfen ob eine Farbe in der Liste enthalten ist

# print('Schwarz' in colours)   # Gibt True oder False aus

# GO!

# Mit append kannst Du Werte zu der Liste hinzufügen

colours.append('Schwarz')
colours.append('Weiss')

# print('Black' in colours)  # Sollte das jetzt anders sein?

# GO!

# Mit extend kannst Du eine Liste mit einer Liste erweitern

more_colours = ['Grau', 'Dunkelblau', 'Pink']

colours.extend(more_colours)

# Versuche die Liste auszugeben um zu sehen, was da alles drin ist.

# GO!

# 14. Du kannst zwei Listen auch mit + addieren

primary_colours = ['Rot', 'Blau', 'Gelb']
secondary_colours = ['Lila', 'Orange', 'Grün']

main_colours = primary_colours + secondary_colours

# Versuche main_colours auszugeben

# 15. Du kannst mit len(deine_liste) herausfinden, wie viele Werte in Deiner Liste sind

# Wie viele Farben sind in main_colours

# GO!

all_colours = colours + main_colours

# Wie viele Farben sind in all_colours?
# Probiere es aus. Überlege Dir vorher, was Du erwartest.

# GO!

# Hast Du den erwarteten Wert bekommen? Falls nicht, warum nicht?

# 16. Du kannst sicher stellen, dass Du keine Duplikate, wenn Du ein Set verwendest

even_numbers = [2, 4, 6, 8, 10, 12]
multiples_of_three = [3, 6, 9, 12]

numbers = even_numbers + multiples_of_three
# print(numbers, len(numbers))
numbers_set = set(numbers)
# print(numbers_set, len(numbers_set))

# GO!

colour_set = set(all_colours)
# Wie viele Farben erwartest Du dieses Mal? Probiere es aus

# GO!

# 17. Du kannst eine Schleife nutzen, um Dir alle Elemente einer Liste
# einzeln anzusehen

my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']

# Jetzt kommt ein mehrzeiliger Kommentar
# Lösche die ''' vor und hinter dem Block um den Kommentar zu deaktiveren
'''
for student in my_class:
    print(student)
'''

# Füge die Namen aller Leute in unserer Gruppe zu dieser Liste hinzu

# Denke an den Unterschied zwischen append und extend. Du kannst beide nutzen

# Jetzt schreibe eine Schleife um eine Zahl (beginne bei 1) vor jedem
# Namen auszugeben

# GO!

# 18. Mit einem Index kann man einen String aufteilen

full_name = 'Dominic Adrian Smith'#

first_letter = full_name[0]
last_letter = full_name[19]
first_three = full_name[:3]  # [0:3 also works]
last_three = full_name[-3:]  # [17:] and [17:20] also work
middle = full_name[8:14]

# Versuche diese Variablen auszugeben, und versuche ein Wort aus den Buchstaben zu bilden

# GO!

# 19. Du kannst auch einen String bei einem bestimmten Buchstaben oder Zeichen aufteilen

my_sentence = "Hallo, mein Name ist Fred"
parts = my_sentence.split(',')

# print(parts)
# print(type(parts))  # Welchen Typ hat diese Variable? Was kannst Du damit machen?

# GO!

my_long_sentence = "This is a very very very very very very long sentence"

# Teile den Satz und versuche dabei, die Zahl der Wörter auszugeben

# GO! (Falls Du Schwierigkeiten hast, gibt es hier noch Tipps)

# Tipp: Bei welchem Zeichen willst Du den String in einzelne Worte aufteilen?
# Tipp: Welchen Typ hat die Variable mit dem aufgeteilten Satz?
# Tipp: Wie kann man diese zählen?

# 20. Du kannst Daten in einem Tupel gruppieren

person = ('Bobby', 26)

# print(person[0] + ' ist ' + str(person[1]) + ' Jahre alt')

# GO!

# (Name, Alter)
students = [
    ('Dave', 12),
    ('Sophia', 13),
    ('Sam', 12),
    ('Kate', 11),
    ('Daniel', 10)
]

# Jetzt schreibe eine Schleife und gebe den Namen und das Alter von jedem Schüler aus

# GO!

# 21. Tupel können eine beliebige Länge haben. Die Beispiele oben sind 2er-Tupel.

# Mache eine Liste von Studenten mit (Name, Alter, Lieblingsfach, Lieblingssport)

# Mache eine Schleife und gebe alles aus

# GO!

# Wähle eine Zahl (passend zum Alter der Schüler)
# Mache eine Schleife, die nur die Studenten ausgibt, die älter als die Zahl sind

# GO!

# 22. Dictionaries beinhalten Schlüssel-Wert-Paare wie ein Adressbuch - oder ein Wörterbuch

phone_numbers = {
    'Laura': '0161 5673 890',
    'Amy': '0115 8901 165',
    'Daniel': '0114 2290 542',
    'Notfall': '112'
}

# Du greifst auf ein Dictionary zu, indem Du den Schlüssel angibt:

# print(phone_numbers['Amy'])

# Du kannst überprüfen, ob ein Schlüssel oder Wert im Dictionary vorhanden ist:

# print('David' in phone_numbers)         # [False]
# print('Daniel' in phone_numbers)        # [True]
# print('112' in phone_numbers)           # [False]
# print('112' in phone_numbers.values())  # [True]
# print(112 in phone_numbers.values())    # [False]

# GO!

# Achtung: 112 war als String eingeben, nicht als Zahl

# Was würde passieren, wenn die Telefonnummern als Zahlen gespeichert würden?

# Versuche Amys Numer zu ändern

# phone_numbers['Amy'] = '0115 236 359'
# print(phone_numbers['Amy'])

# GO!

# Lösche Daniel aus dem Dictionary

# print('Daniel' in phone_numbers)  # [True]
# del phone_numbers['Daniel']
# print('Daniel' in phone_numbers)  # [False]

# GO!

# Du kannst auch eine Schleife über ein Dictionary machen und auf den Inhalt zugreifen:
'''
for name in phone_numbers:
    print(name, phone_numbers[name])
'''

# GO!

# 23. Eine letzte Aufgabe:
# Was ist die Summe aller Ziffern in den Zahlen von 1 bis 1000?

# GO!

# Tipp: range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Tipp: str(87) => '87'
# Tipp: int('9') => 9
