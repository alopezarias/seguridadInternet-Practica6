from math import floor, log, ceil


def obtain(route):
    # READING OF THE DATA FROM THE FILE
    f = open(route, 'r')
    data = f.read()
    f.close()
    # STORING THE DIFFERENT KINDS OF DATA IN VARIABLES
    data = data[data.find('alf="')+5:] #go to the starting part of the alphabet
    alphabet = data[:data.find("\"")]
    people = {}
    for p in range(0, 4):
        public_key = {}
        dividers = []
        data = data[data.find('\n\n') + 2:]  #go to the next text beggining
        person = data[:data.find('\n')]
        public_key["n"] = int(data[data.find('n=')+2:data.find('\ne=')])
        public_key["e"] = int(data[data.find('e=')+2:data.find('\nf=')])
        dividers.append(int(data[data.find('f=')+2:data.find('-')]))
        dividers.append(int(data[data.find('-')+1:data.find('\n\n')]))
        public_key["f"] = dividers
        public_key["d"] = int("0")
        people[person] = public_key
    messages = {}
    for m in range(0, 4):
        data = data[data.find('Modelo')+6:]  #go to the next message begining
        messages[m] = data[data.find('\"')+1:data.find('\"\n')]
    return alphabet, people, messages


def calculate_private_key(person):
    p, q = person['f']
    phi_n = (p-1)*(q-1)
    person['d'] = extended_euclides_algorithm(person['e'], phi_n)


def extended_euclides_algorithm(e, phi_n):
    values = [[phi_n, 0], [e, 1]]
    while e != 1:
        values.append([floor(phi_n/e), 0])
        phi_n, e = e, phi_n % e
    for iteration in range(2, len(values)):
        values[iteration][1] = values[iteration-2][1] - values[iteration-1][1]*values[iteration][0]
    return number_to_module(values[len(values)-1][1], values[0][0])


def number_to_module(num, module):
    while num < 0:
        num += module
    return num % module


def to_dictionary(alphabet, key):
    dictionary = {}
    number_list = []
    for i in range(0, len(alphabet)):
        number_list.append(i)

    if key == 'numbers':
        key_list, value_list = number_list, alphabet
    elif key == 'letters':
        key_list, value_list = alphabet, number_list

    for i in range(0, len(alphabet)):
        dictionary[key_list[i]] = value_list[i]
    return dictionary


def decipher(person, ciphered_message, alphabet):
    n_alphabet = len(alphabet)
    calculate_private_key(person)
    alphabet_dictionary_number_letter = to_dictionary(alphabet, 'numbers')
    alphabet_dictionary_letter_number = to_dictionary(alphabet, 'letters')
    k = floor(log(person['n'], n_alphabet))
    blocks = separate_in_blocks(ciphered_message, k+1)
    blocks_in_numbers = letters_into_numbers(blocks, alphabet_dictionary_letter_number)
    blocks_numbers_module = blocks_to_module(blocks_in_numbers, n_alphabet)
    numbers_deciphered = decode_numbers(blocks_numbers_module, person['d'], person['n'])
    deciphered_blocks = module_to_blocks(numbers_deciphered, n_alphabet, k)
    return solve_message(deciphered_blocks, alphabet_dictionary_number_letter)


def separate_in_blocks(message, k_plus_one):
    blocks = []
    for separation in range(0, ceil(len(message) / k_plus_one)):
        blocks.append(message[separation * k_plus_one:separation * k_plus_one + k_plus_one])
    return blocks


def letters_into_numbers(blocks, dictionary):
    number_blocks = []
    for block in blocks:
        numbers = [dictionary[l] for l in block]
        number_blocks.append(numbers)
    return number_blocks


def blocks_to_module(blocks, n):
    numbers_n = []
    for block in blocks:
        numbers_n.append(block_to_module(block, n))
    return numbers_n


def block_to_module(block, n):
    num = 0
    block.reverse()
    for i in range(0, len(block)):
        num += block[i]*(n**i)
    return num


def decode_numbers(blocks, private_key, n):
    decoded = []
    private_key_binary = module_to_blocks(private_key, 2, None)
    print(private_key_binary)
    for block in blocks:
        decoded.append(modular_potentiation_algorithm(block, private_key_binary, n))
    return decoded


def modular_potentiation_algorithm(number, p, module):
    return None


def module_to_blocks(number, module, k):
    block = []
    quotient = number
    while quotient != 1:
        rest = int(quotient % module)
        block.append(rest)
        quotient = (quotient-rest)/module
    block.append(int(quotient))
    block.reverse()
    if k != None:
        #dosomething
        print(1)
    return block