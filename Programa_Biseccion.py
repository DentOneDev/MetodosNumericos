import math
# Funcion que evalua f(x) con el metodo de Horner
def f(coeficientes, grado, valor):
    resultado = coeficientes[0]
    i = 1

    while(i <= grado):
        resultado = (resultado * valor) + coeficientes[i]
        i += 1

    return resultado
# FUNCION QUE CALCULA Mx
def Mx(a, b):
    return (a + b) / 2

# METODO DE BISECCION

def biseccion(coeficientes, grado, iInicial, iFinal):
    a = iInicial
    b = iFinal
    nIteraciones = math.ceil((math.log(b - a) - math.log(0.00001)) / math.log(2))

    print "{0}\t{1}\t{2}\t{3}\t{4}".format('n', 'a', 'b', 'Mx', 'f(Mx)f(a)')

    i = 1
    while(i <= nIteraciones):
        x = Mx(a, b)
        Fx = f(coeficientes, grado, x)
        Fa = f(coeficientes, grado, a)


        condicion = Fx * Fa

        print i, "\t{:.4}\t{:.4}\t{:.4}\t".format(a, b, x)


        if(condicion > 0):
            a = x
        elif(condicion < 0):
            b = x
        else:
            x = x


        i += 1
    print "\nLa raiz encontrada es: {0}\n".format(x)


#Programa principal

consulta = '1'
while(consulta != '0'):

    print "Metodo de biseccion\n"


    grado = int(raw_input("Grado de ecuacion: "))   
    print                                                  
    iInicial = float(raw_input("Intervalo inicial: "))      
    iFinal = float(raw_input("Intervalo final: "))         



    coeficientes = []       


    i = grado
    while(i >= 0):                                              
        cof = float(raw_input("Ingresa x^{0}: ".format(i)))     
        coeficientes.append(cof)                                
        i -= 1                                                   


    biseccion(coeficientes, grado, iInicial, iFinal)


    print
    consulta = raw_input("Para salir presiona 0, sino otra tecla: ")
