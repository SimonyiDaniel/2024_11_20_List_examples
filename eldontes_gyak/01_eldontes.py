'''
Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).

A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
'''
lista = [2, 5, 4, 8, 9, 11, 10, 12]
harommal_oszthatok = []
talalat = False
index = 0
t = True
while index < len(lista):
    if lista[index] % 3 == 0:
        harommal_oszthatok.append(index)
    index = index + 1

if t:
    print(f'Van a listában hárommal osztható szám, ezek a számok:{str(lista[harommal_oszthatok])}.')
else:
    print('Nincs a listában hárommal osztható szám.')