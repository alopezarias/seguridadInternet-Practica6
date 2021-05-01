from functions import obtain as colect_data_from, decipher as clarify_message, module_to_blocks

alphabet, people, messages = colect_data_from('resources/datos_6.txt')

# PEPA -> BENITO (message 0 - Modelo 1)
sender, receiver, msg_ciphered = people['Pepa'], people['Benito'], messages[0]
print(clarify_message(receiver, msg_ciphered, alphabet))
