from View import MyView
from Model import MyModel
from PyQt5.QtWidgets import QApplication
import sys
class MyController(object):
	"""docstring for MyController"""
	def __init__(self, v, m):
		self.__vistaDelControlador = v
		self.__modeloDelControlador = m

	def __hacerPregunta(self):
		data = self.__modeloDelControlador.obtenerPregunta()
		self.__ventanaPredeterminada.mostrarCategoriaYNivel(data[0],data[1])
		self.__ventanaPredeterminada.mostrarPregunta(data[2])
		self.__ventanaPredeterminada.mostrarRespuestas(data[3])
		textoInfo = self.__modeloDelControlador.obtenerTextoInformativo()
		self.__ventanaPredeterminada.mostrarTextoInformativo(textoInfo)
		puntos = self.__modeloDelControlador.obtenerPuntosActuales()
		self.__ventanaPredeterminada.mostrarPuntosActuales(puntos)

	def abandonarTest(self):
		jugadorActual = self.__modeloDelControlador.obtenerJugadorActual()
		self.__modeloDelControlador.guardarPuntajeJugador()
		self.__ventanaPredeterminada.mostrarMensajeAbandono(jugadorActual)
		self.cerrarVentadaPredeterminada()

	def cerrarPrograma(self):
		sys.exit()

	def cerrarVentadaPredeterminada(self):
		self.__ventanaPredeterminada.close()

	def cerrarVentanaJugadores(self):
		self.__ventanaJugadores.close()

	def mostrarJuegoMauricio(self, ventana):
		#ventana.show()
		self.__ventanaPredeterminada = ventana
		self.__ventanaPredeterminada.show()
		self.__hacerPregunta()

	def mostrarJugadores(self, ventana):
		#print("Se creo la ventana de jugadores")
		self.__ventanaJugadores = ventana
		self.__ventanaJugadores.show()
		self.obtenerJugadores()

	def obtenerJugadores(self):
		data = self.__modeloDelControlador.obtenerJugadores()
		self.__ventanaJugadores.listarJugadores(data[0],data[1])


	def verificarJugadores(self):
		cantidadJugadores = self.__modeloDelControlador.obtenerNumeroDeJugadores()
		if(cantidadJugadores == 0):
			#print("No hay jugadores registrados")
			self.__vistaDelControlador.mostrarMensajeJugadores()
		else:
			#print("Aquí están los jugadores")
			self.__vistaDelControlador.mostrarListaDeJugadores()

	def verificarRespuesta(self,num):
		band = self.__modeloDelControlador.verVerdadera(num)
		if(band):
			if(self.__modeloDelControlador.obtenerNivelActual()<=5):
				self.__hacerPregunta()
			else:
				#print("¡Has Ganado! :D")
				puntos = self.__modeloDelControlador.obtenerPuntosActuales()
				self.__ventanaPredeterminada.mostrarPuntosActuales(puntos)
				jugadorActual = self.__modeloDelControlador.obtenerJugadorActual()
				self.__modeloDelControlador.guardarPuntajeJugador()
				self.__ventanaPredeterminada.mostrarMensajeExito(jugadorActual)
				self.cerrarVentadaPredeterminada()
		else:
			#print("Perdiste :(")
			jugadorActual = self.__modeloDelControlador.obtenerJugadorActual()
			self.__modeloDelControlador.guardarPuntajeJugador()
			self.__ventanaPredeterminada.mostrarMensajeFracaso(jugadorActual)
			self.cerrarVentadaPredeterminada()



class MyExecutable(object):
	"""docstring for MyExecutable"""
	def __init__(self):
		self.__miApp = QApplication(sys.argv)
		self.__miVista = MyView()
		self.__miModelo = MyModel()
		#self.__miModelo = MyModel()
		self.__miControlador = MyController(self.__miVista, self.__miModelo)
		self.__miVista.establecerControlador(self.__miControlador)
		self.__miModelo.establecerControlador(self.__miControlador)

		self.__main()

	def __main(self):
		self.__miVista.show()
		sys.exit(self.__miApp.exec())

var = MyExecutable()
		
		
