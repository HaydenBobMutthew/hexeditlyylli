from struct import unpack

def inspect(file, loc, endian):
    original_pos = file.tell()
    
    file.seek(loc)
    
    data = file.read(8)
    
    if endian == 'big':
        format_string = '>'
    elif endian == 'little':
        format_string = '<'
    else:
        raise TypeError(f"invaild endianness: '{endian}'")
    
    returned_int = {}
    returned_float = {}
    
    returned_int['8-bit Integer'] = (unpack(f'{format_string}b', data[0:1])[0], unpack(f'{format_string}B', data[0:1])[0])
    returned_int['16-bit Integer'] = (unpack(f'{format_string}h', data[0:2])[0], unpack(f'{format_string}H', data[0:2])[0])
    returned_int['32-bit Integer'] = (unpack(f'{format_string}i', data[0:4])[0], unpack(f'{format_string}I', data[0:4])[0])
    returned_int['64-bit Integer'] = (unpack(f'{format_string}q', data[0:8])[0], unpack(f'{format_string}Q', data[0:8])[0])
    
    returned_float['16-bit Floating Point'] = unpack(f'{format_string}e', data[0:2])[0]
    returned_float['32-bit Floating Point'] = unpack(f'{format_string}f', data[0:4])[0]
    returned_float['64-bit Floating Point'] = unpack(f'{format_string}d', data[0:8])[0]
    
    file.seek(original_pos)
    
    return returned_int, returned_float