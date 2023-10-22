#EX1
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

n = 10
result = fibonacci_sequence(n)
print(result)

#EX2

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def find_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = find_primes(numbers)
print(prime_numbers)



#EX3

def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

result = list_operations(a, b)
print("Intersection:", result[0])
print("Union:", result[1])
print("a - b:", result[2])
print("b - a:", result[3])


#EX4
def compose(notes, moves, start_position):
    song = []
    position = start_position

    for move in moves:
        song.append(notes[position])
        position = (position + move) % len(notes)

    final_note = notes[position]

    song.append(final_note)

    return song


notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
result = compose(notes, moves, start_position)
print(result)


#EX5
def zero_below_main_diagonal(matrix):
    if not matrix:
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    result_matrix = [row[:] for row in matrix]

    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                result_matrix[i][j] = 0

    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = zero_below_main_diagonal(matrix)
for row in result:
    print(row)


#EX6

def items_that_appear_x_times(x, *input_lists):
    count = {}
    result = []

    for lst in input_lists:
        for item in lst:
            count[item] = count.get(item, 0) + 1

    for item, freq in count.items():
        if freq == x:
            result.append(item)

    return result

x = 2
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
result = items_that_appear_x_times(x, list1, list2, list3, list4)
print(result)


#EX7

def is_palindrome(number):
    if number < 0:
        return False

    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number

def find_palindromes(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]

    if not palindromes:
        return (0, None)

    max_palindrome = max(palindromes)
    return (len(palindromes), max_palindrome)


numbers = [3443, 828, 7337, 56965, 8974]
result = find_palindromes(numbers)
print(result)

#EX8
def filtrare_ascii(x = 1, liste_de_stringuri=[], flag=True):
    rezultat = []

    for s in liste_de_stringuri:
        lista_caractere = []

        for caracter in s:
            cod_ascii = ord(caracter)

            if (cod_ascii % x == 0) and flag:
                lista_caractere.append(caracter)
            elif (cod_ascii % x != 0) and not flag:
                lista_caractere.append(caracter)

        rezultat.append(lista_caractere)

    return rezultat

x = 2
liste_de_stringuri = ["test", "hello", "lab002"]
flag = False
rezultat = filtrare_ascii(x, liste_de_stringuri, flag)
print(rezultat)

#EX9
def spectatori_nevazatori(matrice_inaltimi):
    nevazatori = []

    for i in range(len(matrice_inaltimi)):
        for j in range(len(matrice_inaltimi[i])):
            inaltime_spectator = matrice_inaltimi[i][j]
            inaltime_spectatori_din_fata = [matrice_inaltimi[x][j] for x in range(i)]

            if any(inaltime >= inaltime_spectator for inaltime in inaltime_spectatori_din_fata):
                nevazatori.append((i, j))

    return nevazatori

matrice_inaltimi = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

rezultat = spectatori_nevazatori(matrice_inaltimi)
print(rezultat)

#EX10
def merge_lists(*input_lists):
    max_length = max(len(lst) for lst in input_lists)
    result = []

    for i in range(max_length):
        tuple_items = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        result.append(tuple_items)

    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
result = merge_lists(list1, list2, list3)
print(result)


#EX11
def order_tuples_by_third_char(tuples_list):
    def get_third_char(item):
        return item[1][2]

    sorted_list = sorted(tuples_list, key=get_third_char)

    return sorted_list


tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
sorted_tuples = order_tuples_by_third_char(tuples_list)
print(sorted_tuples)


#EX12

def group_by_rhyme(words):
    rhyme_dict = {}

    for word in words:
        rhyme = word[-2:]

        if rhyme in rhyme_dict:
            rhyme_dict[rhyme].append(word)
        else:
            rhyme_dict[rhyme] = [word]

    grouped_by_rhyme = list(rhyme_dict.values())

    return grouped_by_rhyme


words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)



