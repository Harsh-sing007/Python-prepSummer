def reverse_number(num):
    rev = str(num)[::-1]
    return int(rev)

n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))