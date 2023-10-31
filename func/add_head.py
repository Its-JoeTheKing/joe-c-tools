import os

lib = '#include "printf.h"'

def add_libft(file, library):
	fi = open(file, "r")
	lista = fi.readlines()
	if '#include "libft.h"' not in lista[0]:
		lista.reverse()
		lista.append(library+ "\n\n")
		lista.reverse()
		fil = open(file, "w")
		for line in lista:
			fil.write(line)
		fil.close()

print("proccess started ...")
os.system("ls *.c | tr -d ' ' > scripts.txt")
scripts = open("scripts.txt", "r").readlines()

for file in scripts:
	add_libft(file.strip(), lib)

open("scripts.txt", "r").close()
os.system("rm scripts.txt")
