class Persona():
    
    def __init__(self,nombre='',rut=''):
        self.__nombre = nombre
        self.__rut = rut
    
    def __str__(self):
        return "Nombre: {} Rut: {}"
    
    def GetNombre(self):
        return self.__nombre
    def GetRut(self):
        return self.__rut
    
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetRut(self,rut):
        self.__rut = rut  
    
    def mostrar_datos(self):
       print('Datos docente')
       print('Nombre: ',self.__nombre)
       print('Rut: ', self.__rut)