import os

def get_proto(file):
	name = file.split(".c")[0]
	lines = open(file, "r").readlines()
	for line in lines:
		if name in line:
			return line.strip()+";\n"
print("proccess started ...")
os.system("ls *.c | tr -d ' ' > scripts.txt")
scripts = open("scripts.txt", "r").readlines()
save = open("prototypes.txt", "a")
for script in scripts:
	res = get_proto(script.strip())
	if res:
		save.write(res)
os.system("rm scripts.txt")
print("saved in prototypes.txt")
