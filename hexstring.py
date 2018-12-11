#hexstring.py jaden
def bincon(decimal):
	print(decimal)
	print("BIN ********")
	binstr = "" # binstr is a string
	for i in range (8):
		bin = decimal % 2
		decimal = decimal // 2
		#print(bin)
		binstr = binstr + str(bin)
		#print(binstr)
	print("-----")
	print(binstr[::-1]) 

def hexcon(decimal):
	print(decimal)
	print(" HEX ********")
	# divident/divisor=quotient
	hexstr = ""
	# ---------------------------------
	remainder = decimal % 16
	if (remainder == 10):
		remainder = "A" 
	elif (remainder == 11):
		remainder = "B" 
	elif (remainder == 12):
		remainder = "C" 
	elif (remainder == 13):
		remainder = "D" 
	elif (remainder == 14):
		remainder = "E" 
	elif (remainder == 15):
		remainder = "F" 
	# ---------------------------------
	quotient = decimal // 16
	if (quatiant == 10):
		quotient = "A"
	elif (quotient == 2):
		quotient = "B"
