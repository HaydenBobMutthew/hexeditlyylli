from struct import unpack
from datetime import datetime, timezone

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
    
    returned = {}
    
    if len(data) >= 1:
        returned['B'] = unpack(f'{format_string}B', data[0:1])[0]
        returned['b'] = unpack(f'{format_string}b', data[0:1])[0]
    else:
        returned['H'] = 'End of file'
        returned['h'] = 'End of file'
    
    if len(data) >= 2:
        returned['H'] = unpack(f'{format_string}H', data[0:2])[0]
        returned['h'] = unpack(f'{format_string}h', data[0:2])[0]
        returned['e'] = unpack(f'{format_string}e', data[0:2])[0]
    else:
        returned['H'] = 'End of file'
        returned['h'] = 'End of file'
        returned['e'] = 'End of file'
    
    if len(data) >= 4:
        returned['I'] = unpack(f'{format_string}I', data[0:4])[0]
        returned['i'] = unpack(f'{format_string}i', data[0:4])[0]
        returned['f'] = unpack(f'{format_string}f', data[0:4])[0]
        try:
            returned['ut'] = datetime.strftime(datetime.fromtimestamp(int.from_bytes(data[0:4], endian), timezone.utc), '%Y-%m-%d %H:%M:%S UTC')
        except OverflowError:
            returned['ut'] = 'OverflowError'
        except OSError:
            returned['ut'] = 'OSError'
    else:
        returned['I'] = 'End of file'
        returned['i'] = 'End of file'
        returned['f'] = 'End of file'
        returned['ut'] = 'End of file'
    
    if len(data) >= 8:
        returned['Q'] = unpack(f'{format_string}Q', data[0:8])[0]
        returned['q'] = unpack(f'{format_string}q', data[0:8])[0]
        returned['d'] = unpack(f'{format_string}d', data[0:8])[0]
    else:
        returned['Q'] = 'End of file'
        returned['q'] = 'End of file'
        returned['d'] = 'End of file'
    
    file.seek(original_pos)
    
    return returned