# Jumpyrinth (ReplyCTF - Practice)  
  
  
> While doing his mission preparation tests, R-boy notices  in the file he's reading that the data has been inserted in a  mysterious order. Read the text with him and discover what's behind it.  
> A [file](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/Jumpyrinth/2c464e58-9121-11e9-aec5-34415dec71f2.txt) containing many many symbols and another with [rules](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/Jumpyrinth/RULES.txt) was also given.  
  
  
We have to follow the rules given in the file and write code to traverse through the file until an `@` is seen.  
The starting point is said to be `$`. However, there are many of them (more than a 100) and we have no other choice than checking all those paths for the flag.  
The code to solve the challenge is in [this file](https://github.com/EnigmaEnvoy/CTF-Practice/blob/main/Jumpyrinth/solve.py).
  
  
### Flag
`{FLG:H4ckItUpH4ckItInL33tM3B3g1n}`
