import os, sys, time
menuac="menu"
def auto():
	global menuac
	print("In Process .... 	            [ OK ]")
	time.sleep(1.0)
	print("Starting Script ....         [ OK ]")
	time.sleep(1.0)
	os.system("java -jar encoder.jar -l resources/es.properties -i  script.txt -o inject.bin")
	time.sleep(1.0)
	os.system("clear")
	menuac="menu"
def manu():
	global menuac
	menu2="""
	[+] Put the type of Keyboard and the name of the fail wiht the extenxion.
	"""
	print(menu2)
	ak = input("Auto@auto$~> ")
	ak2=ak.split("-")
	print("In Process .... 	            [ OK ]")
	time.sleep(1.0)
	print("Starting Script ....         [ OK ]")
	time.sleep(1.0)
	os.system("java -jar encoder.jar -l resources/"ak2[0]".properties -i  "ak2[1]" -o inject.bin")
	time.sleep(1.0)
	os.system("clear")
	menuac="menu"
def ayuda():
	global menuac
	ayuda1="""
	_______________________________________

	How dose it work?
		-> This program makes it
			unnecessary to remember the
			compilation command of the
			'DuckyScript'.
	_______________________________________

	-> By default the script is assigned
		the 'DuckyScript' called script.txt.
	________________________________________	
	"""
	print(ayuda1)
	print("[1] to go back")
	op=input("Auto@auto$~> ")
	if op == "1":
		menuac="menu"

def menu():
	global menuac
	menu1="""
	[+] Opciones.
	[1] Convert Script Autoatic.
        [2] Convert Script Manual.
        [3] Help.
	[4] Exit.
	"""
	print(menu1)
	op = input("Auto@auto$~> ")
	if op == "1":
		menuac="auto"
	elif op == "2":
		menuac="manu"
	elif op == "3":
		menuac="ayuda"
	elif op == "4":
		sys.exit()

def movimiento():
	try:
		while True:
			if menuac == "menu":
				menu()
			elif menuac == "auto":
				auto()
			elif menuac == "manu":
				manu()
			elif menuac == "ayuda":
				ayuda()
	except KeyboardInterrupt:
if __name__=="__main__":
	movimiento()
