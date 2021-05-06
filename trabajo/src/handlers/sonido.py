import os
from playsound import playsound

def reproducir_sonido(tipo):
	"""
	Reproduce el sonido enviado en tipo

	tipo = 1 ----> sonido click.wav

	"""
	if tipo == 1:
		sonido_boton = os.path.join('src','recursos', 'sonidos', 'click.wav')
	else:
		return

	try:
		playsound(sonido_boton)
	except:
		pass
