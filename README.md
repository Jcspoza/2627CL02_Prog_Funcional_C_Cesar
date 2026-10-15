# 2627CL02_Prog_Funcional_Cifra_Cesar

2627CLxx 

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/26_27Prog_RobotCMMBML_Index: Indice - Taller Programacion y Robotica 2026 - 2027 en CMM Benito Martin Lozano · GitHub](https://github.com/Jcspoza/26_27Prog_RobotCMMBML_Index)

## Clase xx curso 26 27: Programación Funcional - Cifrado Cesar- Resumen inicial

### Tópicos que se van a cubrir

1- Cifrado Cesar básico

- Entender el cifrado cesar

- Pseudo codigo del programa base

2- Conceptos previos de Python

* Ventajas de la programación funcional

* Como se escribe una función en Python

* Cadenas : acceso por índices y rebanado

* Documentación de funciones en python

3- Programa base analisis : cifrado/descifrado con índices

5- Mejoras

* Añadir una letra al alfabeto como la "Ñ"
* Descifrado por fuerza bruta
* Cifrado/descifrado por rebanado
* Mostrar el mensaje cifrado o descifrado en bloques de 5 letras

#### Materiales necesarios

Solo programación: Thonny en PC 

### Enlaces a tutoriales e información

| Tutorial                                                                                 | Nivel  | Notas                                        |
| ---------------------------------------------------------------------------------------- | ------ | -------------------------------------------- |
| [Libro ‘Invent ..’ capitulo 14](https://inventwithpython.com/invent4thed/chapter14.html) | Básico | Explica cifrado Cesar y programa base        |
| https://www.programaenpython.com/fundamentos/strings-en-python/                          | Básico | Cadenas : acceso por índices y rebana además |
|                                                                                          |        |                                              |

### Programas usados en esta clase

| Programa                                                                 | Objetivo                                                                                      | Tópicos cubiertos                                                                | Notas                                                 |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [P2627_cifracesarSimpleI.py](P2627_cifracesarSimpleI.py)                 | Cifrado y descifrado cesar funcional                                                          | Criptografía, Cifrado Cesar / Programacion Funcional / Cadenas acceso y rebanado | Programa BASE I: cifrado / descifrado por índices     |
| [P2627_cifracesarSimpleIÑ.py](P2627_cifracesarSimpleIÑ.py)               | Añadir al alfabeto la letra Ñ                                                                 | idem / qué significa **robustez** en un programa                                 | BASE I + "Ñ"                                          |
| [P2627_cifracesarSimpleIÑ_5l_.py](P2627_cifracesarSimpleIÑ_5l_.py)       | hacer el mensaje cifrado menso reconocible ==> bloques de 5 letras                            | list comprehension con join                                                      | BASE I + "Ñ" + bloques 5 letras                       |
| [P2627_cifracesarSimpleIÑ_Fbruta.py](P2627_cifracesarSimpleIÑ_Fbruta.py) | Ver como la **Programación Funcional** facilita la repetición de codigo                       | Criptografía método fuerza bruta                                                 | BASE I +Ñ+F bruta                                     |
| [P2627_cifracesarSimpleReba.py](P2627_cifracesarSimpleReba.py)           | Ver metodo alternativo de cifrado descifrado con Rebanado usando  cadena auxiliar "alfacrifra | Rebanado / codigo mas compacto                                                   | Programa BASE REBA: cifrado / descifrado por Rebanado |
| [P2627_cifracesarSimpleRebaÑ_5l.py](P2627_cifracesarSimpleRebaÑ_5l.py)   | Todo junto                                                                                    |                                                                                  | Programa BASE REBA + Ñ + bloques 5 letras             |

---

## Programación Funcional, Explicaciones

Hay muchos textos y tutoriales que explican las bondades y los porque de la programación funcional. 

1- En nuestro libro de referencia esta  en [Funciones en Python](https://ellibrodepython.com/funciones-en-python)

2- En Real Python tenemos [functions | Python Best Practices – Real Python](https://realpython.com/ref/best-practices/functions/)

Hay varios temas relacionados con la Programación funcional que son avanzados y no los explicaremos, ( siguiendo nuestro libro de referencia) estarían:

* [📙 Paso por valor y referencia](https://ellibrodepython.com/paso-por-valor-y-referencia)
- [📙 Uso de args y kwargs](https://ellibrodepython.com/args-kwargs-python)
- [📙 Anotaciones en Funciones](https://ellibrodepython.com/function-annotations)
- [📙 Funciones Lambda](https://ellibrodepython.com/lambda-python)
- [📙 Recursividad](https://ellibrodepython.com/recursividad)
- [📕 Decoradores](https://ellibrodepython.com/decoradores-python)
- [📕 Generadores](https://ellibrodepython.com/yield-python)
- [📕 Corrutinas](https://ellibrodepython.com/corrutinas-python)
- [📕 Caching Funciones](https://ellibrodepython.com/caching-python)
- [📕 Programación Funcional](https://ellibrodepython.com/programacion-funcional-python) : map, filter y reduce

## Cifra Cesar Explicaciones

El material explicativo en pdf [Cifra Cesar Explicaciones](CCesar_explicaciones.pdf) cubre los puntos

1- Cifrado Cesar básico

- Entender el cifrado cesar

- Pseudo codigo del programa base

2- Conceptos previos de Python

- Cadenas : acceso por índices y rebanado

- Documentación de funciones en Python

3- Programa base analisis

5- Mejoras

- Añadir una letra al alfabeto como la "Ñ"
- Descifrado por fuerza bruta
- Cifrado/descifrado por rebanado
- Mostrar el mensaje cifrado o descifrado en bloques de 5 letras ==> asi el mensaje cifrado es menos reconocible porque ya no se ven las palabras

---

Todo: 
