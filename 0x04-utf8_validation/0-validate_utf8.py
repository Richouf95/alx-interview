#!/usr/bin/python3
"""
UTF-8 test
"""

def validUTF8(data):
    """
    Validation utf-8
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Prendre les 8 bits de poids faible

        if n_bytes == 0:
            if byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
