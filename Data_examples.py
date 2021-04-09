#--------------List-----------
print("----- List -----")
names = ['Jhonatan', 'Paola', 'Andres', 'James', 'Teresa']
for i in names:
    print(i)

print(names[0])
print(type(names))
print("----- end List -----")

#--------------Tuple-----------
print("----- Tuple -----")
names_tp = ('Jhonatan', 'Paola', 'Andres', 'James', 'Teresa')
print(list(enumerate(names_tp)))
print ('Jhonatan --', names_tp.count('Jhonatan'))
print(type(names_tp))
print("----- end Tuple -----")

#--------------Dictionary-----------
print("----- Dictionary -----")
names_dc = {'Jhonatan': 1515,
            'Paola': 1215,
            'Andres': 1918,
            'James': 1951,
            'Teresa': 1586}
for i in names_dc:
    print(names_dc.items())
print(names_dc)
print(names_dc['Jhonatan'])
print(type(names_dc))
print("----- end Dictionary -----")
