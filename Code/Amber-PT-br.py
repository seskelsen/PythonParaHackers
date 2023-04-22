# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
import pyttsx3
import subprocess
import urllib
import os
import sys


while True:
    bot = ChatBot('Amber')
    speak = pyttsx3.init('sapi5')

    def Speak(text):
        Speak.say(text)
        Speak.runAndWait()


    SPKint = [
              'Olá' or 'Oi' or 'Opa' or 'Eai' or 'Eae',
              'Olá, como você está?' or 'Você Poderia me Ajudar?',
              'Eu Estou Bem' or 'Está tudo bem por aqui' or 'Eu estou bem, obrigado',
              "Qual o seu nome?" or 'Como você se chama?',
              'Meu nome é Amber' or "Me chamo Amber, qual o seu nome?",
              'O que você pode fazer?' or 'Como pode me ajduar?',
              "Estou aqui para ajudá-lo!"
              ]   

    
    SPKPerson = [
                 'Conte-me mais sobre você?' or 'Quem é você?',
                 "Sou assistente pessoal, sou muito legal!" or "Eu sou um assistente que facilitará sua vida.",
                 'Quem criou você?' or 'Quem desenvolveu você?',
                 'Eu fui desenvolvida por um estudante.',
                 'Quantos anos você tem?' or "Qual a sua idade?",
                 "Eu sou muito jovem, ainda estou em uma fase de desenvolvimento."
                 ]

    
    SPKProgramas = ['Abrir Google','Executando Google', 'Abrir Photoshop','Executando Adobe Photoshop','Abrir vegas','Executando Sony Vegas',
                    'Abrir Skype','Executando Skype','Abrir Brackets'or'Executando brackets','Executando Brackets Developer',
                    'Pesquisar','Pesquisando no Google', 'Pesquisar no Youtube', 'Pesquisando YouTube', 'Maps' or 'Buscar no Maps', 'Buscando no maps'
                    'Abrir agenda' or 'Meus Compromissos', 'Abrindo sua agenda']






    bot.set_trainer(ListTrainer)

    bot.train(SPKint)
    bot.train(SPKPerson)
    bot.train(SPKProgramas)







    #Reconhecimento de Voz
    rec= sr.Recognizer()
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        # ---------------------------

        print('Say Something: ')
        restart=0
        while restart<1:

            try:
                
                speak.setProperty('voice', b'brazil') #Fala Resposta
                audio = rec.listen(s) #Modulo de reconhecimento
                speech = rec.recognize_google(audio,language='pt-BR') # Reconhecimento e translate
                print('Você: ', speech)
                response= bot.get_response(speech) #Captação de resposta através de Speech(FALA)
                speak.say(response) #Entender Resposta Audio Audio
                print ('Amber: ', response) #Resposta escrita
                speak.runAndWait() #Falar Resposta
            except:
                print(end="")
#_________________________________________________________________________________________________________________________________
#Execução de pesquisas no Google
            
            try:    
                if 'pesquisar' or 'Pesquisar' in speech:
                    speech = speech.replace('pesquisar ' or 'Pesquisar ','')
                    speech = speech.replace(' ','+')
                    subprocess.Popen('start http://www.google.com.br/search?q='+speech, shell = True)


                if 'YouTube' in speech:
                    speech = speech.replace('YouTube 'or'youtube'or'Youtube','')
                    speech = speech.replace(' ','+')
                    subprocess.Popen('start  https://www.youtube.com/results?search_query='+speech, shell = True)

                elif 'maps'or'Maps' in speech:
                     speech = speech.replace('maps'or'maps','')
                     speech = speech.replace(' ','+')
                     subprocess.Popen('start https://www.google.com.br/maps/search/'+speech, shell = True) 

                else:
                    print(end="")
                
                    









                 #Execcução de softwares   
             

                    if 'abrir' or 'Abrir' in speech:
                        speech = speech.replace('abrir' or 'Abrir','')
                        if 'Google' in speech:
                            subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', shell = True)
                        elif 'Photoshop' in speech:
                            subprocess.call('C:\Program Files (x86)\Adobe\Adobe Photoshop CS6\Photoshop.exe', shell = True)
                        elif 'Vegas' or 'vegas' in speech:
                            subprocess.call('cd "C:\Program Files\Sony\Vegas Pro 11.0\vegas110.exe"', shell = True)
                        elif 'Skype' or 'skype' in speech:
                            subprocess.call(b'C:\Users\AdSE\Desktop\skype.lnk', shell = True)
                        elif 'Brackets' or 'brackets' in speech:
                            subprocess.call(b'C:\Users\AdSE\Desktop\brackets.lnk', shell = True)
                        elif 'Whatsapp' or 'whatsapp' or 'WhatsApp' in speech:
                            subprocess.Popen('start https://web.whatsapp.com', shell = True)
            except:
                print(end="")


            



                


