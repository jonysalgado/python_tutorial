import math



def calcularArea(raio2):

    area = math.pi * raio2 ** 2

    return area



if __name__ == '__main__':

    raio1 = float(input("Digite o raio:"))

    area = calcularArea(raio1)

    print("a area é: ", area)
