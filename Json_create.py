import json
import os
import platform

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        os.system('cls')
    else:
        os.system('clear')

class The_Architect():

	def __init__ (self,json):
	    self.json=json
	    self.daten= None

	# Schreibt self.daten in die Json Datei
	def write_json(self):
	    with open (self.json,"w") as json_ziel:
        	json.dump(self.daten,json_ziel,indent=4)

	#ein python generator onjekt das if_n zurückgibt
	@staticmethod
	def make_if(n):
		for i in range(n): yield(f"if_{i+1}")

	#Liest die Json Datei aus und setzt self.daten
	def read_json(self):
	    with open (self.json,"r") as jsondata:
        	self.daten=json.load(jsondata)

	def compile_data_j(self,index,text,inp,code,nxt,is_code=None,ifs=None):

	    self.daten[index]={"text": text,
			        "input" : inp,
				"code" :code,
				"next" : nxt,
				}
	    if ifs: self.daten[index]["ifs"]=ifs
	    if is_code: self.daten[index]["is_code"]=is_code

	def translator(self,text):
	    # text=text.replace("__","\n")
	    text=text.replace("ä","\u00e4")
	    text=text.replace("ö","\u00f6")
	    text=text.replace("ü","\u00fc")
	    return text

	#holt die Daten vom user
	def inp(self):

		index=input("Index: ")
		text=input("Text: ")
		inp=input("Input: ")
		try: inp=int(inp)
		except ValueError: inp=False
		
		#text=self.translator(self,text)

		if inp:
			ifs={}
			for i in self.make_if(inp):
				ifs[i]= int(input(i+" "))
			nxt=None

		else:
			nxt=int(input("next: "))
			ifs=None

		code=True if input("Code: ") else False
		is_code=input("is_code: ") if code else None

		self.compile_data_j(index,text,inp,code,nxt,is_code,ifs)

def main():
	creator=The_Architect("Frames.json")
	clean()
	creator.read_json()
	
	while True:
		try: creator.inp()
		except:
			creator.write_json()
			break	
		clean()

if __name__ == "__main__":
    main()
    #print(json.dumps(["äöü"]))
