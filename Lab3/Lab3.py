#EX1
def list_of_sets(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)

    result = [intersection, union, a_minus_b, b_minus_a]
    return result

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
result = list_of_sets(list_a, list_b)
print(result)


#EX2

def count_characters(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

input_string = "Ana has apples."
result = count_characters(input_string)
print(result)

#Ex3
def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if type(dict1) is not dict:
        return True if dict1 is dict2 else False

    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False

        value1 = dict1[key]
        value2 = dict2[key]

        if type(value1) != type(value2):
            return False

        if type(value1) is dict:
            if not compare_dicts(value1, value2):
                return False
        elif type(value1) is list:
            if not compare_lists(value1, value2):
                return False
        elif type(value1) is set:
            if not compare_sets(value1, value2):
                return False
        elif type(value1) in (int, str):
            if value1 is not value2:
                return False

    return True

def compare_lists(list1, list2):
    if type(list1) != type(list2):
        return False

    if type(list1) is not list:
        return True if list1 is list2 else False

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        value1 = list1[i]
        value2 = list2[i]

        if type(value1) != type(value2):
            return False

        if type(value1) is dict:
            if not compare_dicts(value1, value2):
                return False
        elif type(value1) is list:
            if not compare_lists(value1, value2):
                return False
        elif type(value1) is set:
            if not compare_sets(value1, value2):
                return False
        elif type(value1) in (int, str):
            if value1 is not value2:
                return False

    return True

def compare_sets(set1, set2):
    if type(set1) != type(set2):
        return False

    if type(set1) is not set:
        return True if set1 is set2 else False

    return set1 is set2

dict1 = {
    "a": 1,
    "b": [22, "lalala"],
    "c": {
        "d": "value",
        "e": [4, 6]
    }
}

dict2 = {
    "a": 1,
    "b": [22, "lalala"],
    "c": {
        "d": "value",
        "e": [4, 6]
    }
}

result = compare_dicts(dict1, dict2)
print(result)

#EX4
def build_xml_element(tag, content, attributes):
    xml_element = f"<{tag}"

    for key, value in attributes.items():
        xml_element += f' {key}="{value}"'

    xml_element += f'>{content}</{tag}>'

    return xml_element


attributes = {
    'href': 'http://python.org',
    '_class': 'my-link',
    'id': 'someid'
}

result = build_xml_element("a", "Hello there", attributes)
print(result)


#EX5
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]

            if prefix != "":
                prefix_len = len(prefix)
                if prefix_len <= len(value):
                    for i in range(prefix_len):
                        if value[i] != prefix[i]:
                            return False
                else:
                    return False

            middle_start = len(prefix)
            middle_end = len(value) - len(suffix)

            if middle != "":
                middle_len = len(middle)
                if middle_len <= middle_end - middle_start:
                    middle_index = value.find(middle, middle_start, middle_end)
                    if middle_index == -1:
                        return False
                else:
                    return False

            if suffix != "":
                suffix_len = len(suffix)
                if suffix_len <= len(value):
                    for i in range(suffix_len):
                        if value[-1 - i] != suffix[-1 - i]:
                            return False
                else:
                    return False
        else:
            return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
data = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
result = validate_dict(rules, data)
print(result)


#EX6
def unique_and_duplicate_elements(input_list):
    unique_elements = set(input_list)
    num_duplicates = len(input_list) - len(unique_elements)
    return (len(unique_elements), num_duplicates)


my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7]
result = unique_and_duplicate_elements(my_list)
print(result)


#EX7
def set_operations(*args):
    result = {}
    sets = list(args)

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            union_result = set1 | set2
            intersection_result = set1 & set2
            difference_ab = set1 - set2
            difference_ba = set2 - set1

            result[f"{set1} | {set2}"] = union_result
            result[f"{set1} & {set2}"] = intersection_result
            result[f"{set1} - {set2}"] = difference_ab
            result[f"{set2} - {set1}"] = difference_ba

    return result

set1 = {1, 2}
set2 = {2, 3}
result_dict = set_operations(set1, set2)

for key, value in result_dict.items():
    print(f"{key}: {value}")


#EX8
def loop(mapping):
    visited = set()
    result = []
    current_key = mapping.get("start")

    while current_key is not None:
        if current_key in visited:
            break
        visited.add(current_key)
        result.append(current_key)
        current_key = mapping.get(current_key)

    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result_list = loop(mapping)
print(result_list)

#EX9
def my_function(*args, **keyword_args):
    keyword_values = set(keyword_args.values())
    count = 0

    for arg in args:
        if arg in keyword_values:
            count += 1

    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)

