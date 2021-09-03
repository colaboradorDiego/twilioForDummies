# twilioForDummies
Using Twilio for messagien with python

# Project Imports
 pip install twilio
 pip install flask
 


WhatsApp Bot using Twilio and Python (Part-1) | Setting up Twilio Sandbox for WhatsApp
	https://www.youtube.com/watch?v=BKK5NMDC0fk&t=514s
	
Para utilizar las funciones programables de whatsAPP hay que comprar whatsAPP for Bussines. El punto es que lo mas simple y rapido no es hacerlo directamente con whatsAPP (4/8/21 ya que tardan mucho tiempo en aprobar el request) sino mediante un intermediario, en este caso lo vamos a hacer con Twilio.

Flujo de conversacion convencional ->  1:15

Flujo de conversacion con whatsAPP API	-> 2:54
	debemos configurar a la cuenta de whatsAPP bussines con un callback (url) para derivar el msg al servidor de aplicaciones.
	De tal forma para cuando lleguen los msg del cliente los mande a dicho servisor para procesarlos
	
Flujo de conversacion con Twilio whatsAPP API -> 5:24


Como configurar un sanBox en Twilio -> 9:39

	Creo un nuevo proyecto en twilio para whatsAPP con python siguiento una guia
	
	
	To send messages with WhatsApp in production, WhatsApp has to formally approve your account. But, that doesn't mean you have to wait to start building. Twilio Sandbox for WhatsApp lets you test your app in a developer environment.
	
	
Configurar el sanBox -> 14:00

Flask app to respond to whatsAPP messages
	https://www.youtube.com/watch?v=EeUdel2AJ5g
	
	ahora vienen una serie de pasos que ya sabemos y manejamos como:
		python simplebot.py
		https://ngrok.com/ -> ngrok http 5000
	

	configamos la url call en Twilio account.
		Messagin -> Settings -> WhatsApp sanBox settings
		
		WHEN A MESSAGE COMES IN make http post to: http://90aa1c6a675f.ngrok.io/wasap
			originalmente estaba esta: https://timberwolf-mastiff-9776.twil.io/demo-reply
	
Deploying Flask App on Heroku
	https://www.youtube.com/watch?v=4ho21Wppf30
	
