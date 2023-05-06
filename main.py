
from gestorAlumnos import GestorAlumnos
from gestorMaterias import GestorMaterias
if __name__ == '__main__':
    listaAlumnos=GestorAlumnos(8)
    listaAlumnos.leerArchivo()
    listaMaterias=GestorMaterias()
    listaMaterias.leerArchivo()
    opcion=4
    while opcion!=0:
        print('1 - Informar promedio con aplazas y sin aplazos')
        print('2 - Mostrar informe')
        print('3 - Obtener listado de alumnos ordenado')
        print('0 - Salir\n')
        opcion=int(input('Ingrese la opcion a ejecutar: '))
        if opcion==1:
            print('Punto a\n')
            dni=int(input('Ingrese dni del alumno: '))
            listaMaterias.informarPromedio(dni)
        elif opcion==2:
            print('Punto b\n')
            materia=input('Ingrese nombre de la materia: ')
            listaMaterias.mostrarInforme(materia,listaAlumnos)
        elif opcion==3:
            print('Punto c\n')
            listaAlumnos.ordenarLista()
            print(listaAlumnos)
    else:
        print('\nHa salido del sistema\n')