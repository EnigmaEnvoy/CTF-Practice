# LogCaesar (ReplyCTF - Practice)
  
> The satellite communications have stopped working – suddenly they're sending back unknown algorithms. Help R-boy decipher them.  
> Another file - [encrypt.py](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/LogCaesar/encrypt.py) is also provided along with the [encrypted text](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/LogCaesar/encrypted.txt).
  
  
As we can see in the given file, the plaintext is 256 bytes long and all the characters are shuffled according to a key. 
We consider all keys from 0 to 255 and reverse the decrypt function as shown in [decrypt.py](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/LogCaesar/decrypt.py).  
  
  
### Flag
`{FLG:but_1_th0ught_Dlog_wa5_h4rd}`
