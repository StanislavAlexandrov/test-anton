import tkinter as tk
from PIL import ImageTk

import requests

bgColor = "#FFF0F5"

parent = tk.Tk()
parent.eval("tk::PlaceWindow . center")
parent.title("Anton Telegram Tkinter")

frame1 = tk.Frame(parent, width=600, height=600, bg=bgColor)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)  # !

# Image Widget
my_image = ImageTk.PhotoImage(
    file="/Users/stanislavalexandrov/projects/clever.png", width=600, height=600)
myWidget = tk.Label(frame1, image=my_image)
myWidget.image = my_image
myWidget.pack()

# Text Label
my_label = tk.Label(parent, text="Hello", font=("Arial Bold", 70), bg=bgColor)
my_label.grid(column=0, row=0)

# Input Label functionality to be implemented
my_input_text = tk.Entry(frame1, text="some input here", bg=bgColor)
my_input_text.pack()


def telegram_bot_sendtext(bot_message):

    bot_token = 'BOT_TOKEN_HERE'
    bot_chatID = 'CHAT_ID_HERE'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    # try:
    #     response = requests.get(send_text)
    # except:
    #     print("an error occured while sending message")
    response = requests.get(send_text)
    return response.json()


my_button = tk.Button(frame1, text="send text to telegram", command=lambda: telegram_bot_sendtext("hello"),
                      bg=bgColor)


my_button.pack()


parent.mainloop()
