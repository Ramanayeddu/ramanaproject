#Example 4: Writing a String to a Binary File

text = "Python Binary Write"
encoded_text = text.encode('utf-8')  # Convert string to bytes

with open('text.bin', 'wb') as file:
    file.write(encoded_text)

print("Text written to binary file successfully.")


#encode('utf-8') converts the string into binary format.
#The binary data is then written to a file.
