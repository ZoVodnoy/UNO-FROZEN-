from math import log2

def DecToBin(n):
	binary = []
	while n > 0:
		binary.append(n%2)
		n = n // 2
	return binary[::-1]

def BinToDec(binary):
	number = 0
	for n, i in enumerate(binary[::-1]):
		if i:
			number += 2 ** n
	return number 

n = 14

print(DecToBin(n))
print(BinToDec(DecToBin(n)))