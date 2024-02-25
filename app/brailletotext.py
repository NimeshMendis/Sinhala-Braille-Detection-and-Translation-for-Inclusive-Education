# braille to text

import numpy as np

eng_alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
eng_alphabet = np.array(eng_alphabet)

eng_codes = ['000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110',
             '110010', '010100', '010110', '101000',  '111000', '101100', '101110', '101010',
             '111100', '111110', '111010', '011100',  '011110', '101001', '111001', '010111',
             '101101', '101111', '101011']

eng_codes = np.array(eng_codes)


vowels = [' ', 'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ', '් ']
vowels = np.array(vowels)

braille_vowels = [' ', '⠁', '⠜', '⠷', '⠻', '⠊', '⠔', '⠥', '⠳', '⠑', '⠢', '⠌', '⠭', '⠕', '⠪', '⠈']
braille_vowels = np.array(braille_vowels)

code_vowels = ['000000', '100000', '001110', '111011', '110111', '010100', '001010', '101001', '110011', '100010', '010001', '001100', '101101', '101010', '010101', '000100']
code_vowels = np.array(code_vowels)

extensions = [' ', '්', 'ා', 'ැ', 'ෑ', 'ි', 'ී', 'ු', 'ූ', 'ෙ', 'ේ', 'ෛ', 'ො', 'ෝ', 'ෞ', '්']
extensions = np.array(extensions)

consonants = ['ක', 'ඛ', 'ග', 'ඝ', 'ඞ', 'ච', 'ඡ', 'ජ', 'ඣ', 'ඤ', 'ට', 'ඨ', 'ඩ', 'ඪ', 'ණ', 'ත', 'ථ', 'ද',
              'ධ', 'න', 'ප', 'ඵ', 'බ', 'භ', 'ම', 'ය', 'ර', 'ල', 'ළ', 'ව', 'ශ', 'ෂ', 'ස', 'හ', 'ඥ', 'ෆ', 'ඹ']
consonants = np.array(consonants)

braille_consonants = ['⠅', '⠨', '⠛', '⠣', '⠬', '⠉', '⠡', '⠚', '⠴', '⠒', '⠾', '⠺', '⠫', '⠿', '⠵', '⠞', '⠹', '⠙',
                      '⠮', '⠝', '⠏', '⠱', '⠃', '⠘', '⠍', '⠽', '⠗', '⠇', '⠸', '⠧', '⠯', '⠩', '⠎', '⠓', '⠟', '⠋', '⠆']
braille_consonants = np.array(braille_consonants)

code_consonants = ['101000', '000101', '110110', '110001', '001101', '100100', '100001', '010110', '001011',
                   '010010', '011111', '010111', '110101', '111111', '101011', '011110', '100111', '100110',
                   '011101', '101110', '111100', '100011', '110000', '000110', '101100', '101111', '111010',
                   '111000', '000111', '111001', '111101', '100101', '011100', '110010', '111110', '110100', '011000']
code_consonants = np.array(code_consonants)



def find_element(searched_letter, array):
    result_tuple = np.where(array  == searched_letter)
    result_array = result_tuple[0]
    try:
        result = result_array[0]
        return result
    except IndexError:
        return "notfound"


def translate_to_text_single(formatted_text):
    braille_sentence = ""
    last_letter = 'empty'

    x = formatted_text

    if (find_element(x, code_vowels) != "notfound"):
        if(last_letter == 'consonant'):
            braille_char = extensions[find_element(x, code_vowels)]
        else:
            braille_char = vowels[find_element(x, code_vowels)]
        braille_sentence += braille_char
        last_letter = 'vowel'

    elif (find_element(x, code_consonants) != "notfound"):
        braille_char = consonants[find_element(x, code_consonants)]
        braille_sentence += braille_char
        last_letter = 'consonant'

    else:
        braille_sentence += "_"
        last_letter = 'consonant'
    return braille_sentence


def translate_to_text(formatted_text):
    braille_sentence = ""
    last_letter = 'empty'

    for x in formatted_text:
        if (find_element(x, code_vowels) != "notfound"):
            if(last_letter == 'consonant'):
                braille_char = extensions[find_element(x, code_vowels)]
            else:
                braille_char = vowels[find_element(x, code_vowels)]
            braille_sentence += braille_char
            last_letter = 'vowel'

        elif (find_element(x, code_consonants) != "notfound"):
            braille_char = consonants[find_element(x, code_consonants)]
            braille_sentence += braille_char
            last_letter = 'consonant'

        elif (x == "222222"):
            braille_sentence += " \n"

        else:
            braille_sentence += "_"
            last_letter = 'consonant'
    return braille_sentence


def translate_to_text_eng(formatted_text):
    braille_sentence = ""
    for x in formatted_text:
        if (find_element(x, eng_codes) != "notfound"):
            braille_char = eng_alphabet[find_element(x, eng_codes)]
            braille_sentence += braille_char
            last_letter = 'vowel'

        elif (x == "222222"):
            braille_sentence += " \n"

        else:
            braille_sentence += "_"
    return braille_sentence

# abcd = ['001110', '100000', '101000', '111000', '001110']
# abcde = '001110'
#
#
# print(translate_to_text_single(abcde))



