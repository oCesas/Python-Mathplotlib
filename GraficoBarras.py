import csv
import matplotlib.pyplot as plt      


with open('wealth-per-country.csv', 'r') as csv_file:
    arq = csv.reader(csv_file)

    paises = []
    median = []
    mean = []
    pop = []

    next(arq)

    for linha in arq:
        
        if linha == []:
            continue
        paises.append(str(linha[0]))
        median.append(int(linha[1].replace(',', '')))
        mean.append(int(linha[2].replace(',', '')))
        pop.append(int(linha[3].replace(',', '')))


    x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    width = 0.27
    plt.figure(figsize= (11,8))
    for i in x:
        if i == 0:
            plt.bar(i - width, median, width, label='Median Wealth', color='b')
            plt.bar(i, mean, width, label='Mean Wealth', color='g')
            plt.bar(i + width, pop, width, label='Population', color='r')
        
        else:
            plt.bar(i - width, median, width, color='b')
            plt.bar(i, mean, width, color='g')
            plt.bar(i + width, pop, width, color='r')
        
    plt.legend()
    plt.title('Dados socioeconômicos')
    plt.ylabel('Valores')
    plt.xticks(ticks=x, labels=paises)
    

    plt.tight_layout()

    plt.show()