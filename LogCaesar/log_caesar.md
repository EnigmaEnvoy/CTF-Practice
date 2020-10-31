# LogCaesar (ReplyCTF - Practice)
  
> The satellite communications have stopped working – suddenly they're sending back unknown algorithms. Help R-boy decipher them.  
> Another file - encrypt.py is also provided
  
  
As we can see in the given file, the plaintext is 256 bytes long and all the characters are shuffled according to a key. 
We consider all keys from 0 to 255 and reverse the decrypt function as shown in encrypt.py.  
  
  
### Flag
`{FLG:but_1_th0ught_Dlog_wa5_h4rd}`
