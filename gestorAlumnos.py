from alumno import Alumno
import numpy as np
import csv
class GestorAlumnos:
    __listaAlumnos=None
    __dimension=int
    __incremento=int
    __cantidad=int
    def __init__(self,dimension,incremento=1):
        self.__listaAlumnos= np.empty(dimension,dtype=Alumno)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    
    def agregarAlumno(self,alumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaAlumnos.resize(self.__dimension)
        self.__listaAlumnos[self.__cantidad]=alumno
        self.__cantidad+=1
    def leerArchivo(self):
        file= open('alumnos.csv')
        reader= csv.reader(file,delimiter=';')
        cab=True
        for row in reader:
            if cab:
                cab=False
            else:
                dni=int(row[0])
                apellido=row[1]
                nombre=row[2]
                carrera=row[3]
                año=int(row[4])
                unAlumno=Alumno(dni,apellido,nombre,carrera,año)
                self.agregarAlumno(unAlumno)
        file.close()
    def getAlumno(self,dni):
        for alumno in self.__listaAlumnos:
            if dni==alumno.getDni():
                return alumno
    def ordenarLista(self):
       self.__listaAlumnos.sort()
    def __str__(self):
        s=''
        for i in self.__listaAlumnos:
            s+= str(i) + '\n'
        return s