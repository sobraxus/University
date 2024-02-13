# David Williams, david.m.williams@port.ac.uk, University of Portsmouth
# Written with reference to:
# Cracking Codes with Python http://inventwithpython.com/hacking
# pycipher https://pycipher.readthedocs.io/en/master/
# vigenere-breaker https://github.com/ebakoba/vigenere-breaker/blob/master/vigenere_crypto.py
# Cryptography Tutorial https://www.geeksforgeeks.org/cryptography-tutorial/
from heys import *
from owenpki import *
from ciphertexts import *
from collections import Counter
import string
import hashlib
import math

digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

english_letter_freq = {'A': 8.17,'B': 1.29,'C': 2.78,'D': 4.25,'E': 12.70,'F': 2.23,'G': 2.02,'H': 6.09,'I': 6.97,'J': 0.15,'K': 0.77,'L': 4.03,'M': 2.41,'N': 6.75,'O': 7.51,'P': 1.93,'Q': 0.10,'R': 5.99,'S': 6.33,'T': 9.06,'U': 2.76,'V': 0.98,'W': 2.36,'X': 0.15,'Y': 1.97,'Z': 0.07}

def generate_plaintext(number, length=0):
    if len(number)!=3 or number.isnumeric()!=True:
        return 'ERROR: Input must be a string of 3 numeric digits'
    digitz = [int(x) for x in number]
    digitz = digitz+digitz
    digitx = "".join([digits[x] for x in digitz])
    if length==0:
        length = len(digitx)
    return digitx[:length]

def get_letter_count(msg):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in msg.upper():
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letter_count[letter] += 1
    return letter_count

def print_english_letter_frequency():
    for letter in english_letter_freq:
        st = letter + ': '
        for x in range(1,(int(english_letter_freq[letter]*20)//4)):
            st = st + '#'
        print(st)

def print_letter_frequency(msg):
    letter_count = get_letter_count(msg)
    for letter in letter_count:
        st = letter + ': '
        for x in range(1,letter_count[letter]//4):
            st = st + '#'
        print(st)

def print_frequency_order(msg):
    letter_count = get_letter_count(msg)
    letter_count = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1], reverse=True)}
    st = ''
    for letter in letter_count:
        st += letter
    return st

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def print_bigram_frequency(test_str):
    test_str = test_str.upper()
    input = ''.join(ch for ch in test_str if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    res = Counter(input[idx : idx + 2] for idx in range(len(input) - 1))
    keys = [x+' ' for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"] + [' '+x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    res2 = {key: res[key] for key in res if key not in keys}
    print(Counter(res2).most_common())

def decrypt_caesar(k,msg):
    letters="abcdefghijklmnopqrstuvwxyz"
    cap_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ""
    for ch in msg:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        elif ch in cap_letters:
            position = cap_letters.find(ch)
            new_pos = (position - k) % 26
            new_char = cap_letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message

def decrypt_sub(map,msg):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ""
    for ch in msg:
        if ch in letters.upper():
            if ch in map.upper():
                new_pos = map.upper().find(ch)
                new_char = letters.upper()[new_pos]
                decrypted_message += new_char
            else:
                decrypted_message += ch.lower()
        elif ch in letters:
            if ch in map.lower():
                new_pos = map.lower().find(ch)
                new_char = letters[new_pos]
                decrypted_message += new_char
            else:
                decrypted_message += ch.lower()
        else:
            decrypted_message += ch
    return decrypted_message

def calculate_index_of_coincidence(txt):
  text_length = len(txt)
  alphabet = string.ascii_uppercase
  frequency_sum = 0
  for character in alphabet:
    frequency = txt.count(character)
    frequency_sum += frequency * ( frequency - 1)
  index_of_coincidence = (1/(text_length * (text_length - 1))) * frequency_sum
  return index_of_coincidence

def find_cosets(txt, lngth):
  txt = ''.join(i for i in txt if i.isalnum()) #remove spacing and punctuation
  newText = txt.upper()
  co_sets = []
  for _ in range(0, lngth):
    co_sets.append([])
  for index, character in enumerate(newText):
    co_set_index = index % lngth
    co_sets[co_set_index].append(character)
  kosets = []
  for co_set in co_sets:
    kosets.append(''.join(co_set))
  return kosets

def cosets_index_of_coincidence(co_sets):
  indexes = []
  for co_set in co_sets:
    indexes.append(calculate_index_of_coincidence(co_set))
  average_coincidence = sum(indexes) / float(len(indexes))
  return average_coincidence

def print_coincidences_for_key_lengths(txt, max):
  coincidences = []
  st = ''
  for x in range(1,max):
    coincidence = cosets_index_of_coincidence(find_cosets(txt, x))
    st = "{:02d}".format(x) + ': '
    if max<10:
        st += ' '
    for y in range(1,int(coincidence*100)):
        st += '#####'
    print(st)

def decrypt_vigenere(k, ct):
  ct = ct.upper()
  k = k.upper()
  alphabet = string.ascii_uppercase
  key_index = 0
  translated = []
  for character in ct:
    number = alphabet.find(character)
    if number != -1:
      number -= alphabet.find(k[key_index])
      number %= len(alphabet)
      translated.append(alphabet[number])
      key_index += 1
      key_index %= len(k)
    else:
      translated.append(character)
  return ''.join(translated)

def print_tabulation(cols,txt):
    row = ''
    for ch in txt:
        row += ch
        if len(row)>=cols:
            print(row)
            row = ''
    print(row)

def decrypt_columnar_transposition(k, ct):
    k = k.lower().replace(" ", "")
    ct = ct.replace(" ", "")
    row = int(math.ceil(len(ct) / len(k)))
    matrix = [ ['X']*len(k) for i in range(row) ]
    matrix_new = [ ['X']*len(k) for i in range(row) ]
    key_order = [ k.index(ch) for ch in sorted(list(k))]
    t = 0
    for c in key_order:
        for r,ch in enumerate(ct[t : t+ row]):
            matrix_new[r][c] = ch
        t += row
    p_text = ''
    for r in range(row):
        for c in range(len(k)):
            p_text += matrix_new[r][c]
    return p_text

def sortind(word):
    t1 = [(word[i],i) for i in range(len(word))]
    t2 = [(k[1],i) for i,k in enumerate(sorted(t1))]
    return [q[1] for q in sorted(t2)]

def unsortind(word):
    t1 = [(word[i],i) for i in range(len(word))]
    return [q[1] for q in sorted(t1)]

def xor_str_hex(a, b, prnt=False):
    b = split_into_bytes_xor(b)
    a = (a * (len(b)//len(a) + 1))[:len(b)] # a will be repeated or cut to length of b
    hex_values = ["{:02x}".format(ord(x) ^ int(y,16)) for (x, y) in zip(a[:len(b)], b)]
    hex_blocks = [hex_values[x: 8+x] for x in range(0,len(hex_values),8)]
    str_values = [chr(ord(x) ^ int(y,16)) for (x, y) in zip(a[:len(b)], b)]
    str_blocks = [str_values[x: 8+x] for x in range(0,len(str_values),8)]
    if prnt==True:
        for i in range(len(hex_blocks)):
            sss = "".join(list(str_blocks)[i]).ljust(9," ")
            hhh = " ".join(list(hex_blocks)[i]).upper()
            if not sss.isprintable(): sss = '         '
            print(sss," ",hhh)
    return "".join(hex_values)

def xor_hex_hex(a, b, prnt=False):
    a = split_into_bytes_xor(a)
    b = split_into_bytes_xor(b)
    a = (a * (len(b)//len(a) + 1))[:len(b)] # a will be repeated or cut to length of b
    hex_values = ["{:02x}".format(int(x,16)^int(y,16)) for (x, y) in zip(a[:len(b)], b)]
    hex_blocks = [hex_values[x: 8+x] for x in range(0,len(hex_values),8)]
    str_values = [chr(int(x,16)^int(y,16)) for (x, y) in zip(a[:len(b)], b)]
    str_blocks = [str_values[x: 8+x] for x in range(0,len(str_values),8)]
    if prnt==True:
        for i in range(len(hex_blocks)):
            sss = "".join(list(str_blocks)[i]).ljust(9," ")
            hhh = "".join(list(hex_blocks)[i]).upper()
            if not sss.isprintable(): sss = '         '
            print(sss," ",hhh)

    return "".join(hex_values)

def xor_str_str(a, b):
    a = (a * (len(b)//len(a) + 1))[:len(b)] # a will be repeated or cut to length of b
    print(" ".join(["{:02x}".format(ord(x) ^ ord(y)).upper() for (x, y) in zip(a[:len(b)], b)]))

def xor_slide(a,b):
    b = split_into_bytes_xor(b)
    blocks = [b[i:i+len(a)] for i in range(len(b)-(len(a)-1))]
    for block in blocks:
        str_values = "".join([chr(ord(x) ^ int(y,16)) for (x, y) in zip(a[:len(block)], block)])
        if not str_values.isprintable(): str_values = '         '
        hex_values = ["{:02x}".format(ord(x) ^ int(y,16)) for (x, y) in zip(a[:len(block)], block)]
        print(str_values," "," ".join(hex_values).upper())

def sha1_msg(msg):
    h  = hashlib.sha1()
    h.update(msg.encode('utf-8'))
    return h.hexdigest()

def sha1_file(fn):
    h  = hashlib.sha1()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(fn, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

def sha256_file(fn):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(fn, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()

def md5_bytes(b):
    h  = hashlib.md5()
    h.update(b)
    return h.hexdigest()

def split_into_blocks_xor(input):
    blocks = []
    while input > 0xff:
        input,b = divmod(input, 0x100)
        blocks.insert(0, b)
    blocks.insert(0, input)
    return blocks

def split_into_bytes_xor(input):
    if len(input) %2 != 0:
        print("Input must be multiple of a number of bytes. Perhaps input is missing a nibble.")
        sys.exit(0)
    return [input[i:i+2] for i in range(0, len(input), 2)]

def print_bytes(input):
    print(''.join(format(x, '02x') for x in input).upper())
