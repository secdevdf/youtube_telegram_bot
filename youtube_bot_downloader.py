from datetime import datetime
import youtube_dl
import telepot
import csv
import sys
import os

os.system("clear")
bot = telepot.Bot("BOT_TOKEN")

banner = 'Bom dia'
descricao = ' Para utilizar o bot digite /a $url \n exemplo: /a https://youtu.be/wIuBcb2T55Q'
print("[+]===========================================================[+]")
print("                          BOT ONLINE")
print("[+]===========================================================[+]")
try:

    def recebendoMsg(msg):
        logs = open('bot_logs.txt','a')
        logs.write(str(msg))
        logs.close()
        texto = msg["text"]
        cliente = msg["chat"]["first_name"]
        chat_id = msg["chat"]["id"]
        compila = (str(chat_id)+" "+cliente+" "+texto)
        print("[+]------------------------------[+] ")
        print(cliente,texto)
        print("[+]------------------------------[+] ")
        if texto == True or texto in ('/Start', '/start'):
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
            dh = data_e_hora_em_texto.split()
            hora = dh[1]
            if hora <= "12:00":
                banner = 'Bom dia '+cliente+descricao
            elif hora <= "18:00":
                banner = 'Boa tarde '+cliente+descricao
            else:
                banner = 'Boa noite '+cliente+descricao
            bot.sendMessage(chat_id,banner)
            print("[!] ENVIANDO BANNER [!]")

        elif texto == True or texto[0:2] in ('/a', '/a'):
            url2 = texto[3:46]
            print("[ ! ] CLIENT_ID ===> "+str(chat_id)+" [ ! ]")
            #print("[ ! ] CLIENT_USERNAME ===>"+cliente+" [ ! ]")
            print("[ ! ] URL ====> "+url2+" [ ! ]")
            bot.sendMessage(chat_id,"Aguarde alguns instantes, estou baixando para te enviar...")
            video_url = url2
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url,download=False
            )
            filename = f"{video_info['title']}.mp3"
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filename,
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])
            output_file= open(filename,'rb')
            print("[ ! ] sending audio to client [ ! ]")
            bot.sendAudio(chat_id,(filename, output_file))

        else:
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
            dh = data_e_hora_em_texto.split()
            hora = dh[1]
            if hora <= "12:00":
                banner = 'Bom dia '+cliente+descricao
            elif hora <= "18:00":
                banner = 'Boa tarde '+cliente+descricao
            else:
                banner = 'Boa noite '+cliente+descricao
            bot.sendMessage(chat_id,banner)

        print("[+]===========================================================[+]")
        print("                      [!] Recebendo nova mensagem [!]")
        print("[+]===========================================================[+]")

    bot.message_loop(recebendoMsg)
except:
        pass
while True:
    pass
