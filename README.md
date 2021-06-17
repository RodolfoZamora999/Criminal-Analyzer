# Criminal Analyzer.

<br>

## Introducción a la problematica

México es un país que tiene altos indices de criminalidad al año, desde asesinatos,
extorsiones, asaltos, corrupción y muchas cosas más (no es de extrañar que varias de las
ciudades más violentas del mundo estén en México). Muchos de estos crímenes quedan
impunes y otros simplemente no son tomados en cuenta. ¿Causas? Posiblemente la
incompetencia de nuestras autoridades, la indiferencia obtenida por la alta tasa de
criminalidad día con día, tal vez debido a nuestra cultura (?), falta de oportunidades o
educación deficiente. Como sea esto se le tiene dar posibles soluciones a la problemática, no
sera una tarea sencilla pero cada pequeña aportación es de gran utilidad.
He aquí donde entra “Criminal Analyzer” (sí, el nombre esta en inglés para que suene más
profesional), el cual es un software que permite agilizar la identificación de criminales en
base a datos recuperados cerca de la escena del crimen, algunos ejemplo son datos
recuperados en base a descripciones de testigos, cámaras de seguridad cercanas, evidencia
encontrada en la escena del crimen, etc. Una vez recopilada la información esta sera
ingresada al software, posteriormente iniciara la consulta para verificar si las características
de uno de los sospechosos detenidos concuerdan con los recopilados e ingresados al
sistema, en caso de ser afirmativo el sistema notificara de que es el responsable del crimen,
en caso contrario no se le podrá culpar del crimen.
En el siguiente apartado se explica mejor la dinámica del software, ademas se ilustra con una
pequeña infografía. 

<br>
<br>

## Dinámica del proyecto

La dinamia del proyecto es sencilla, antes de interactuar con el sistema se deberá de contar
con los datos recopilados del crimen cometido, estos datos pueden ser recopilados de
diversas formas, como por ejemplo descripciones de testigos, cámaras de seguridad
cercanas, indicios en la escena del crimen, etc. Los datos serán introducidos por medio de
una interfaz en consola, posteriormente se podrá iniciar con la consulta de datos para
determinar si las características del sospechoso introducidas al sistema concuerdan con las
características en la base de conocimiento, en caso de ser cierto el sistema alertara de que
se trata del responsable del crimen, en caso contrario no se podrá culpar de dicho crimen.
Esta dinámica se explica mejor con una infografía, a continuación se muestra el flujo del
sistema desde la escena del crimen hasta la obtención de los resultados por parte del
sistema

![info](documentation/Infografia.svg)

> Infografía de la dinámica del sistema.

<br>

También se adjunta el diagrama de flujo del sistema para tener una idea más concreta del flujo de entrada y salida del sistema. 

![diagram](documentation/DiagramaFlujo.svg)

> Diagrama de flujo del sistema.

<br>
<br>

## Lo que es y no es este proyecto
Posiblemente no quede del todo claro algunos aspectos del proyecto, como por ejemplo el
objetivo de este, sus alcances, limitaciones y que es lo que se plantea resolver, es por eso
que he decidido agregar esta sección explicando con más detalle los puntos anteriores. Para
esto he decidido englobar en dos partes, la primera “Que no es este proyecto” habla sobre
algunas confusiones o ideas erróneas que piensa las personas sobre el proyecto, la segunda
parte es “Que es este proyecto” donde se especifica de manera explicita la razón de ser de
este proyecto.

### Que No es este proyecto:
* No es un sistema impulsado por inteligencia artificial que permite determinar con exactitud quien es el criminal en base a características ingresadas.

* No es un sistema conectado con una base datos policial que permita determinar quien es un criminal en base a antecedentes penales.

### Que Sí es este proyecto:
* Es un sistema que recibe una entrada de características recopiladas anteriormente, genera una base de conocimiento, se hace una consulta comparando los valores de dicha consulta con la base de conocimiento y genera una salida en base a los resultados.

* El objetivo principal del proyecto es simplemente agilizar las comparaciones de características recopiladas del supuesto criminal con las características de los sospechosos detenidos, de esta manera obtenemos resultados más rápidos y acertados sobre quien es el presunto autor de dicho crimen. 
