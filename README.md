# Prueba Técnica Sofka
Este repositorio fue creado por el hecho de presentar la prueba técnica para el proceso de selección de Sofka University, escogí hacer esta prueba en Python debido a que el código se podía simplicar mucho con este leguaje y que debido a la prueba, no se requiere escalar el código. Si quieres ver cómo desarrollé dicha prueba, quédate en esta página. En ella se mencionarán los aspectos importantes a tener en cuenta, cómo puedes ejecutar el código y se mencionan todos los casos posibles del test.

# Contenido

1. **Preparación**
  * Debes tener instalado Python3 junto con pip en tu ordenador, para ver detalles de como instalarlo por favor dirígete a esta [página](https://realpython.com/installing-python/) para guiarte como puedes instalar Python3 y en esta [otra](https://pip.pypa.io/en/stable/installation/) para guiarte a instalar pip.
  * También debes de tener instalada la librería de PyQt5, esta la puedes encontrar y ver su proceso de instalación [aquí.](https://pypi.org/project/PyQt5/)
  * Por último, una vez ya tengas instalado Python3 en tu ordenador, debes de tenerlo en ejecución en cmd o en cualquier otro IDE de Python que prefieras. Cuando estés aquí trata de chequear si los siguientes comandos te funcionan:
````
python>>>import sys
````

````
python>>>import random
````

````
python>>>from PyQt5.QtWidgets import QMainWindow
````
2. **Descarga De Archivos**

En este punto ya puedes bajar los archivos encontrados en este repositorio. Ve a la pestaña de "code" y descarga el .ZIP File. También si tienes Git en tu ordenador y te gusta hacer todo a través de la consola lo puedes hacer con el siguiente comando:
````
gh repo clone MauricioZapata00/PruebaTecnicaSofka
````

3. **Ejecución del código y explicación de cada caso**
  * #### Ejecución
  Para ejecutar el programa recuerda que debes tener todos los archivos guardados en la misma carpeta, la carpeta puede estar almacenada en cualquier lugar que quieras de tu ordenador. Una vez tengas esto listo puedes ejecutar el código [Controller.py](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Controller.py). Si sabes algo de programación notarás que el código está escrito bajo una arquitectura MVC, la verdad decidí hacerlo de esta manera para evitar llamar varias veces las mismas funciones y que estas se ejecuten cada vez que el usuario ingrese algo bajo la interfaz gráfica (UI). Aparte también me pareció un buen ejercicio hacerlo de esta manera. 😃
  
  Una vez ejecutes Controller.py se te debe de aparecer una ventana como esta:
  ![MainWindow](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Figures/Figure_1.JPG)
  
  Si esto te funciona, creo que no debería de darte ningún problema en un futuro.
  
  * #### Explicación De Cada Caso
  Como puedes ver en la interfez, te da las opciones para ver los puntajes de los jugadores, jugar o salir del programa. Una vez que le das click en jugar se te desplegará una nueva ventana semejante a la siguiente:
  ![InitialQuestion](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Figures/Figure_2.JPG)
  
  En ella puedes ver en la parte superior la categoría de la pregunta junto con su nivel de difilcultad. Hay 5  (cinco) categorías, las cuales se componen por **[Matemáticas, Física, Biología, Historia, Contenido inaportante creado por la mente de Mauricio]**, y a su vez cada una de estas tiene otras 5(cinco) preguntas que se clasifican por medio de los niveles de dificultad. Siendo 'Nivel 1' la dificultad más fácil y 'Nivel 5'. Dando como resultado un total de 25 preguntas, si quieres ver como se almacenaron estas preguntas, esto lo puedes ver en el código [Model.py](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Model.py) apartir de la línea 19. Lo quise guardar de esta manera debido a que si dado el caso se deben guardar más preguntas por categoría, se hiciera de una forma rápida y fácil. Aparte en ningún momento la guía de desarrollo de la prueba impone almaenar dicha información de alguna forma específica (ya sea un documento .txt, conectándose a una base de datos local, etc.)
  
  También puedes ver la pregunta a contestar junto con 4 (cuatro) botones que sugiere una de las 4 (cuatro) posibles respuestas. Solo puedes escoger una dado que siempre se cumple que solo una es la correcta. Justo debajo puedes ver la barra de progreso la cual indica el número de puntos ganados durante el test (concurso), tal y como puedes ver en la siguiente imagen:
  ![NotInitialQuestion](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Figures/Figure_3.JPG)
  siendo 0 el mínimo de puntos y 100 el máximo total de puntos que puedes acumular. Dado este caso si llegas a 100 puntos ganarás el test (concurso)
  *  ##### Caso en fallar una pregunta
  Si llegas a contestar una pregunta de forma incorrecta, se te hará una notificación de que has fallado y que tu juego ha terminado. También se te informará que tu puntaje ha sido guardado y el nombre de jugador que se te fue asignado. Un ejemplo lo puedes ver a continuación:
  ![WrongAnswer](https://github.com/MauricioZapata00/PruebaTecnicaSofka/blob/main/Figures/Figure_4.JPG)

