#chat de inteligencia artificial con Python
from rivescript import RiveScript

bot = RiveScript()
bot.load_file('datos.rive')
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot> ' + str(reply))

'''
    desde rivescript importa RiveScript
    bot <- RiveScript()
    bot.Leer_Archivo(archivo)
    bot.OrdenarPregunta()

    Mientras sea verdadero:
        Si mensaje es igual a '/quit'
            Salir()
        reply <- bot.CompararDatos('BaseDatos',mensaje)
        Imprime 'Bot' + reply

'''