from struct import pack
from datetime import datetime
import shutil
import os

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
    
def insert_bytes(file, start, data, chunk_size=1024):
    current_pos = file.tell()
    
    filename = file.name
    
    with open(f'hexeditlyylli/{os.path.basename(filename)}', 'wb') as f:
        file.seek(0)
        for i in range(0, start, chunk_size):
            if start - i >= chunk_size:
                data_ = file.read(chunk_size)
            else:
                data_ = file.read(start)
            
            if data_ == b'':
                break
            else:
                f.write(data_)
        
        f.write(data)
        
        data_ = None
        while data_ != b'':
            data_ = file.read(chunk_size)
            f.write(data_)
    
    file.close()
    shutil.move(f'hexeditlyylli/{os.path.basename(filename)}', os.path.basename(filename))
    file = open(filename, 'rb+')
    
    file.seek(current_pos)
    
    return file

def insert_ascii(file, start, data, chunk_size=1024):
    current_pos = file.tell()
    
    filename = file.name
    
    data = bytes(int.from_bytes(bytes(char, 'windows-1252'), 'big') for char in data)
    
    with open(f'hexeditlyylli/{os.path.basename(filename)}', 'wb') as f:
        file.seek(0)
        for i in range(0, start, chunk_size):
            if start - i >= chunk_size:
                data_ = file.read(chunk_size)
            else:
                data_ = file.read(start)
            
            if data_ == b'':
                break
            else:
                f.write(data_)
        
        f.write(data)
        
        data_ = None
        while data_ != b'':
            data_ = file.read(chunk_size)
            f.write(data_)
    
    file.close()
    shutil.move(f'hexeditlyylli/{os.path.basename(filename)}', os.path.basename(filename))
    file = open(filename, 'rb+')
    
    file.seek(current_pos)
    
    return file

def remove(file, start, end, chunk_size=1024):
    current_pos = file.tell()
    
    filename = file.name
    
    with open(f'hexeditlyylli/{os.path.basename(filename)}', 'wb') as f:
        file.seek(0)
        for i in range(0, start, chunk_size):
            if start - i >= chunk_size:
                data_ = file.read(chunk_size)
            else:
                data_ = file.read(start)
            
            if data_ == b'':
                break
            else:
                f.write(data_)
        
        file.seek(end)
        
        while data_ != b'':
            data_ = file.read(chunk_size)
            f.write(data_)
    
    file.close()
    shutil.move(f'hexeditlyylli/{os.path.basename(filename)}', os.path.basename(filename))
    file = open(filename, 'rb+')
    
    file.seek(current_pos)
    
    return file

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
        data_ = pack(f'{format_string}{dtype}', data)
    elif dtype in {'e', 'f', 'd'}:
        data = float(data)
        data_ = pack(f'{format_string}{dtype}', data)
    elif dtype == 'ut':
        data_ = pack(f'{format_string}i', int(datetime.strptime(f'{data} +0000', '%Y-%m-%d %H:%M:%S %z').timestamp()))
    else:
        raise ValueError(f"invaild data type: '{dtype}'")
    
    write_bytes(file, pos, data_)
    
    return data_
    
def insert_typed_data(file, endian, pos, dtype, data):
    if endian == 'big':
        format_string = '>'
    elif endian == 'little':
        format_string = '<'
    else:
        raise TypeError(f"invaild endianness: '{endian}'")
    
    if dtype.lower() in {'b', 'h', 'i', 'q'}:
        data = int(data)
        data_ = pack(f'{format_string}{dtype}', data)
    elif dtype in {'e', 'f', 'd'}:
        data = float(data)
        data_ = pack(f'{format_string}{dtype}', data)
    elif dtype == 'ut':
        data_ = pack(f'{format_string}i', int(datetime.strptime(data, '%Y-%m-%d %H:%M:%S').timestamp()))
    else:
        raise ValueError(f"invaild data type: '{dtype}'")
    
    insert_bytes(file, pos, data_)
    
    return data_