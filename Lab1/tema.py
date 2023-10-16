#Ex1

def gcd(a, b):
    while b != 0:
        aux = a % b

        a = b
        b = aux

    return a


def find_gcd_of_numbers(numbers):

    if len(numbers) < 2:
        print("At least two numbers are required to calculate the GCD.")
    else:
        result = numbers[0]
        for num in numbers[1:]:
            result = gcd(result, num)

        print(f"The greatest common divisor of the numbers is: {result}")

numbers_input = input("Insert numbers: ")
numbers_list = [int(num) for num in numbers_input.split()]
find_gcd_of_numbers(numbers_list)


#EX2

def count_vowels(text):
    vowels = set("aeiouAEIOU")

    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


text = input("Enter the text: ")
vowel_count = count_vowels(text)
print(f"The number of vowels in the text: {vowel_count}")


#EX3

def count_occurrences(substring, text):
    count = 0
    i = 0

    while i < len(text):
        if text[i] == substring[0]:
            j = 0
            match = True

            while j < len(substring):
                if text[i + j] != substring[j]:
                    match = False
                    break
                j += 1

            if match:
                count += 1
            i += j
        else:
            i += 1

    return count


substring = input("Enter the substring: ")
text = input("Enter the text: ")

occurrences = count_occurrences(substring, text)
print(f"The substring '{substring}' appears {occurrences} times in the text.")

#EX4

def lowercase_with_underscores(input_string):
    output_string = ""

    for i, char in enumerate(input_string):
        if char.isupper():
            if i != 0:
                output_string += '_' + char.lower()
            else:
                output_string += char.lower()
        else:
            output_string += char

    return output_string

input_string = input("Enter a text in UpperCamelCase: ")
output_string = lowercase_with_underscores(input_string)
print("Converted text in lowercase_with_underscores:", output_string)


#EX5

def spiralOrder(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction = 0
    x, y = 0, 0
    result = []

    for _ in range(rows * cols):
        result.append(matrix[x][y])
        visited.add((x, y))

        new_x = x + directions[direction][0]
        new_y = y + directions[direction][1]

        if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
            x, y = new_x, new_y
        else:
            direction = (direction + 1) % 4
            x = x + directions[direction][0]
            y = y + directions[direction][1]

    return result

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiralOrder(matrix)
print(result)


#EX6

def is_palindrome(number):
    original_number = number

    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return original_number == reversed_number

number = int(input("Enter a number: "))

result = is_palindrome(number)
if result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

#EX7

def extract_and_count_numbers(text):
    first_number = ""
    index = 0

    while index < len(text) and not text[index].isdigit():
        index += 1

    while index < len(text) and text[index].isdigit():
        first_number += text[index]
        index += 1

    return int(first_number) if first_number else None


text = input("Enter a text: ")
result = extract_and_count_numbers(text)

if result is not None:
    print(f"First number in text: {result}")
else:
    print("No number found in the text.")


#EX8

def bits_with_value_1():
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Input must be a non-negative integer.")

    binary_representation = ""
    while number > 0:
        binary_representation = str(number % 2) + binary_representation
        number //= 2

    count = binary_representation.count('1')

    return count

result = bits_with_value_1()
print(f"Number of bits with the value 1: {result}")


#Ex9

def most_common_letter(text):

    new_text = text.replace(" ", "").lower()

    most_common = max(new_text, key=new_text.count)
    count = new_text.count(most_common)

    return most_common, count


text = input("Enter a text: ")

common_letter, count = most_common_letter(text)
print(f"The most common letter is '{common_letter}' with {count} occurrences.")


# Ex10

def count_words(text):
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
    word_count = space_count + 1
    return word_count

text = input("Enter a text: ")
result = count_words(text)
print("Number of words:", result)
