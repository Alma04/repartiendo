print ("bienvenido, ingrese nombre y valor separado por ' : ' y termine ingresando exit")
# Defino las variables para utilizar
datos = ""
cantidad_personas = 0
total_importe = 0
nombres = []
importes = []
# Mientras no se ingrese 'exit' sigo el bucle
while datos != "exit":
    datos = input ("ingrese un nombre y el valor: ")
    datos_separados = datos.split(":") # Utilizo el metodo '.split()' para separar los elementos ingresados mediante ' : '
    if len(datos_separados) == 2: # Si la lista es de dos elementos sigo, sino salta un error
        if datos_separados[0].isalpha() and datos_separados[1].isdigit(): # Valido si el priemr elemento es una palabra y el segundo un numero
            cantidad_personas += 1
            total_importe += int (datos_separados[1])
            # Guardo los datos en dos listas
            nombres.append(datos_separados[0]) 
            importes.append(datos_separados[1])
        else:
            print ("Error, ingrese un nombre y un valor separado por ' : ' o 'exit' para terminar")
    elif datos != "exit":
        print ("Error, ingrese un nombre y un valor separado por ' : ' o 'exit' para terminar")
#termino y muestro el resumen
if cantidad_personas == 0:
    print ("Nada que calcular.")
else:
    print ("Los gastos se reparten entre " + (str(cantidad_personas)) + " personas.")
    print ("El total gastado fue de " + (str(total_importe)) + " pesos.")
    total_persona = int (total_importe / cantidad_personas)
    print ("La cuenta por personas queda en " + (str(total_persona)) + " pesos.")
    x = 0 # Utilizo la variable 'x' para guardar el indice de un nombre y buscar su importe correspondiente 
    for nombre in nombres:
        if int (importes[x]) > total_persona:
            print (nombre + " gasto " + (importes[x]) + " y recibe " + str (int (importes[x]) - total_persona))
        elif int (importes[x]) == total_persona:
            print (nombre + " gasto " + (importes[x])+ " y no debe ni recibe nada.")
        else:
            print (nombre + " gasto " + (importes[x]) + " y debe " + str (total_persona - int (importes[x])))
        
        x += 1

    

'''
- 1) Ingresar string por pantalla hasta que se ingrese "exit"
- 2) validar que se ingrese un dato con " : " adentro
- 3) validar que el primer dato sea un Caracter
- 4) validar que el segundo dato sea un nuemro
- 5) contar cuantos veces se repitio el ciclo correctamnte 
- 6) sumar el valor numerico en una variable totalizadora
- 7) guardar en una lista los nombres
- 8) guardar en una lista los importes
- 9) cuando se igresa "exit" se muestra un resumen
- 9.1) se muestra la cantidad de participantes
- 9.2) se muestra el total gastado
- 9.3) se muestra cuanto corresponde pagara a cada participantes
- 9.4) se recorren las listas mostrando el nombre de el participante:
        - si el importe es mayor a lo que corresponde al 9.2, imprimir la pesona 1 recibe (lo que puse - lo que deberia poner)
        - si es igual, imprimir que no debe ni le deben nada
        - si es menor el importe a lo que corresponde a el 9.2, imprimir la persona 1 tiene que pagar (lo que deberia poner - lo que puso)
'''