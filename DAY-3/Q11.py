import struct

numbers = [10, 20, 30, 40]  # List of integers

with open('numbers.bin', 'wb') as file:
    for num in numbers:
        file.write(struct.pack('i', num))  # Convert each integer to 4-byte binary format

print("Binary numbers written successfully.")

#Explanation:

#The struct.pack('i', num) converts an integer into a 4-byte binary representation.
#The wb mode is used to store these bytes in a binary file.