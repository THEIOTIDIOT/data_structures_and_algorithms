##Using 'with' will auto close files when done
with open('some_file.txt') as f:
    file_data = f.read()
    print(file_data)

# f.close() must be used if not using 'with'
