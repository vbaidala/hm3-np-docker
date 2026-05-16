import numpy as np


# створюємо одновимірний масив з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, size=200)

print("Початковий масив:")
print(arr)


# створюємо маску для вибору тільки додатних чисел
positive_mask = arr > 0

# фільтруємо масив за маскою
positive_numbers = arr[positive_mask]

print("\nДодатні числа:")
print(positive_numbers)


# замінюємо всі від’ємні значення на нулі
arr[arr < 0] = 0

print("\nМасив після заміни від’ємних значень на нулі:")
print(arr)


# обчислюємо середнє значення отриманого масиву
mean_value = np.mean(arr)

print("\nСереднє значення отриманого масиву:")
print(mean_value)