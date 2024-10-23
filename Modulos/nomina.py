import os
import json

empleados = {}
#########################################################################################################################################

def cargarDatos():#carga los datos desde un archivo JSON si existe
    if os.path.exists("empleados.json"):
        with open("empleados.json","r") as archivo:
            empleados = json.load(archivo)
    else:

        print("No se encontro datos")
#########################################################################################################################################

def guardarDatos():#guarda los datos
    with open("empleados.json","w") as archivo:
        json.dump(empleados,archivo,indent=4)

###########################################################################################################################################



def registrarEmpleado(identificacion, nombre, cargo, salario): #Registra a un empleado nuevo 
    empleados[identificacion]={
        'nombre':nombre,
        'cargo': cargo,
        'salario': salario,
        'inasistencia':[],
        'bonos': []
    }
    guardarDatos()

#########################################################################################################################################

def registrarInasitencia(identificacion, fecha):#Registro de inasistencia
    if identificacion in empleados:
        empleados[identificacion]['inasistencia'].append(fecha)
        guardarDatos()
    else:
        print("Empleado no encontrado")

###########################################################################################################################################

def registrarBono(identificacion, fecha , valor, concepto):#Registra bono del empleado
    if identificacion in empleados:
        empleados[identificacion]['bonos'].append({'fecha': fecha,'valor': valor,'concepto':concepto})
        guardarDatos()
    else:
        print("empleado no encontrado.")

###############################################################################################################################################

def calcularnomina(identificacion): #calcula la nomina de un empleado
    if identificacion in empleados:
        empleado = empleados[identificacion]
        salarioBase = empleado['salario']
        descuentoSalud = salarioBase * 0.04
        descuentoPension = salarioBase * 0.04
        auxilioTransporte = 1000000 if salarioBase  <= 2000000 else 0
        descuentoInasistencias = (salarioBase / 30) * len(empleado['inasistencias'])

        totalBonos = sum(bono['valor'] for bono in empleado['bonos'])

        salarioNeto = salarioBase - descuentoSalud - descuentoPension - descuentoInasistencias + auxilioTransporte + totalBonos
        
        return salarioNeto
    else:
        print("Empleado no encontrado")




    


    



