#!/usr/bin/python3

def roman_to_int(roman_string):
    """Function converts a Roman numeral to an integer."""
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom_dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ebi_roms = [rom_dictionary[eb] for eb in roman_string]
    result = 0
    for e in range(len(ebi_roms)):
        result += ebi_roms[e]
        if ebi_roms[e - 1] < ebi_roms[e] and e != 0:
            result -= (ebi_roms[e - 1] + ebi_roms[e - 1])
    return result
