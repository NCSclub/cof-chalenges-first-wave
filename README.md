# **MZL MAKEMELTCH!!!!!**
# websites:
http websites that may have a backend i guess

## blog: **0 pts**
first level 
poorly made blog that looks old probably made with php,
we can browse through 3 articles,

the challenges:

- image displayed in an article is stored in a directory that itself contains a text file (flag) **10 pts**

- the same image has a flag in the metadata **10 pts**

- the same image has euh lsb steganography thing **15 pts**

- a comment in the html code (inspect) **5 pts**

- an article that is a tutorial on how to connect to a SSH server
    but that dumbass used his actual credentials (gets to the user1) (no flag)

- a qr code that is missing some pixels, and must be recovered manualy **20 pts**

## ~service website: **30 pts**~
~has a login screen with no sign in so the info must come from somewhere else~

# ssh servers:
home dirs contain perssonal files with emails and conversations,
the home directory contains a todo file which is a list of what the participant should do to get small flags
(display the main thread flags in .bashrc)

## user1: **30 pts**
challenges are basic shell commands:

- regex/grep:
    - have a file with a long list of strings, and the participant have to find one string (the flag) that has a specific pattern **20 pts**
    - have a file with the flag but it is altered so the exercise is to search and remplace a certain pattern in the key **20 pts**

- just 'cat' a file named 'flag' i guess **5 pts**

- git:
    - git repo with 2 commits, and the 1st commit is the flag **10 pts**
    - the same repo contains another branch which have a flag **10 pts**
    - in a past commit there's also another flag **10 pts**

- some text somewhere would say kill your self and they must kill a process named yourself **10 pts**

- a dictionary (file with words) is provided and the flag is a combination of 3 of them words, a hash of the flag to find is provided also. the goal is to brute force the flag **15 pts**

- get acces to user2 with a ssh key (no flag)

## user2: **40 pts**
challenges are some binary exploits and micelanious:

- funny sigint exersice, see <tests/teste.c> **15 pts**

- somewhere again a seed must be found, and that seed must be passed through euh rand function 20 times, and that would be the flag **20 pts**

- program (with user3 privileges) that does a shell command, (privilege escalation) (no flag)

## user3: **50 pts**
challeges are about cryptography:

- a feistel stucture cypher alternating between a vignere cypher and a xor cypher (xor the size of the prev vignere key) **30 pts**

- a ceasar cypher that needs to be brute forced **10 pts**

- a baufort cypher but instead of a standart table it's the 1st 676 letters of the gnu/linux copypasta **20 pts** 
```
i'd just like to interject for a moment. what you're refering to as linux, is in fact, gnu/linux, or as i've recently taken to calling it, gnu plus linux. linux is not an operating system unto itself, but rather another free component of a fully functioning gnu system made useful by the gnu corelibs, shell utilities and vital system components comprising a full os as defined by posix.
many computer users run a modified version of the gnu system every day, without realizing it. through a peculiar turn of events, the version of gnu which is widely used today is often called linux, and many of its users are not aware that it is basically the gnu system, developed by the gnu project.
there really is a linux, and these people are using it, but it is just a part of the system they use. linux is the kernel: the program in the system that allocates th
```

~# git remote repositories:~
~has some programming challeges!!!~
