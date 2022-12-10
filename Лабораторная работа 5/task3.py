def get_unique_list_numbers() -> list[int]:
    from random import randint
    numbers = []
    for i in range(15):
        num = randint(-10, 10)
        if num not in numbers:
            numbers.append(num)
    return numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
