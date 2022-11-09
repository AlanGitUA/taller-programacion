from persona import Persona

class Docente(Persona):

    def __init__(self, nombre='', rut='', grado = '', typedocente = '',fechacontrato =''):
        super().__init__(nombre, rut)
        self.__grado = grado
        self.__typedocente = typedocente
        self.__fechacontrato = fechacontrato
    
    def GetGrado(self):
        return self.__grado 
    def SetGrado(self,grado):
        self.__grado = grado
    
    def GetTypedocente(self):
        return self.__typedocente
    def SetTypedocente(self,typedocente):
        self.__typedocente = typedocente

    def GetFechacontrato(self):
        return self.__fechacontrato
    def SetFechacontrato(self,fechacontrato):
        self.__fechacontrato = fechacontrato
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print('Tipo de docente: ',self.__typedocente)
        print('Fecha de inicio de contratro: ', self.__fechacontrato)