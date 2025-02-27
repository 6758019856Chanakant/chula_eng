#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "ก - Gor Gai"), ("ข", "ข - Khor Khai"), ("ฃ", "ฃ - Khor Khuat"),
    ("ค", "ค - Khor Khwai"), ("ฅ", "ฅ - Khor Khon"), ("ฆ", "ฆ - Khor Rakhang"),
    ("ง", "ง - Ngor Ngu"), ("จ", "จ - Jor Jaan"), ("ฉ", "ฉ - Chor Ching"),
    ("ช", "ช - Chor Chang"), ("ซ", "ซ - Sor So"), ("ฌ", "ฌ - Chor Cher"),
    ("ญ", "ญ - Yor Ying"), ("ฎ", "ฎ - Dor Chada"), ("ฏ", "ฏ - Tor Patak"),
    ("ฐ", "ฐ - Thor Thaan"), ("ฑ", "ฑ - Thor Montho"), ("ฒ", "ฒ - Thor Phuthao"),
    ("ณ", "ณ - Nor Nen"), ("ด", "ด - Dor Dek"), ("ต", "ต - Tor Tao"),
    ("ถ", "ถ - Thor Thung"), ("ท", "ท - Thor Thahan"), ("ธ", "ธ - Thor Thong"),
    ("น", "น - Nor Nu"), ("บ", "บ - Bor Baimai"), ("ป", "ป - Por Pla"),
    ("ผ", "ผ - Phor Phung"), ("ฝ", "ฝ - For Fa"), ("พ", "พ - Phor Phan"),
    ("ฟ", "ฟ - For Fun"), ("ภ", "ภ - Phor Samphao"), ("ม", "ม - Mor Ma"),
    ("ย", "ย - Yor Yak"), ("ร", "ร - Ror Rua"), ("ล", "ล - Lor Ling"),
    ("ว", "ว - Wor Waen"), ("ศ", "ศ - Sor Sala"), ("ษ", "ษ - Sor Ruesi"),
    ("ส", "ส - Sor Suea"), ("ห", "ห - Hor Hip"), ("ฬ", "ฬ - Lor Chula"),
    ("อ", "อ - Or Ang"), ("ฮ", "ฮ - Hor Nokhuk")
]

def next_card():
    global current_card
    current_card = random.choice(thai_consonants)
    canvas.itemconfig(card_text, text=current_card[0])
    canvas.itemconfig(card_label, text="Thai Consonant")

def flip_card():
    canvas.itemconfig(card_text, text=current_card[1])
    canvas.itemconfig(card_label, text="Pronunciation")

# Create the main window
root = tk.Tk()
root.title("Thai Consonant Flashcards")
root.config(padx=50, pady=50, bg="#BDE0FE")

# Create a canvas for the flashcard
canvas = tk.Canvas(width=400, height=250, bg="white", highlightthickness=0)
card_label = canvas.create_text(200, 50, text="Thai Consonant", font=("Arial", 20, "italic"))
card_text = canvas.create_text(200, 125, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
flip_button = tk.Button(root, text="Flip", command=flip_card, font=("Arial", 14))
flip_button.grid(row=1, column=0, pady=20)

next_button = tk.Button(root, text="Next", command=next_card, font=("Arial", 14))
next_button.grid(row=1, column=1, pady=20)

# Start the game
next_card()

# Run the application
root.mainloop()

