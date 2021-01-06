def write_bytes(file, start, data):
    current_pos = file.tell()
    file.seek(start)
    file.write(data)
    file.seek(current_pos)
        
def write_ascii(file, start, data):
    current_pos = file.tell()
    file.seek(start)
    for char in data:
        file.write(bytes(char, 'windows-1252'))
    file.seek(current_pos)
    
def truncate(file, size):
    file.truncate(size)