from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PyQt5.uic import loadUi
class MyView(QMainWindow):
	"""docstring for MyView"""
	def __init__(self):
		super(MyView, self).__init__(None)
		loadUi('MainWindow.ui', self)
		self.__setUp()

	def __setUp(self):
		self.BotonConsultarPuntajes.clicked.connect(self.__mostrarPuntajes)
		self.BotonJuegoPredeterminado.clicked.connect(self.__jugarPredeterminado)
		self.BotonSalida.clicked.connect(self.__salir)

	def __mostrarPuntajes(self):
		#print("Se escogió el botón de ver puntajes")
		#print(self.BotonConsultarPuntajes.text())
		#self.BotonConsultarPuntajes.setText("Cambio el texto")
		self.__controladorDeVista.verificarJugadores()
		

	def __jugarPredeterminado(self):
		#print("Se escogió el botón de jugar preestablecido")
		self.__ventanaSecundaria = DefaultView(self.__controladorDeVista)
		self.__controladorDeVista.mostrarJuegoMauricio(self.__ventanaSecundaria)

	def __salir(self):
		print("Se cerró el programa")
		self.__controladorDeVista.cerrarPrograma()


	def establecerControlador(self, c):
		self.__controladorDeVista = c

	def mostrarListaDeJugadores(self):
		self.__ventanaDeJugadores = PlayersView(self.__controladorDeVista)
		self.__controladorDeVista.mostrarJugadores(self.__ventanaDeJugadores)

	def mostrarMensajeJugadores(self):
		mensaje = QMessageBox()
		mensaje.setWindowTitle("Nadie ha jugado todavía")
		mensaje.setText("No hay jugadores almacenados\nPor favor realiza un Test.")
		mensaje.setIcon(QMessageBox.Information)
		mensaje.exec_()

class DefaultView(QMainWindow):
	"""docstring for DefaultView"""
	def __init__(self, controlador):
		super(DefaultView, self).__init__(None)
		loadUi('QuestionsWindow.ui', self)
		self.__controladorVistaPredeterminada = controlador;
		self.__setUp()

	def __setUp(self):
		self.BotonOpcion1.clicked.connect(self.__presionarOpcion1)
		self.BotonOpcion2.clicked.connect(self.__presionarOpcion2)
		self.BotonOpcion3.clicked.connect(self.__presionarOpcion3)
		self.BotonOpcion4.clicked.connect(self.__presionarOpcion4)
		self.BotonRegresar.clicked.connect(self.__presionarRegresar)

	def __presionarOpcion1(self):
		#print("Se presionó la opción 1")
		self.__controladorVistaPredeterminada.verificarRespuesta(0)

	def __presionarOpcion2(self):
		#print("Se presionó la opción 2")
		self.__controladorVistaPredeterminada.verificarRespuesta(1)

	def __presionarOpcion3(self):
		#print("Se presionó la opción 3")
		self.__controladorVistaPredeterminada.verificarRespuesta(2)

	def __presionarOpcion4(self):
		#print("Se presionó la opción 4")
		self.__controladorVistaPredeterminada.verificarRespuesta(3)

	def __presionarRegresar(self):
		print("se regresó a la ventana principal")
		self.__controladorVistaPredeterminada.abandonarTest()

	def mostrarCategoriaYNivel(self, categoria, nivel):
		self.TextoCategoria.setText(categoria + " " + nivel)

	def mostrarPregunta(self, pregunta):
		self.TextoPregunta.setText(pregunta)

	def mostrarRespuestas(self, listaRespuestas):
		self.BotonOpcion1.setText(listaRespuestas[0])
		self.BotonOpcion2.setText(listaRespuestas[1])
		self.BotonOpcion3.setText(listaRespuestas[2])
		self.BotonOpcion4.setText(listaRespuestas[3])

	def mostrarTextoInformativo(self,texto):
		self.TextoInfo.setText(texto)

	def mostrarPuntosActuales(self,puntos):
		self.BarraPuntaje.setValue(puntos)

	def mostrarMensajeAbandono(self, jugador):
		mensaje = QMessageBox()
		mensaje.setWindowTitle("Has abandonado el Test :O")
		mensaje.setText("Acabas de salirte del concurso\nTus puntos obtenidos han sido guardados\nFuiste el " + jugador)
		mensaje.setIcon(QMessageBox.Warning)
		mensaje.exec_()

	def mostrarMensajeExito(self, jugador):
		mensaje = QMessageBox()
		mensaje.setWindowTitle("¡Has Ganado! :D")
		mensaje.setText("Acabas de ganar el concurso\nTus puntos obtenidos han sido guardados\nFuiste el " + jugador)
		mensaje.setIcon(QMessageBox.Information)
		mensaje.exec_()

	def mostrarMensajeFracaso(self, jugador):
		mensaje = QMessageBox()
		mensaje.setWindowTitle("Perdiste :C")
		mensaje.setText("Acabas de perder el concurso\nTus puntos obtenidos han sido guardados\nFuiste el " + jugador)
		mensaje.setIcon(QMessageBox.Critical)
		mensaje.exec_()
		
		
class PlayersView(QMainWindow):
	"""docstring for PlayersView"""
	def __init__(self, controlador):
		super(PlayersView, self).__init__(None)
		loadUi('PlayerWindow.ui', self)
		self.__controladorVistaJugadores = controlador
		self.__setUp()

	def __setUp(self):
		self.BotonRegresar.clicked.connect(self.__presionarRegresar)
		#self.__controladorVistaJugadores.obtenerJugadores()

	def __presionarRegresar(self):
		self.__controladorVistaJugadores.cerrarVentanaJugadores()

	def listarJugadores(self, jugadores, puntajes):
		for i in range(0, len(jugadores)):
			elementoActual = QListWidgetItem(jugadores[i] + "(Puntaje): " + str(puntajes[i]))
			#self.ListaJugadores.insertItem(jugadores[i] + "\t" +str(puntajes[i]))
			self.ListaJugadores.addItem(elementoActual)
		
		