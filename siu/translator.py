#Brandon McCurry
#English/German/French translator
from tkinter import *
class Application(Frame):
	#create the GUI
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		
		self.label = Label(self, text = "Welcome to my translator!")
		self.label.grid(row = 0, column = 0, columnspan = 3)
		
		self.engLbl = Label(self, text = "English: ")
		self.engLbl.grid(row = 1, column = 0)
		self.engTxt = Entry(self)
		self.engTxt.grid(row = 1, column = 1)
		
		self.gerLbl = Label(self, text = "German: ")
		self.gerLbl.grid(row = 2, column = 0)
		self.gerTxt = Entry(self, text = "The")
		self.gerTxt.grid(row = 2, column = 1)
		
		self.freLbl = Label(self, text = "French: ")
		self.freLbl.grid(row = 3, column = 0)
		self.freTxt = Entry(self)
		self.freTxt.grid(row = 3, column = 1)
		
		self.bttn = Button(self, text = "submit", command = self.submit)
		self.bttn.grid(row = 4, column = 0)
		
		self.clear = Button(self, text = "clear", command = self.clear)
		self.clear.grid(row = 4, column = 1,sticky = E)
	#translate the chosen word into the other two languages using two files
	def submit(self):
		#english to german file in text format of (English:German)
		eg = open("engGer.txt")
		#german to french file in text format of (German:French)
		gf = open("gerFre.txt")
		
		gerToEng = {}
		gerToFre = {}
		engToGer = {}
		freToGer = {}
		count = 0
		#turns the string into a dictionary in both directions
		for line in eg:
			eng, ger = line.strip().split(":")
			engToGer[eng] = ger
			gerToEng[ger] = eng
		for lines in gf:
			germ, fren = lines.strip().split(":")
			gerToFre[germ] = fren
			freToGer[fren] = germ
		
		#check if there are multiple entries filled
		if self.engTxt.get() != "":
			count += 1
		if self.gerTxt.get() != "":
			count += 1
		if self.freTxt.get() != "":
			count += 1
			
		if count > 1:
			self.label["text"] = "Please clear all but one entry"
		else:
			self.label["text"] = "Thank you! Try another."
			#translate the word to both other languages
			if self.engTxt.get() != "":
				english = self.engTxt.get()
				if english in engToGer:
					engToGer[english]
					german = engToGer[english]
					self.gerTxt.insert(0, german)
					self.freTxt.insert(0, gerToFre[german])
				else:
					self.label["text"] = "Sorry, we do not know that word."
			elif self.gerTxt.get() != "":
				german = self.gerTxt.get()
				if german in gerToEng:
					english = gerToEng[german]
					self.engTxt.insert(0, english)
					french = gerToFre[german]
					self.freTxt.insert(0, french)
				else:
					self.label["text"] = "Sorry, we do not know that word."
			elif self.freTxt.get() != "":
				french = self.freTxt.get()
				if french in freToGer:
					german = freToGer[french]
					self.gerTxt.insert(0, german)
					english = gerToEng[german]
					self.engTxt.insert(0, english)
				else:
					self.label["text"] = "Sorry, we do not know that word."
	#clear all entries
	def clear(self):
		self.engTxt.delete(0,END)
		self.gerTxt.delete(0,END)
		self.freTxt.delete(0,END)
		
root = Tk()
root.title("Translator")
root.geometry("235x105")
app = Application(root)
root.mainloop()