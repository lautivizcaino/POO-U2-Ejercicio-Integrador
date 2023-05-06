from materia import MateriaAprobada as Materia
from gestorAlumnos import GestorAlumnos
import csv
class GestorMaterias:
    __listaMaterias=None
    def __init__(self):
        self.__listaMaterias=[]
    def agregarMateria(self,materia):
        self.__listaMaterias.append(materia)
    def leerArchivo(self):
        file= open('materiasAprobadas.csv')
        reader= csv.reader(file,delimiter=';')
        cab=True
        for row in reader:
            if cab:
                cab=False
            else:
                dni=int(row[0])
                nombre=row[1]
                fecha=row[2]
                nota=int(row[3])
                aprobacion=row[4]
                unaMateria=Materia(dni,nombre,fecha,nota,aprobacion)
                self.agregarMateria(unaMateria)
        file.close()
    def informarPromedio(self,dni):
        totCon=0.0
        iCon=0
        totSin=0.0
        iSin=0
        for materia in self.__listaMaterias:
            if dni==materia.getDni():
                totCon+=materia.getNota()
                iCon+=1
                if materia.getNota()>=6:
                    totSin+=materia.getNota()
                    iSin+=1
        print('\nPromedio con aplazos: %.2f'%(totCon/iCon))
        print('Promedio sin aplazos: %.2f\n'%(totSin/iSin))
    
    def mostrarInforme(self,nombre,listaAlumnos):
        print('DNI         Apellido y nombre       Fecha       Nota   Año que cursa')
        for materia in self.__listaMaterias:
            if nombre==materia.getNombre():
                if materia.getNota()>=7 and materia.getAprobacion()=='P':
                    alumno=listaAlumnos.getAlumno(materia.getDni())
                    print('%d     %s %s     %s      %d         %d'%(alumno.getDni(),alumno.getApellido(),alumno.getNombre(),materia.getFecha(),materia.getNota(),alumno.getAño()))
    
    def __str__(self):
        s=''
        for i in self.__listaMaterias:
            s+= str(i) + '\n'
        return s