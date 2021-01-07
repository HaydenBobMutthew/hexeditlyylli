from struct import pack

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
    
def write_typed_data(file, endian, pos, dtype, data):
    if endian == 'big':
        format_string = '>'
    elif endian == 'little':
        format_string = '<'
    else:
        raise TypeError(f"invaild endianness: '{endian}'")
    
    if dtype.lower() in {'b', 'h', 'i', 'q'}:
        data = int(data)
    elif dtype in {'e', 'f', 'd'}:
        data = float(dtype)
    else:
        raise ValueError(f"invaild data type: '{dtype}'")
    
    data_ = pack(f'{format_string}{dtype}', data)
    
    write_bytes(file, pos, data_)
    
    return data_