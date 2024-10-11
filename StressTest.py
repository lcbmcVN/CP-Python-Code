import time, subprocess
from random import randint

NTEST = 100
TIMELIMIT = 1
NAME =  "TASK"
inp = NAME+".inp"
out = NAME+".out"
ans = NAME+".ans"
endl = "\n"

def check(file1, file2):
	with open(file1, 'r') as f1, open(file2, 'r') as f2:
		return f1.read() == f2.read()

for i in range(1, NTEST+1):
	print(f"\033[0;37mCase #{i}\n")
	with open(inp, 'w') as f:
		n = 1000
		f.write(str(n)+endl)
		for _ in range(n):
			f.write(str(randint(1,100000))+ " ")
		f.write(endl)

	begin = time.time()
	subprocess.run(["python", NAME+".py"])
	end = time.time()
	subprocess.run(["python", NAME+"_trau.py"])

	if not check(out,ans):
		print(f"\033[0;31mWA\n---------------\n\033[0;37m")
		break
	else:
		if end-begin <= TIMELIMIT:
			print(f"\033[0;32mAC [{(end - begin):.4f} s]\n---------------\n\033[0;37m")
		else:
			print(f"\033[0;34mTLE\n---------------\n\033[0;37m")
			break
