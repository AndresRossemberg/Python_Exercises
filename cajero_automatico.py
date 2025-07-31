#Ejercicio de cajero automatico

print("\nEste programa de cajero automático, le muestra cuantos billetes le va a dar de cada valor para la cantidad ingresada.\n\nEste programa solo da valores de billetes, no admite monedas, ni valores decimales.")

billetes_entregar = {}
denominaciones = [20000, 10000, 5000, 2000, 1000]

try:

    valor = int(input("\nIngrese la cantidad que desea retirar: "))
    resto = valor

    if valor < 1000:

        print(f"\nEl valor ${valor}, no está permitido, tiene que ser mayor o igual a $1.000.\n\nReinicie el programa he intente nuevamente\n")
        
    else:

        for denominacion in denominaciones:
            
            cantidad_billetes = resto // denominacion

            billetes_entregar[denominacion] = cantidad_billetes

            resto = resto % denominacion

        if resto == 0:

            print("\nLos billetes que se le van a entregar son:\n")

            for denominacion, cantidad in billetes_entregar.items():

                print(f"Billetes de ${denominacion:}: {cantidad}")

            print("\n")

        else:
        
            print(f"\nEl valor ${valor} no se puede entregar, sobran ${resto} y este cajero no da monedas.\n\nReinicie el programa he intente nuevamente.\n")

except Exception:
    print("\nEste valor no está permitido, reinicie el programa he intente nuevamente\n")