from adjunto import Adjunto
from regular import Regular

global lista 
lista=[]

def agregar_docente():
    print('Agregando docente')
    rut = input("Ingrese rut: ")
    nombre = input("Ingrese nombre completo: ")
    typecontrato=int(input('Ingrese un 1 si es docente Regular\nIngrese un 2 si es docente Adjunto: '))
    global grado
    global sueldofinal
    if typecontrato==1:
        grado=0
        while estudios==0:
            sueldobase=int(input('Ingrese sueldo base: '))
            grado=int(input('1.Licenciado\n2.Magister\n3.Doctorado:\nOpcion: '))
            if grado==1:
                grado='Licenciado'
                sueldofinal=100000+sueldobase
            elif grado==2:
                grado='Magister'
                sueldofinal=300000+sueldobase
            elif grado==3:
                grado='Doctorado'
                sueldofinal=700000+sueldobase
            else:
                print('--------')
                print('Ingrese una opcion valida: ')
                
            objd=Regular(rut,nombre,grado,sueldobase)
            print('Docente agregado al sistema')
            print('--------')
    elif typecontrato==2:
        estudios=0
        while estudios==0:

            horastrabajadas=int(input('Ingrese horas trabajadas: '))
            fechacontrato = input("Ingrese su fecha de inicio de contrato: ")
            grado=int(input('1.Licenciado\n2.Magister\n3.Doctorado:\nOpcion: '))
            if estudios==1:
                grado='Licenciado'
                sueldofinal=str(horastrabajadas*15000)
            elif estudios==2:
                grado='Magister'
                sueldofinal=str(horastrabajadas*17000)
            elif estudios==3:
                grado='Doctorado'
                sueldofinal=str(horastrabajadas*20000)
            else:
                print('Ingrese una opcion valida: ')
            objd=Regular(rut,nombre,grado,horastrabajadas)
            print('Docente agregado al sistema')
            print('--------')
        
        objd=Adjunto(rut,nombre,grado,horastrabajadas)
        print('Docente agregado al sistema')
        print('--------')
    else:
        print('Opcion no valida')
        print('--------')
    
    lista.append(objd)
















