class MateriaAprobada:
    __dni=int
    __nombre=str
    __fecha=str
    __nota=int
    __aprobacion=str
    def __init__(self,dni,nombre,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
    def getDni(self):
        return self.__dni
    def getNota(self):
        return self.__nota
    def getNombre(self):
        return self.__nombre
    def getAprobacion(self):
        return self.__aprobacion
    def getFecha(self):
        return self.__fecha
    def __str__(self):
        return '%s %s %s %s %s'%(self.__dni,self.__nombre,self.__fecha,self.__nota,self.__aprobacion)