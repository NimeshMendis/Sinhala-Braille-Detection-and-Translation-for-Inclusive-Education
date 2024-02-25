import numpy as np


vowels = [' ', 'අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ', '්']
vowels = np.array(vowels)

braille_vowels = [' ', '⠁', '⠜', '⠷', '⠻', '⠊', '⠔', '⠥', '⠳', '⠑', '⠢', '⠌', '⠭', '⠕', '⠪', '⠈']
braille_vowels = np.array(braille_vowels)

code_vowels = ['000000', '100000', '001110', '111011', '110111', '010100', '001010', '101001', '110011', '100010', '010001', '001100', '101101', '101010', '010101', '000100']
code_vowels = np.array(code_vowels)

extensions = [' ', '', 'ා', 'ැ', 'ෑ', 'ි', 'ී', 'ු', 'ූ', 'ෙ', 'ේ', 'ෛ', 'ො', 'ෝ', 'ෞ', '්']
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

alphabet = [vowels , braille_vowels]
alphabet = np.array(alphabet)

eng_alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
eng_alphabet = np.array(eng_alphabet)

code_eng = ['000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110',
             '110010', '010100', '010110', '101000',  '111000', '101100', '101110', '101010',
             '111100', '111110', '111010', '011100',  '011110', '101001', '111001', '010111',
             '101101', '101111', '101011']

code_eng = np.array(code_eng)

numbers = [" ",1,2,3,4,5,6,7,8,9,0]
numbers = np.array(numbers)


def find_element(searched_letter, array):
    result_tuple = np.where(array  == searched_letter.lower())
    result_array = result_tuple[0]
    try:
        result = result_array[0]
        return result
    except IndexError:
        return "notfound"


def normalize(text):
    tokens = list(text)
    formatted_text = np.array(tokens)
    normalized_sentence = ""
    for x in formatted_text:
        index_tuple = np.where(extensions == x)
        index_array = index_tuple[0]
        try:
            index = index_array[0]
            normalized_sentence += vowels[index]
        except IndexError:
            normalized_sentence += x
    return normalized_sentence


def translate_to_braille(text):
    tokens = list(text)
    formatted_text = np.array(tokens)
    braille_sentence = ""
    braille_codes = []
    for x in formatted_text:
        if (find_element(x, vowels) != "notfound"):
            braille_char = braille_vowels[find_element(x, vowels)]
            braille_code = code_vowels[find_element(x, vowels)]
        elif(find_element(x, consonants) != "notfound"):
            braille_char = braille_consonants[find_element(x, consonants)]
            braille_code = code_consonants[find_element(x, consonants)]
        elif (find_element(x, eng_alphabet) != "notfound"):
            braille_char = braille_consonants[find_element(x, eng_alphabet)]
            braille_code = code_eng[find_element(x, eng_alphabet)]
        elif (find_element(x, numbers) != "notfound"):
            braille_char = braille_consonants[find_element(x, numbers)]
            braille_code = code_eng[find_element(x, numbers)]
            braille_codes.append("001111")
        else:
            braille_char = "_"
            braille_code = "000000"
        braille_sentence += braille_char
        braille_codes.append(braille_code)
    print(braille_codes)
    return braille_sentence, braille_codes






# text = "පාසල"
#
# print(normalize(text))
#
# print(translate_to_braille(normalize(text)))











