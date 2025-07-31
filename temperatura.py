# Ejercicio de temperatura

print("\nEste programa realiza conversion entre temperaturas Celcius y Falenheit\n")

try:
    opc = int(input('Presione 1 para convertir de Celcius a Fahrenheit.\nPresione 2 para convertir de Fahrenheit a Celcius.\n\nIntroduzca su opcion: '))

    if opc == 1:

        try:

            temp = float(input('\nIntroduzca la temperatura que desea convertir: '))
            res = round((temp*(9/5))+32, 1)

            print(f"\nLa temperatura es: {res} grados Fahrenheit.\nFin del programa.\n")
            ("Fin del programa.\n")

        except ValueError:

            print("\nEste programa solo admite valores numericos, reinicie el programa.\nFin del programa.\n")

    elif opc == 2:

        try:

            temp = float(input('\nIntroduzca la temperatura que desea convertir: '))
            res = round((temp-32)*(5/9), 1)

            print(f"\nLa temperatura es: {res} grados Celcius.\nFin del programa.\n")

        except ValueError:

            print("\nEste programa solo admite valores numericos, reinicie el programa.\nFin del programa.\n")

    else:
        
        print("\nLa opcion marcada no existe, reinicie el programa.\nFin del programa.\n")

except ValueError:
    print("\nEste programa solo admite valores numericos, reinicie el programa.\nFin del programa.\n")