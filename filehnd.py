# Open a new file for writing
with open('new_file.txt', 'w') as f:
    
    # Write some text to the file
    f.write('Hello, world!\n')
    f.write('This is a new file created with Python.\n')
    f.write('It is very easy to create new files in Python.\n')
    
    # Close the file
    f.close()
