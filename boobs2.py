import sys
letter = raw_input('letter ')
character = raw_input('character ')
shift = abs(ord(letter) - ord(character))
print(shift)
text = raw_input('text ')
for l in text:
	if((ord(l) > 31) and (ord(l) < 127)):
		if(ord(l) + shift > 127):
			temp = ord(l) + shift - 127
			sys.stdout.write(chr(temp))
		else:
			sys.stdout.write(chr(ord(l) + shift))
	if((ord(l) + shift < 32) or (ord(l) + shift == 127)):
		sys.stdout.write(" ")

print('\n')
