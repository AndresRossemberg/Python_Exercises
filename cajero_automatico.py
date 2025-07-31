#Ejercicio de cajero automatico

valor = int
bill_20k = 20000
bill_10k = 10000
bill_5k = 5000
bill_2k = 2000
bill_1k = 1000
resto = 0

print("\nEste programa de cajero automatico, le muestra cuantos billetes le va a dar de cada valor para la cantidad ingresada.\n\nEste programa solo da valores de billetes, no admite monedas, nivalores decimales.")

try:

    valor = int(input("\nIngrese la cantidad que desea retirar: "))

    if valor < 1000:

        print(f"\nEl valor ${valor}, no esta permitido, tiene que ser mayor o igual a $1.000.\n\nReinicie el programa he intente nuevamente\n")
        
    else:

        cantidad_20k = (valor // bill_20k) 

        resto = (valor % bill_20k) 

        cantidad_10k = (resto // bill_10k) 

        resto = (resto % bill_10k) 

        cantidad_5k = (resto // bill_5k) 

        resto = (resto % bill_5k) 

        cantidad_2k = (resto // bill_2k) 

        resto = (resto % bill_2k) 

        cantidad_1k = (resto // bill_1k) 

        resto = (resto % bill_1k) 

        if resto == 0:

            print("\nLos billetes que se le van a entregar van a ser:")
            print(f"\n$20.000: {cantidad_20k} $10.000: {cantidad_10k} $5.000: {cantidad_5k} $2.000: {cantidad_2k} $1.000: {cantidad_1k}")

        else:

            print(f"\nEl valor ${valor} no se puede entregar, sobran ${resto} y este cajero no da monedas.\n\nReinicie el programa he intente nuevamente.\n")

except Exception:
    print("\nEste valor no esta permitido, reinicie el programa he intente nuevamente\n")