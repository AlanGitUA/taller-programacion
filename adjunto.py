from docente import Docente

class Adjunto(Docente):
    def __init__(self, rut='', nombre='', grado='',typedocente="",fechacontrato="",horastrabajadas=0.0, sueldofinal=0.0):
        super().__init__(rut, nombre, grado,typedocente, fechacontrato)
        self.__horastrabajadas=horastrabajadas
        self.__sueldofinal = sueldofinal

    def mostrar_datos(self):
        super().mostrar_datos()
        print('Las horas trabajadas fueron: ', str(self.__horastrabajadas))  
        
        print('El sueldo liquido final es:', str(self.__sueldofinal))