'''
#permiso para leer y escribir
with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea 1 \n')
  file.write('otra linea 2\n')
  file.write('mas lineas\n')
'''

#permiso para leer y sobreescribir el archivo
with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea 1 \n')
  file.write('otra linea 2\n')
