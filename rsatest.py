
##RSA crypto function for DM 




def RSAconvert(string,n,e):

	#This part Michelle wrote. It converts the String into numbers

	numbers = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
	word = string
	wordCon = ""
	for c in word:
	    if(ord(c) > 64 and ord(c) < 91):
	        wordCon += numbers[ord(c) - 65] 
	    elif(ord(c) > 96 and ord(c) < 123):
	        wordCon += numbers[ord(c) - 97] 

#So if the string is "ATTACK" this will make wordcon = 001919000210

# This next part will do the RSA encryption of the string

#We will split the word into 3 groups of 4 numbers. This will only work for 6 letter words I can think about how to impliment any length later

	one = int(wordCon[0:4])
	two = int(wordCon[4:8])
	three = int(wordCon[9:12])

#So we will take each of these groups of 4 numbers and encrypt them with the RSA schema from the book

	print one, "-", two, "-", three
	return ((one**e)%n),((two**e)%n),((three**e%n))




print RSAconvert("ATTACK",(43*59),13)
print RSAconvert("UPLOAD",(53*61),17)



# Sample output
# 19 - 1900 - 210
# (2299, 1317L, 2117L)
# 2015 - 1114 - 3
# (2545L, 2757L, 1211)
