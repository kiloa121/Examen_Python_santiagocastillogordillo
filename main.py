from Modulos.nomina import*
cargarDatos()
print(empleados)
while True:
    print("""
        -----------------------------------------
        -               Nomina-Acme             -
        -----------------------------------------
        - (1)Registro de Empleado               -
        - (2)Registro de inasistencia           -
        - (3)Registro de Bonos Extras-Legales   -
        - (4)Calcular Nomina                    -
        - (0)Salir                              -
        -----------------------------------------
        
        """)
    opcion = input("Ingrese la Opcion Deseada : 1/2/3/0\n")

    if opcion == "0":
        print("Saliendo del programa...")
        break
          
    if opcion == "1":
        print("REGISTRO DE EMPLEADO")
        try:
            id = input("Ingrese Numero de Identificacion del Empleado:\n")
            nombre = input("Ingrese Nombre del Empleado\n")
            cargo = input("Ingrese el Cargo del Empleado\n")
            salario = int(input("Ingrese el Salario del Empleado\n"))
            registrarEmpleado(id, nombre, cargo, salario)
        except ValueError:
            print("Error:Ingresar un valor numero para salario")

    if opcion == "2":
        print("REGISTRO DE INASISTENCIAS")
        id = input("Ingrese Numero de Identificacion del Empleado:\n")
        fecha = input("Ingrese Fecha de la Inasistencia:\n") 
        registrarInasitencia(id, fecha,)

    if opcion == "3":
        print("REGISTRO DE BONOS EXTRAS-LEGALES")
        id = input("Ingrese Numero de Identificacion del Empleado:\n")
        fecha = input("Ingrese Fecha del bono:\n ")
        valor = input("Ingrese valor del bono:\n ")
        concepto = input("Ingrese concepto del bono:\n ")
        registrarBono(id, fecha , valor, concepto)

    if opcion == "4":
        print("CALCULAR NOMINA")
        id = input("Ingrese Numero de Identificacion del Empleado:\n")
        salarioNeto = calcularnomina(id)
        if salarioNeto is not None:
            print(f"El salario neto de {id} es: {salarioNeto}")
         

