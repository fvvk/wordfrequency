from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import codecs
import re
import string

def callback():
	    counter("Starten")
	
class MyFrame(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.master.title("Worthäufigkeit")
		self.master.rowconfigure(5, weight=1)
		self.master.columnconfigure(5, weight=1)
		self.grid(sticky=W)

		self.button1 = Button(self, text="Datei auswählen", command=self.load_file, width=15)
		self.button1.grid(row=1, column=0, sticky=W)

		self.button_submit = Button(self, text="Start", command=callback, width=15)
		self.button_submit.grid(row=3, column=0, sticky=W)
		
	def load_file(self):
		filename = askopenfilename(filetypes=(("Text files", "*.txt"),("HTML files", "*.html")))
		
		if filename:
			file = codecs.open(filename, 'r', 'utf-8')
			text = file.read().lower()
			word_list = re.findall(r'\b[a-zöäü]{4,20}\b', text)
			word_freq = {}
			ignore = {''}
			words = input
			return words


	def counter(word):
			for word in wordlist:
				if word not in ignore:
					word_freq[word] = word_freq.get(word, 0) + 1
			
			result = sorted(word_freq.items(), key = lambda x:x[1], reverse = True)
			
			f = open ('output.txt', 'w')
			for word, freq in result:
				f.write("%-20s %d\n" % (word, freq))
			f.close()
			
if __name__ == "__main__":
	MyFrame().mainloop()