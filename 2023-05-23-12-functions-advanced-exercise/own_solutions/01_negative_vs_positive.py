def print_numbers_stat(numbers):
    sum_positive = 0
    sum_negative = 0
    for x in numbers:
        if x > 0:
            sum_positive += x
        else:  # x < 0 as it's given 0 never comes
            sum_negative += x

    print(sum_negative)
    print(sum_positive)
    if abs(sum_negative) > sum_positive:
        print("The negatives are stronger than the positives")
    elif sum_positive > abs(sum_negative):
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
print_numbers_stat(numbers)

