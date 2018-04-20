letter = raw_input('letter ')
character = raw_input('character ')
shift = abs(ord(letter) - ord(character))
print(shift)
text = raw_input('text ')
for l in text:
	if(ord(l) + shift > 127):
		temp = ord(l) + shift - 127
		print chr(temp),
	else:
		print chr(ord(l) + shift),
	
