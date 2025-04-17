# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:
Este proyecto tiene el propósito de demostrar habilidades técnicas requeridas por las Becas Codeable. El proyecto implica el desarrollo de una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya: Balance Final, Transacción de Mayor Monto y Conteo de Transacciones. Para ello, se puede escoger entre varios lenguajes de programación, como Python, Java, C#, Javascript (Node.js). En este caso, el programa está basado en Python.

## Instrucciones de Ejecución:
1. Descargar los archivo y guardarlos en un folder. O, clonar el repositorio.
2. Inicializar el programa "Procesamiento de Transacciones Bancarias.py".
3. Esto abre un terminal con los datos procesados, donde se presentará el "Reporte de Transacciones".
4. Presionar Enter cuando se haya culminado la lectura del reporte.

## Enfoque y Solución:
La lógica del programa es la siguiente:
1. Importación de la libreria pandas con el propósito de manipular y analizar los datos del CSV.
2. Se lee el archivo CSV mediante el uso de herramientas de pandas y se guarda en dataframe.
3. Primero, inicié con el cálculo del balance final restando la suma del monto de los dataframe tipo crédito y la suma del monto de los dataframe tipo débito.
4. Luego, hallé el monto máximo de las transacciones, con la finalidad de usar este dato para, posterioremnte, almacenar en un dataframe los montos que sean iguales al mayor monto de transacción.
5. Seguidamente, porcedí a contar el número de transacciones que sean tipo Crédito y Débito por separado.
6. Imprimí el título del reporte y el balance final.
7. Dado que podría haber más de una transacción que tenga el mismo monto máximo, usé una lógica "for" para imprimir todas las transacciones con el mismo monto contenidas en el dataframe creado anteriormente.
8. Despúes, se imprimen el conteo de transacciones de Crédito y las de Débito.
9. Finalmente, agregue un linea con una función input() que mantendrá abierto el programa hasta que el usuario presione Enter para cerrarlo.

## Estructura del Proyecto:
Los archivos que componen la solución son los siguientes:
 - "Procesamiento de Transacciones Bancarias.py": Contiene el código que cumple con la tarea asignada apra este proyecto.
 - "Transacciones Bancarias.csv": Contiene los datos que se usarán para realizar el análisis.
 - "main_functions.py": Contiene las funciones que calculan el balance final, mayor transacción, conteo de transacciones tipo débito y crédito. 
