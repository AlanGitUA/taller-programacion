from docente import Docente

class Regular(Docente):
    def __init__(self, rut='', nombre='', grado='',fechacontrato="", sueldobase=0.0, sueldofinal=0.0):
        super().__init__(rut, nombre, grado, fechacontrato)
        self.__sueldobase=sueldobase 
        self.__sueldofinal=sueldofinal
    def mostrar_datos(self):
        super().mostrar_datos()
        print('El sueldo base es: ', str(self.__sueldobase))
        print('El sueldo liquido final es: ',str(self.__sueldofinal))