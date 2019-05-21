import os, sys, time
menuac="menu"
def auto():
	global menuac
	print("In process...[ok]")
	time.sleep(1.0)
	print("Starting Script...[ok]")
	time.sleep(1.0)
	os.system("java -jar encoder.jar -l resources/es.properties -i  script.txt -o inject.bin")
	os.system("clear")
	menuac="menu"
def manu():
	global menuac
	menu2="""
	[+] Coloque el tipo de teclado y el nombre del archivo y extenxion.
	"""
	print(menu2)
	ak = input("Auto@auto$~> ")
	ak2.split("-")
	print("In process...[ok]")
	time.sleep(1.0)
	print("Starting Script...[ok]")
	time.sleep(1.0)
	os.system("java -jar encoder.jar -l resources/"ak2[0]".properties -i  "ak2[1]" -o inject.bin")
	os.system("clear")
	menuac="menu"
def ayuda():
	global menuac
	ayuda1=""""""
	print(ayuda1)

def menu():
	global menuac
	menu1="""
	[+] Opciones.
	[1] Convertir Script Autoatico.
	[2]	Convertir Script Manual.
	[3]	Ayuda.
	[4] Salir.
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