# web/stegano:
- **5 pts** a comment in the html code (inspect)
- **5 pts** image displayed in an article is stored in a directory that itself contains a text file (flag)
- **5 pts** the same image has a flag in the metadata
- **10 pts** also a text is hidden IN the image, when you play with the lightning and contrast
- **10 pts** an image of an old screenshot of the website, showing a section that is not accessible now (sections are accessible with string queries so should manualy enter the string query)
- **15 pts** the same image has euh lsb steganography thing (one flag in each color channel)
- **15 pts** a flag hidden in the cookies of the session (have to go lookup the euh webtools of the browser)
- **20 pts** a qr code that is missing some pixels, and must be recovered manualy
- **20 pts** an event that triggers euh adds a query string to the url, and that qeury string is a base64 encrypted string of a flag
- **10 pts** a image with diffrent colors and the flag is the hex value of the color converted to ascci (each 2 digit of the code is one char)

# linux shell
- **2 pts** just 'cat' a file named 'flag' i guess
- **15 pts** a dictionary (file with words) is provided and the flag is a combination of 3 of them words, a hash of the flag to find is provided also. the goal is to brute force the flag
- **15 pts** check for open ports and find an unusual port that is listening, is a http server that gives a flag with a simple get request

## git:
- **5 pts** git repo with 2 commits, and the 1st commit is the flag
- **5 pts** the same repo contains another branch which have a flag

## grep/regex:
- **10 pts** have a file with a long list of strings, and the participant have to find one string (the flag) that has flag{.*}
- **20 pts** have a file with a long list of strings, and the participant have to find one string (the flag) that has a specific pattern
- **20 pts** have a file with the flag but it is altered so the exercise is to search and remplace a certain pattern in the key

# pwn:
- **20 pts** seed must be found, and that seed must be passed through euh rand function 20 times, and that would be the flag

# forensic:
- **20 pts** broken epub file, flag hidden in content

# miscs:
- **15 pts** funny sigint exersice, see <tests/teste.c>
- **20 pts** "Syscall Roulette": A binary that randomly picks 1 of 5 syscalls to reveal the flag you must brute force the lucky one

# crypto
- **5 pts** simple vignere cypher
- **5 pts** simple rot13
- **5 pts** base64 encode
- **5 pts** base64 encode then rot13
- **10 pts** xor cypher but with no key provided or plaintext, (known plaintext attack)
- **10 pts** a program that does an unspecified cypher to any input text, and a cyphertext of the flag is provided (chosen plaintext attack)
- **10 pts** a ceasar cypher that needs to be brute forced (hash of the flag given)
- **25 pts** a feistel stucture cypher alternating between a vignere cypher and a xor cypher
- ** pts**

# reverse engineering
