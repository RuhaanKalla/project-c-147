# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:30:35 2022

@author: dell
"""

from tkinter import*
root = Tk()
root.title("ASCII Encrypted Code")
root.geometry("400x400")
root.configure(background = "pink")

text_input_word = Entry(root)
text_input_word.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
label_ascii = Label(root,text = "Name in ASCII : " , bg = "yellow" , fg = "red")
label_ascii.place(relx = 0.5 , rely = 0.6,anchor = CENTER)
label_encrypted = Label(root,text = "Encrypted value : " , bg = "yellow" , fg = "red")
label_encrypted.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

def ascii_to_encrypted():
    name_input = text_input_word.get()
    label_ascii["text"] = "Name in ASCII : "
    
    for letter in name_input:
          label_ascii["text"] += str(ord(letter)) + " "
          num_ascii = int(ord(letter))
          encryption_num = num_ascii - 1
          encryption_value = str(chr(encryption_num)) + " "
          label_encrypted["text"] += encryption_value
          

btn = Button(root,text = "Display the ASCII Code in Encrypted Value",bg = "blue" , fg = "yellow" , command = ascii_to_encrypted)
btn.place(relx = 0.5 , rely = 0.5,anchor = CENTER)

root.mainloop()
