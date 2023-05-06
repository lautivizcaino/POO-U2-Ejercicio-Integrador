class Alumno:
    __dni=int
    __apellido=str
    __nombre=str
    __carrera=str
    __año=int
    def __init__(self,dni,apellido,nombre,carrera,año):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__año=año
    
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getAño(self):
        return self.__año
    def __lt__(self,otro):
        return self.__año<otro.__año or self.__apellido<otro.__apellido
    def __str__(self):
        return '%s %s %s %s %s'%(self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__año)