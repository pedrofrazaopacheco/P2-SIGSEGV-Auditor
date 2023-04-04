# Project 2 SIGSEGV discovery bugs
 
This is a python script for generating random test cases for a C project.

## How to use
- Clone the repo or download the tester.py
- Put the tester.py in the same folder as your executable
- If your executable is named differently than "project2", change the last line of the tester.py to handle your executable name
- Run python3 tester.py until the program stops with a segmentation fault error

# IMPORTANT
To check the last line before a segmentation fault, you should add a case to your c program like this, so that it appears the last printed number before the error!
```c
case 'o':
    printf("%s\n", commands[1]);
    break;
```


### Final note
Run the program until you get a SIGSEGV error. Please do not modify the python program to make a loop of testing because that will not work.
Only run once at a time, and statistically, a random test will be created that will crash your program
Read the *Infinite monkey theorem*
