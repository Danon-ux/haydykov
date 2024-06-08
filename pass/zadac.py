#tasks
#1
ef is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
numbers = [12, -45, 67, -34, 89, -100, 23, -5, 34]
for number in numbers:
    print(f"{number} является {'простым' if is_prime(abs(number)) else 'составным'} числом")
#2
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
numbers = [-90, 56, -23, 12, 45, -67, 89, -32, 11, -76, 54]
print("Сумма всех чисел:", sum_array(numbers))
#3
def count_positives_negatives(arr):
    positives = 0
    negatives = 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1

    return positives, negatives
  numbers = [3, -15, 27, -48, 59, -6, 14, -38, 72, -94, 18, -12]
positives, negatives = count_positives_negatives(numbers)
print("Количество положительных чисел:", positives)
print("Количество отрицательных чисел:", negatives)
#4
def find_max_min(arr):
    max_num = min(arr)
    min_num = max(arr)

    for num in arr:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num
  numbers = [-22, 45, -67, 34, -89, 100, -23, 5, -34, 78]
max_num, min_num = find_max_min(numbers)
print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)
