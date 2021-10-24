import random
from tkinter import *

class DiceRoller(object):

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.label = Label(master, font=("times", 200))
		button = Button(master, text="Rolar dados", command=self.roll)
		button.place(x=200, y=0)

	def roll(self):
		symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
		self.label.config(text=f"{random.choice(symbols)}{random.choice(symbols)}")
		self.label.pack()

if __name__ == "__main__":
	root = Tk()
	root.title("Jogo de Dados")
	root.geometry("500x300")
	DiceRoller(root)
	root.mainloop()