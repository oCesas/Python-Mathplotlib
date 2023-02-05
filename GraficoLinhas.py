import matplotlib.pyplot as plt
import csv

def plotar(x,y,tx,ty):
  plt.plot(x,y,color='k')
  plt.scatter(x,y,label='Valor de cada numero',color='r',marker='*',s=20)
  plt.legend()
  plt.title('Game Number x Game')
  plt.xlabel(tx)
  plt.ylabel(ty)
  plt.savefig('linhas.png')
  plt.show()

numeros=open('sample-line.csv')
linhax=list()
linhay=list()

for linha in numeros:
  semvirgula=linha.split(',')
  linhay.append(semvirgula[1].replace('\n',''))
  linhax.append(semvirgula[0])

titulox=linhax[0].replace('"','')
tituloy=linhay[0].replace('"','')

linhax.pop(0)
linhay.pop(0)

eixox=[int(x) for x in linhax]
eixoy=[int(y) for y in linhay]

plotar(eixox,eixoy,titulox,tituloy)