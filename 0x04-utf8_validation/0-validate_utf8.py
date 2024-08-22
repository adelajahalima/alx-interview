#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.

"""

def validUTF8(data):
    number_of_bytes = 0
    
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF
        
        if number_of_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                number_of_bytes += 1
                mask >>= 1
            
            if number_of_bytes == 0:
                continue
            
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        number_of_bytes -= 1
    
    return number_of_bytes == 0
