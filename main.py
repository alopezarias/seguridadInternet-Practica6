from functions import obtain as colect_data_from, decipher as clarify_message, block_to_module
import math_functions, functions


alphabet, people, messages = colect_data_from('resources/datos_6.txt')

# PEPA -> BENITO (message 0 - Modelo 1)
sender, receiver, msg_ciphered = people['Pepa'], people['Juan'], messages[3]
message = clarify_message(receiver, msg_ciphered, alphabet)
print(message.replace('  ', "\n"))
'''
María-3
Benito-0
Pepa-1
Juan-2
binary = functions.module_to_blocks(726392090981698692097, 2, 0)
number = ''
for i in binary:
    number += str(i)
print(number)
print(block_to_module(binary, 2))
print(726392090981698692097)
var = "1001110110000010110111000111100010100001011001011000001110010000000001"
array = []
for i in var:
    array.append(int(i))
print(block_to_module(array, 2))

print(1001110110000010110111000111100010100001011001011000000000000000000001 == 1001110110000010110111000111100010100001011001011000000000000000000000)
'''