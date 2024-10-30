import time, subprocess, sys
from random import randint

NTEST = 5
TIMELIMIT = 1
NAME = "task"
inp = NAME + ".inp"
out = NAME + ".out"
ans = NAME + ".ans"
endl = "\n"

def check(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

def runscript(script_name, timeout):
	try:
		begin = time.time()
		subprocess.run(["python", script_name], timeout=timeout)
		end = time.time()
		return True, end-begin  # Successfully ran within timeout
	except subprocess.TimeoutExpired:
		return False, None  # Timed out

for i in range(1, NTEST + 1):
	# Generate test input
	with open(inp, 'w') as f:
		n = randint(1, int(1e5))
		m = randint(1, 1000)
		f.write(f"{n} {m}{endl}")
		for _ in range(n):
			f.write(str(randint(1, m)) + ' ') 

	temp, t = runscript(NAME+".py", TIMELIMIT)
	if not temp:
		print(f"\033[0;37mCase #{i}\n\033[0;34m TLE\n---------------\n\033[0;37m")
		continue
	runscript(NAME+"_trau.py",None)

    # Check outputs
	if check(out, ans):
		print(f"\033[0;37mCase #{i}\n\033[0;32m AC [{(t):.4f} s]\n---------------\n\033[0;37m")
	else:
		print(f"\033[0;37mCase #{i}\n\033[0;31m WA\n---------------\n\033[0;37m")
		break
