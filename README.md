# **MZL MAKEMELTCH!!!!!**
# websites:
http websites that may have a backend i guess

## blog: **0 pts**
first level 
poorly made blog that looks old probably made with php,
we can browse through 3 articles,

the challenges:

- **5 pts** a comment in the html code (inspect)
- **10 pts** image displayed in an article is stored in a directory that itself contains a text file (flag)
- **10 pts** the same image has a flag in the metadata
- **10 pts** also a text is hidden IN the image, when you play with the lightning and contrast
- **10 pts** an image of an old screenshot of the website, showing a section that is not accessible now (sections are accessible with string queries so should manualy enter the string query)
- **15 pts** the same image has euh lsb steganography thing (one flag in each color channel)
- **15 pts** a flag hidden in the cookies of the session (have to go lookup the euh webtools of the browser)
- **20 pts** a qr code that is missing some pixels, and must be recovered manualy
- **20 pts** an event that triggers euh adds a query string to the url, and that qeury string is a base64 encrypted string of a flag
- **10 pts** a image with diffrent colors and the flag is the hex value of the color converted to ascci (each 2 digit of the code is one char)
- an article that is a tutorial on how to connect to a SSH server but that dumb used his actual credentials (gets to the user1) (no flag)

# ssh servers:
home dirs contain perssonal files with emails and conversations, the home directory contains a todo file which is a list of what the participant should do to get small flags (display the main thread flags in .bashrc)

## user1: **30 pts**
challenges are basic shell commands:

- **5 pts** just 'cat' a file named 'flag' i guess
- **10 pts** git repo with 2 commits, and the 1st commit is the flag
- **10 pts** the same repo contains another branch which have a flag
- **10 pts** some text somewhere would say kill yourself and they must kill a process named yourself
- **10 pts** have a file with a long list of strings, and the participant have to find one string (the flag) that has flag{.*}
- **15 pts** a dictionary (file with words) is provided and the flag is a combination of 3 of them words, a hash of the flag to find is provided also. the goal is to brute force the flag
- **15 pts** check for open ports and find an unusual port that is listening, is a http server that gives a flag with a simple get request
- **15 pts** that same http server gives another flag when sent a post request
- **20 pts** that same http server gives another flag when sent a get request with specific vales on the request headers
- **20 pts** have a file with a long list of strings, and the participant have to find one string (the flag) that has a specific pattern
- **20 pts** have a file with the flag but it is altered so the exercise is to search and remplace a certain pattern in the key
- get acces to user2 with a ssh key (no flag)

## user2: **40 pts**
challenges are some binary exploits and micelanious:

- **15 pts** funny sigint exersice, see <tests/teste.c>
- **20 pts** somewhere again a seed must be found, and that seed must be passed through euh rand function 20 times, and that would be the flag
- **20 pts** "Syscall Roulette": A binary that randomly picks 1 of 5 syscalls to reveal the flag—you must brute-force the lucky one.
- program (with user3 privileges) that does a shell command, (privilege escalation) (no flag)

## user3: **50 pts**
challeges are about cryptography:

- **5 pts** simple vignere cypher
- **5 pts** base64 decode
- **5 pts** base64 decode then rot13
- **10 pts** xor cypher but with no key provided or plaintext, only the cyphertext provided (they can guess the key because it will be encrypted with the flag{something} so they can xor the f with the 1st letter of the cypher text)
- **10 pts** a ceasar cypher that needs to be brute forced (hash of the flag given)
- **30 pts** a feistel stucture cypher alternating between a vignere cypher and a xor cypher

# outside the environment:
- **5 pts** a youtube video with a flag in the subtitle
