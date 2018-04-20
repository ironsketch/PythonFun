numbers = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

word = raw_input("Enter in JEEZE!... ")
wordCon = ""
for c in word:
	if(ord(c) > 64 and ord(c) < 91):
		wordCon += numbers[ord(c) - 65]
	elif(ord(c) > 96 and ord(c) < 123):
		wordCon += numbers[ord(c) - 97]

print wordCon
