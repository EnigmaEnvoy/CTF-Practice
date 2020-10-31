import chardet

def decrypt(message, key):
	plaintext = list(' '*256)
	for i in range(0, 256):
		new_pos = (3**(key+i)) % 257
		plaintext[i] = (message[new_pos-1]^(new_pos-1))^i
	return bytes(plaintext)

with open('encrypted.txt', 'rb') as content_file:
	content = content_file.read()
	print (content)
	with open('decrypted.txt','wb') as decrypted_file:
		for key in range(256):
			decrypted = decrypt(content, key)
			if (bytes('FLG'.encode('ascii')) in decrypted):
				print (decrypted)
