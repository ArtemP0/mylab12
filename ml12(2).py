import random

def calculate_sum(rolls):
    return sum(rolls)
def roll(n):
    overall_max = 0
    for _ in range(n):
        rolls = [random.randint(1, 6) for _ in range(3)]
        sum_roll = calculate_sum(rolls)
        max_number = max(rolls)
        overall_max = max(overall_max, max_number)
        print(f"Випали числа: {rolls}")
        print(f"Сума чисел: {sum_roll}")
        print(f"Максимальне число цього кидання: {max_number}\n")
    print(f"Максимальне число за всі кидання: {overall_max}\n") 
n = 10
roll(n)
