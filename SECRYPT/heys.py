# A basic Substitution-Permutation Network cipher, implemented by following
# 'A Tutorial on Linear and Differential Cryptanalysis'
# by Howard M. Heys
#
# 02/12/16 Chris Hicks
#
# Basic SPN cipher which takes as input a 16-bit input block and has 4 rounds.
# Each round consists of (1) substitution (2) transposition (3) key mixing

# revised by David Williams, david.m.williams@port.ac.uk, University of Portsmouth

import sys #

blockSize = 16

# Substitution: 4x4 bijective, one sbox used for all 4 sub-blocks of size 4. Nibble wise
sbox =     {0:0xE, 1:0x4, 2:0xD, 3:0x1, 4:0x2, 5:0xF, 6:0xB, 7:0x8, 8:0x3, 9:0xA, 0xA:0x6, 0xB:0xC, 0xC:0x5, 0xD:0x9, 0xE:0x0, 0xF:0x7} #key:value
sbox_inv = {0xE:0, 0x4:1, 0xD:2, 0x1:3, 0x2:4, 0xF:5, 0xB:6, 0x8:7, 0x3:8, 0xA:9, 0x6:0xA, 0xC:0xB, 0x5:0xC, 0x9:0xD, 0x0:0xE, 0x7:0xF}

# Apply sbox (1) to a 16 bit state and return the result
def apply_sbox(state, sbox):
    subStates = [state&0x000f, (state&0x00f0)>>4, (state&0x0f00)>>8, (state&0xf000)>>12]
    for idx,subState in enumerate(subStates):
        subStates[idx] = sbox[subState]
    return subStates[0]|subStates[1]<<4|subStates[2]<<8|subStates[3]<<12

# Permutation. Applied bit-wise
pbox = {0:0, 1:4, 2:8, 3:12, 4:1, 5:5, 6:9, 7:13, 8:2, 9:6, 10:10, 11:14, 12:3, 13:7, 14:11, 15:15}

def decrypt_heys_final_round(k4, k5, state, prnt=False):
    state = int(state,16)

    subKey4 = int(k4,16)
    subKey5 = int(k5,16)

    if prnt: print_binary(state, 'INPUT     ')
    if prnt: print('ROUND 4')
    #Undo final round key
    state = state^subKey5
    if prnt: print_binary(state, 'AFTER-XOR ')

    #Apply inverse s-box
    state = apply_sbox(state,sbox_inv)
    if prnt: print_binary(state, 'AFTER-SBOX')

    #Undo fourth key
    state = state^subKey4

    if prnt: print_binary(state, 'AFTER-XOR ')

    st = '{:04x}'.format(state)
    if prnt: print_hex(st)

    return st[0:4]

# Performs a single round of decryption for a single block
def decrypt_heys_round(k,state,prnt=False):
    state = int(state,16)
    if prnt: print_binary(state, 'INPUT     ')

    k = int(k,16)
    #Un-permute the state bitwise (2)
    state_temp = 0
    for bitIdx in range(0, blockSize):
        if(state & (1 << bitIdx)):
            state_temp |= (1 << pbox[bitIdx])
    state = state_temp
    if prnt: print_binary(state, 'AFTER-PBOX')

    #Apply inverse s-box
    state = apply_sbox(state,sbox_inv)
    if prnt: print_binary(state, 'AFTER-SBOX')

    state = state^k

    if prnt: print_binary(state, 'AFTER-XOR ')

    st = '{:04x}'.format(state)
    if prnt: print_hex(st)

    return st[0:4]

def print_hex(state):
    str = ""
    str += chr(int(state[0:2], 16))
    str += chr(int(state[2:4], 16))
    print(str, '     ', state[0:2].upper(), ' ', state[2:4].upper())

# Pretty prints a block
def print_binary(state, msg):
    print(msg, end=' ')

    hs = '{:04x}'.format(state).upper()
    i=0
    for j in range (15,-1, -1):
        sys.stdout.write( str((state & (1<<j)) >> j) )
        if j % 4 == 0:
            sys.stdout.write(' [')
            sys.stdout.write(hs[i])
            sys.stdout.write('] | ')
            i += 1
    print()
