# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

values_list = []

def showObjectKeys(audi):
  for x in audi.values():
    values_list.append(x)
  return values_list
  
print(showObjectKeys(audi))
