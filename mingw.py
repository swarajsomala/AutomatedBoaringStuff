import subprocess
#try:
print("compiling")
#subprocess.call(["gcc","hello.c","2",">","compile.txt"])
status = subprocess.call("gcc hello.c 2>compile.txt", shell = True)
	if not status:
		print("running")
		tmp=subprocess.call("output.txt")
#except Exception as e: 
#	print(type(e).__name__ )
