
from django.http import HttpResponse
from django.template import Template, Context
import datetime

#Aca van planchadas las distintas paginas y adornos y etc

class Person(object):
	def __init__(self, Nombre, Apellido):
		self.nombre=Nombre
		self.apellido=Apellido

def  Principal(request):
	MeinMenu = ["Quejas", "Mensajes", "Puntuacion"]
	#Nombre = "Melody"
	#Apellido = "Trilla"
	p1 = Person("Melody", "Trilla")
	Est = datetime.datetime.now()

	DoxOut = open(r"D:/Users/lukym/Desktop/Projects/Dproject/static/home.html")
	plt = Template(DoxOut.read())
	DoxOut.close()

	ctx = Context({"Nombre":p1.nombre, "Apellido":p1.apellido, "Fexa":Est, "Menu":MeinMenu})
	Docc = plt.render(ctx)

	return HttpResponse(Docc)

def Comenter(request):
	return HttpResponse("Caja de comentario con boton de enviar")

#Ejemplo de contenido dinamico
def FexaDoy(request):
	Fexa = datetime.datetime.now()
	return HttpResponse("Fecha y Hora de hoy dia %s" %Fexa)

#Pasar parametro por URL

def Calculef(request, agno = 2019):
	edadACT = 18
	Periodo = agno - 2022
	Edfur = edadACT + Periodo

	return HttpResponse("En el el año %s tendras %s años" %(agno, Edfur))

#El uso de las plantillas
