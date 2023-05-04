import sys

class Calculadora:

    def __init__(self):
        self.datos_brutos = []
        self.datos_ordenados = []
        self.resultados = []
        self.switcher={
            '1': self.case_1,
            '2': self.case_2,
            '3': self.case_3
        }
        print('Bienvenido')
        self.calculadora()

    def calcular_media(self, numeros):
        suma = 0
        for num in numeros:
            suma += int(num)
        media = int(suma) / len(numeros)
        return media

    def calcular_mediana(self, numeros_ordenados):
        n = len(numeros_ordenados)
        if n % 2 == 0:
            mediana = int((numeros_ordenados[n//2] + numeros_ordenados[n//2 - 1])) / 2
        else:
            mediana = numeros_ordenados[n//2]
        return mediana

    def calcular_moda(self, numeros):
        repeticiones = {}
        for num in numeros:
            if num in repeticiones:
                repeticiones[num] += 1
            else:
                repeticiones[num] = 1
        moda = []
        max_rep = max(list(repeticiones.values()))
        for num, rep in repeticiones.items():
            if rep == max_rep:
                moda.append(num)
        return moda

    def write(self):
        with open('archivo.txt', 'w') as f:
            for i in range(max(len(self.datos_brutos), len(self.datos_ordenados), len(self.resultados))):
                if i < len(self.datos_brutos):
                    f.write(str(self.datos_brutos[i]))
                f.write('\t')
                if i < len(self.datos_ordenados):
                    f.write(str(self.datos_ordenados[i]))
                f.write('\t')
                if i < len(self.resultados):
                    f.write(str(self.resultados[i]))
                f.write('\n')  # Salto de línea para escribir la siguiente fila


    def get_dat(self):
        condition = True
        while condition:
            dato = input('Ingrese el dato o Q para salir\n')
            if dato == 'Q' or dato == 'q':
                condition = False
            else:
                self.datos_brutos.append(dato)
        

    def order(self):
        self.datos_ordenados = sorted(self.datos_brutos, key=int)
        self.resultados.append('Media')
        self.resultados.append(self.calcular_media(self.datos_ordenados))
        self.resultados.append('Mediana')
        self.resultados.append(self.calcular_mediana(self.datos_ordenados))
        self.resultados.append('Moda')
        self.resultados.append(self.calcular_moda(self.datos_ordenados))

    def read(self):
        with open("archivo.txt", "r") as f:
            for line in f:
                values = line.split("\t")
                first_column = values[0]
                self.datos_brutos.append(first_column)

        

    def case_1(self):
        self.get_dat()
        self.order()
        self.write()
        return False

    def case_2(self):
        self.read()
        self.get_dat()
        self.order()
        self.write()
        return False

    def case_3(self):
        return True

    def switch(self, option):
        func = self.switcher.get(option, lambda: print('Opcion no valida'))
        return func()

    def calculadora(self):
        while True:
            self.datos_brutos.clear
            self.datos_ordenados.clear
            self.resultados.clear
            option = input('Seleccione la opción que desea realizar\n\t1.-Ingresar datos desde cero\n\t2.-Continuar ingresando datos\n\t3.-Salir\n')
            if self.switch(option):
                break        

Calculadora()