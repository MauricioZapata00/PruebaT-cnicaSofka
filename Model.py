import random

class MyModel(object):
	"""docstring for MyModel"""
	def __init__(self):
		#self.__banderaCrearTest = False
		#self.__preguntasUsuario = {}
		self.__contadorJugadores = 1
		self.__nivelPreguntaActual = 1
		self.__puntosActuales = 0
		self.__setUp()
		self.__listaCategorias = list(self.__preguntasMauricio.keys())
		self.__participantes = {}

	def __setUp(self):
		self.__definirPreguntasMauricio()

	def __definirPreguntasMauricio(self):
		self.__preguntasMauricio = {
				"Matemáticas":{
					"Nivel 1":{
						"Preguntas":{
							1:{"¿Cuánto es 2 + 2?":
								[["Indefinido","10","Infinito","4"],[False,False,False,True]]

							}
						}

					},
					"Nivel 2":{
						"Preguntas":{
							1:{"Despeja la X en la siguiente ecuación: 3X + 14 = 41.":
								[["Indefinido","9","7.3","Pi"],[False,True,False,False]]

							}
						}
					},
					"Nivel 3":{
						"Preguntas":{
							1:{"¿Cuál de las siguientes funciones satisface que f(x) = f'(x) = Int(f(x))? Siendo Int() la operación de integregración.":
								[["X^2","Sec(x)","1/sqrt((X^2)-4)","e^x"],[False,False,False,True]]

							}
						}
					},
					"Nivel 4":{
						"Preguntas":{
							1:{"Sea F(x,y,z) una función de campo conservativo C^1. Selecciona la propiedad que sea falsa.":
								[["Div(F(x,y,z)) = Cte","Rot(F(x,y,z)) = 0","F(x,y,z) es gradiente de alguna otra función f(x,y,z)",
								"Para cualquier curva cerrada simple, su integral de línea es 0"],[True,False,False,False]]

							}
						}
					},
					"Nivel 5":{
						"Preguntas":{
							1:{"¿Se puede relacionar el número Pi con el número Euler 'e'?":
								[["Imposible","Únicamente para variables probabilísticas","Sí, combinando una serie infinita y una fracción continua generalizada.",
								"Solamente en relaciones circulares de ciertos eventos naturales."],[False,False,True,False]]

							}
						}
					}
				},
				"Historia":{
						"Nivel 1":{
							"Preguntas":{
								1:{"¿Cuándo sucedieron los eventos de la saga de Star Wars de George Lucas?":
									[["Los eventos nunca sucedieron.","Hace mucho tiempo, en una galaxia muy muy lejana...",
									"En el 2552 D.C.","Acabando la década de 1970 D.C."],[False,True,False,False]]

								}
							}

						},
						"Nivel 2":{
							"Preguntas":{
								1:{"Uno de los siguientes héroes no participó en la guerra de troya narrada en la iliada atribuída tradicionalmente a Homero. Selecciona el correcto.":
									[["Kratos, General de esparta.","Agamenón","Aquiles","Héctor"],[True,False,False,False]]

								}
							}
						},
						"Nivel 3":{
							"Preguntas":{
								1:{"¿Qué lograron demostrar Watson y Crick en 1953?":
									[["Que el agua moja.","Que la relatividad se relaciona con la física cuántica.",
									"Que el humano podría volar usando el principio de sustentación.","El genoma humano se compone por una estructura de doble hélice."],
									[False,False,False,True]]

								}
							}
						},
						"Nivel 4":{
							"Preguntas":{
								1:{"¿Cuál era la enfermedad que padecía el único hijo varón del Zar Nicolas II?":
									[["Tifoidea","SIDA","Hemofilia","Mal de amores"],[False,False,True,False]]

								}
							}
						},
						"Nivel 5":{
							"Preguntas":{
								1:{"¿Quién de los siguientes es uno de los héroes del país de Gabón?":
									[["Jean Michonet","Saud Jonsafa","Haaziq Quowtomboke","John James Rambo"],[True,False,False,False]]

								}
							}
						}
					},
					"Biología":{
						"Nivel 1":{
							"Preguntas":{
								1:{"Una de las siguientes no es una bacteria conocida. Selecciona la correcta":
									[["Escherichia coli","Especto Patronum","Staphylococcus aureus","Helicobacter pylori"],
									[False,True,False,False]]

								}
							}

						},
						"Nivel 2":{
							"Preguntas":{
								1:{"¿Cómo vienen asociados los cromosomas del ser humano?":
									[["Cogiditos de la mano.","Asociadas con cadenas nitriladas.","Vienen en células diploide (2n).","Vienen en células monoploide"],
									[False,False,True,False]]

								}
							}
						},
						"Nivel 3":{
							"Preguntas":{
								1:{"¿Qué es una célula procariota?":
									[["Una célula con problemas de su progenie","Una célula que viene de la procarie.","Es una célula cualquiera.",
									"Es una célula con el material genético disperso en el citoplasma."],
									[False,False,False,True]]

								}
							}
						},
						"Nivel 4":{
							"Preguntas":{
								1:{"Solo uno de los siguientes hace parte de los aminoácidos esenciales":
									[["Albúmina","Fenilalanina","Chicharronina","Niacina"],[False,True,False,False]]

								}
							}
						},
						"Nivel 5":{
							"Preguntas":{
								1:{"¿Cuál de los siguientes no es un producto del ciclo de Krebs?":
									[["Ciclopentanoperhidrofenantreno","alfa-cetoglutarato","Fumarato","Succinil-CoA"],[True,False,False,False]]

								}
							}
						}
					},
					"Física":{
						"Nivel 1":{
							"Preguntas":{
								1:{"¿Qué dimensiones (no unidades en el S.I) posee la velocidad?":
									[["m/s","[Masa]/[Longitud]^3","[Longitud]/[Tiempo]^2","[Longitud]/[Tiempo]"],
									[False,False,False,True]]

								}
							}

						},
						"Nivel 2":{
							"Preguntas":{
								1:{"¿Cuál es la tercera ley de Newton?":
									[["A cualquier acción surge una reacción de misma magnitud y sentido contrario.","La derivada direccional del momentum es igual a la fuerza.",
									"Dos de agua por una de arroz.","El calor siempre sale del sistema."],
									[True,False,False,False]]

								}
							}
						},
						"Nivel 3":{
							"Preguntas":{
								1:{"¿Qué pasa si la carga neta encerrada por una gaussiana es cero?":
									[["Surgen problemas de contorno en las cargas.","Las cargas permanecen estables.","Yamcha muere.",
									"Para condiciones estacionarias, el campo eléctrico es cero."],
									[False,False,False,True]]

								}
							}
						},
						"Nivel 4":{
							"Preguntas":{
								1:{"Según la física, ¿La luz es una onda o una partícula?":
									[["Ninguna de las dos.","Es ambas al mismo tiempo.","Es intrínsicamente una partícula.","Es toda poderosa."],
									[False,True,False,False]]

								}
							}
						},
						"Nivel 5":{
							"Preguntas":{
								1:{"Según la ley de Fourier ¿Cómo se transporta el calor en una placa plana?":
									[["De forma lineal","Por medio del Calomovil","De forma constante.","Como ondas que varian según la posición y el tiempo."],
									[False,False,False,True]]

								}
							}
						}
					},
					"Contenido inaportante creado por la mente de Mauricio":{
						"Nivel 1":{
							"Preguntas":{
								1:{"¿Quién es Ezio Auditore?":
									[["El creador del atún con pan.","Es un personaje ficticio de la saga de juegos de Assassins Creed.",
									"Al que le dicen dizque el peinadito.","Un italiano colega de los fundadores de Sofka"],
									[False,True,False,False]]

								}
							}

						},
						"Nivel 2":{
							"Preguntas":{
								1:{"¿Cuál es el nombre del personaje idéntico a Homero Simpson, el cual fue vetado de la taberna de Moe? Aparece en el episodio 'Miedo a volar'-Cap 11,Temporada 6":
									[["Juan Bautista Junior Sabadú","Mario Neta",
									"Cosme Fulanito","Holipopó Velásquez"],
									[False,False,True,False]]

								}
							}
						},
						"Nivel 3":{
							"Preguntas":{
								1:{"¿Qué pasa si la fuerza imparable choca con el objeto inamovible?":
									[["Nace un gato siames.","El objeto para a la fuerza.","Ambos ceden.",
									"La fuerza vence al objeto."],
									[False,False,True,False]]

								}
							}
						},
						"Nivel 4":{
							"Preguntas":{
								1:{"¿Qué se celebra el 15 de Marzo?":
									[["El día del hombre.","El día de Denzel Crocker.","El año nuevo chino.","El terremoto ocurrido en Japón en 2011."],
									[False,True,False,False]]

								}
							}
						},
						"Nivel 5":{
							"Preguntas":{
								1:{"¿Por qué la iguana tomaba café a la hora del té?":
									[["Porque no tenía té.","Porque no tenía reloj.",
									"Lo que pasa es que la iguana es rebelde.","Porque sino llega Luny Tunes & Noriega"],
									[False,True,False,False]]

								}
							}
						}
					}
				}


	def establecerControlador(self, c):
		self.__controladorDeModelo = c

	def guardarPuntajeJugador(self):
		self.__participantes["Jugador " + str(self.__contadorJugadores)] = self.__puntosActuales
		#print(self.__participantes)
		self.__puntosActuales = 0
		self.__contadorJugadores += 1
		self.__nivelPreguntaActual = 1

	def obtenerJugadores(self):
		jugadores = list(self.__participantes.keys())
		puntajes = list(self.__participantes.values())
		return([jugadores, puntajes])

	def obtenerJugadorActual(self):
		return("Jugador " + str(self.__contadorJugadores))

	def obtenerPregunta(self):
		self.__categoriaEscogida = random.choice(self.__listaCategorias)
		self.__preguntaEscogida = list(self.__preguntasMauricio[self.__categoriaEscogida]["Nivel " + str(self.__nivelPreguntaActual)]
			["Preguntas"][1].keys())[0]
		self.__listaObtenida = list(self.__preguntasMauricio[self.__categoriaEscogida]["Nivel " + str(self.__nivelPreguntaActual)]
			["Preguntas"][1].values())[0]
		self.__respuestas = self.__listaObtenida[0]
		self.__verdades = self.__listaObtenida[1]
		return([self.__categoriaEscogida, "Nivel " + str(self.__nivelPreguntaActual), self.__preguntaEscogida, self.__respuestas])

	def obtenerNivelActual(self):
		return(self.__nivelPreguntaActual)

	def obtenerNumeroDeJugadores(self):
		return(len(self.__participantes))

	def obtenerPuntosActuales(self):
		return(self.__puntosActuales)

	def obtenerTextoInformativo(self):
		if(self.__nivelPreguntaActual == 1):
			return("¡Muy bien! Acabas de empezar el juego, intenta pasar esta pregunta. Recuerda que recibes 20 puntos por pregunta respondida correctamente.")
		elif(self.__nivelPreguntaActual == 2):
			return("¡Bien hecho! Sigue probando tu conocimiento.")
		elif(self.__nivelPreguntaActual == 3):
			return("¡Excelente! Vamos por la otra.")
		elif(self.__nivelPreguntaActual == 4):
			return("Está bien. Creo que vuelas en conocimiento, prueba esta otra")
		elif(self.__nivelPreguntaActual == 5):
			return("Estás a punto de lograrlo. Una pregunta correcta demás y ganarás la competencia. ¡Buena suerte!")


	def verVerdadera(self,indice):
		if((self.__verdades.index(True)) == indice):
			self.__nivelPreguntaActual += 1
			self.__puntosActuales += 20
			return True
		else:
			#self.__contadorJugadores += 1
			return False


		

		
		