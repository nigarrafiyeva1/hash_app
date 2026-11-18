# Hash App
This is a Python program that stores strings in text files using hashing. When a file becomes full, the program creates another file to store the remaining text.

## How It Works
The program takes two values:
n - the number of buckets
s - the maximum number of characters in each bucket

When the program starts, it creates a folder called buckets. Inside this folder, it creates text files like 1.txt, 2.txt, and 3.txt. When the user enters a string, the program calculates its hash value and decides which file to use. More than one string can be stored in the same file. The program keeps asking for new strings until the user presses Ctrl+C.

## Hashing Algorithm

I used MurmurHash3 with the mmh3 Python library. The program uses this formula to choose a bucket:

bucket_number = (hash_value % n) + 1

This makes sure the bucket number is between 1 and n.

## Overflow Files

Each bucket can store up to s characters. If there is not enough space in a bucket, the program creates an overflow file.
For example:
3.txt
3_overflow_1.txt
3_overflow_2.txt

I used file names to connect the overflow files to the main bucket. For example, 3_overflow_1.txt belongs to 3.txt. The numbers show the order of the overflow files.

The program checks the file names to find the last overflow file. It adds new text to that file. If it becomes full, another overflow file is created. If a string does not fit in one file, the program splits it between files.

The strings are stored without commas, spaces, or other separators.

## How to Run
The program needs Python 3 and the mmh3 library.

Firstly, install the library: python -m pip install mmh3

Then run the program: python hash_app.py 5 20

Here, 5 means five buckets, and 20 means each bucket can store up to 20 characters. The program will ask you to enter strings. Press Ctrl+C to stop it.

### Notes
The program keeps existing bucket data when it starts again. If you want to test different n or s values, delete the old buckets folder first.

The .gitignore file is used to keep generated bucket files out of GitHub.