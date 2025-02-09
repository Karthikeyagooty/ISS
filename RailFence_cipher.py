'''
The rail fence cipher (sometimes called zigzag cipher) is a transposition cipher that jumbles up the order of the letters of a message
using a basic algorithm.

The rail fence cipher works by writing your message on alternate lines across the page, and then reading off each line in turn.

Encrytion:
-> The plain-text is written downwards and diagonally on successive rails of an imaginary fence.
-> When we reach the bottom rail, we traverse upwards moving diagonally, after reaching the top rail, the direction is changed again.
    Thus the alphabets of the message are written in a zig-zag manner.
-> After each alphabet has been written, the individual rows are combined to obtain the cipher-text.

Text: ALGORITHMS , Key=3

A * * * R * * * M *
* L * O * I * H * S
* * G * * * T * * *

Encryted Text : ARMLOIHSGT

Decryption:
-> Construct the matrix with the given key
-> Fill the letters accordingly and then traverse the matrix in a zigzag manner.

'''

def encrypt(clearText,key):
    matrix=[["" for x in range(len(clearText))] for y in range(key)]
    increment=1
    row,col=0,0
    for c in clearText:
        if row+ increment<0 or row+increment>=len(matrix):
            increment*=-1
        matrix[row][col]=c
        row+=increment
        col+=1
    result=[]
    for i in range(key):
        for j in range(len(clearText)):
            if matrix[i][j]!='\n':
                result.append(matrix[i][j])
    return ("".join(result))

def decrypt(encryptText,key):
    matrix=[["" for x in range(len(encryptText))] for y in range(key)]
    index=0
    increment=1
    for selectedRow in range(0,len(matrix)):
        row =0
        for col in range(0,len(matrix[row])):
            if row+increment<0 or row+increment>=len(matrix):
                increment*=-1
            if row == selectedRow:
                matrix[row][col]+=encryptText[index]
                index+=1
            row+=increment
    matrix=transpose(matrix)
    result=[]
    for i in range(len(encryptText)):
        for j in range(key):
            if matrix[i][j]!='\n':
                result.append(matrix[i][j])   
    return ("".join(result))

def transpose( m ):
	result = [ [ 0 for y in range( len(m) ) ] for x in range( len(m[0]) ) ]	
	for i in range( len(m) ):
		for j in range( len(m[0]) ):
			result[ j ][ i ] = m[ i ][ j ]	
	return result

if __name__ == "__main__":
    print("Railfence Cipher: ")
    print("1. Encrypt a text")
    print("2. Decrypt a text")
    print("3. Exit")
    n=int(input())

    while n<3:
        if n==1:
            print("Encryption")
            print("Enter the text and the key: ")
            text=input()
            key=int(input())
            print("Encrpyted text using Railfence Cypher Algorithm is: ")
            print(encrypt(text,key))     
        elif n==2:
            print("Decryption")
            print("Enter the text and the key: ")
            text=input()
            key=int(input())
            print("Decrpyted text using Railfence Cypher Algorithm is: ")
            print(decrypt(text,key))

        print("1. Encrypt a text")
        print("2. Decrypt a text")
        print("3. Exit")
        n=int(input())
        
