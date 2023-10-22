import time
import smtplib 
from email.message import EmailMessage 
print (""" 
 ____          _  _      __  __         _  _
|  _ \        | || |    |  \/  |       (_)| |
| |_) | _   _ | || | __ | \  / |  __ _  _ | |
|  _ < | | | || || |/ / | |\/| | / _` || || |
| |_) || |_| || ||   <  | |  | || (_| || || |
|____/  \__,_||_||_|\_\ |_|  |_| \__,_||_||_|
by abelatoxz 
 """)
seleccion = int(input("""
Que quieres hacer?
0 = salir del programa
1 = prueba de envio
2 = enviar ataque en massa

Selecion: """))

if seleccion == 0: 
        print ("Hasta pronto")




if seleccion == 1:
    sender_email_address = str(input("Dime el correo con el cual quieres enviar el mensaje: ")) 
    email_password = str(input("Dame la password sin espacios: ")) 
    receiver_email_address = str(input("Dime a quien quieres enviar el ataque: ")) 

    email_subject = str(input("Dame el tema del mensaje: ")) 
    mensaje = str(input("Dame el mensaje que quieres poner: "))
    email_smtp = "smtp.gmail.com" 








    # Create an email message object 
    message = EmailMessage() 

    # Configure email headers 
    message['Subject'] = email_subject 
    message['From'] = sender_email_address 
    message['To'] = receiver_email_address 

    # Set email body text 
    message.set_content(mensaje) 

    # Set smtp server and port 
    server = smtplib.SMTP(email_smtp, '587') 

    # Identify this client to the SMTP server 
    server.ehlo() 

    # Secure the SMTP connection 
    server.starttls() 

    # Login to email account 

    server.login(sender_email_address, email_password) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()
    print("enviado")


if seleccion == 2:

    sender_email_address = str(input("Dime el correo con el cual quieres enviar el mensaje: ")) 
    email_password = str(input("Dame la password sin espacios: ")) 
    receiver_email_address = str(input("Dime a quien quieres enviar el atauqe: ")) 

    email_subject = str(input("Dame el tema del mensaje: ")) 
    mensaje = str(input("Dame el mensaje que quieres poner: "))
    email_smtp = "smtp.gmail.com" 
    mensajes_enviados = int(input("Cuantos mensajes quieres enviar: "))
    contador = 0
    tiempo = int(input("Dime cuanto tiempo de lapso quieres dejar entre mensajes,el problema que google no te deja enviar demasiados mensajes seguidos entonces para evitar el problema colocamos un lapo de tiempo:"))

    while contador != mensajes_enviados:


        contador += 1


        # Create an email message object 
        message = EmailMessage() 

        # Configure email headers 
        message['Subject'] = email_subject 
        message['From'] = sender_email_address 
        message['To'] = receiver_email_address 

        # Set email body text 
        message.set_content(mensaje) 

        # Set smtp server and port 
        server = smtplib.SMTP(email_smtp, '587') 

        server.ehlo() 
        # Identify this client to the SMTP server 

        # Secure the SMTP connection 
        server.starttls() 

        # Login to email account 
        server.login(sender_email_address, email_password) 

        # Send email 
        server.send_message(message) 

        # Close connection to server 
        server.quit()
        print("\rMensajes enviados: ",contador)
        time.sleep (tiempo)


