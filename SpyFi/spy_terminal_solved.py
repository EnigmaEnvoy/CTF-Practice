import string
from pwn import *
from Crypto.Cipher import AES

# len(sitrep) = 11; then flag will be in next block (the 7th block)
# message = """Agent,\nGreetings. My situation report is as follows:\n{0}\nMy agent identifying code is: {1}.\nDown with the Soviets,\n006\n""".format( sitrep, flag )

final_flag = ""

def split_ciphertext(cipher_text): # to split the cipher text received into blocks of 16 bytes each
	cipher_blocks = []
	prev = 0
	for i in range(1, len(cipher_text)+1):
		if (i%32 == 0):
			cipher_blocks.append(cipher_text[prev:i])
			prev = i
	return cipher_blocks

def solve_it():
	global final_flag

	base_text = "a"*(11+16) + "ifying code is: " # {0} must be entered so that each letter of the flag appears after "My agent identifying code is: " in each iteration. We take an extra block (11 + 16 + 16 bytes) because the flag can be bigger than (11 + 16) bytes.
	sitrep = base_text[len(final_flag):] # Send the text to that the exact number of letters from the flag appear in the 8th block.

	conn = remote('2018shell.picoctf.com', '33893')
	print (conn.recvline().decode())

	conn.sendline(sitrep.encode())

	encrypted = conn.recvall()
	encrypted = (encrypted.decode().split('report: '))[1]

	encrypted_blocks = split_ciphertext(encrypted)
	required_ciphertext = encrypted_blocks[7] # Save the 8th block as the required cipher text block.


	for ch in string.printable:
		base_text = "a"*(11+16) + "ifying code is: "
		sitrep = base_text[len(final_flag)+1:] + final_flag + ch # Send the text with one character less and append the flag and the random character.

		conn = remote('2018shell.picoctf.com', '33893')
		print (conn.recvline().decode())

		conn.sendline(sitrep.encode())

		encrypted = conn.recvall()
		encrypted = (encrypted.decode().split('report: '))[1]

		encrypted_blocks = split_ciphertext(encrypted)
		if (encrypted_blocks[5] == required_ciphertext): # Check if the encrypted block is equal to the required cipher text block
			final_flag += ch
			break

for i in range(43): # 43 because we assume flag cannot be bigger than that and (11 + 16 + len("ifying code is: ") = 43)
	print ("="*100)
	solve_it()
	print (final_flag)



