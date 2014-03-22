def sum_of_digits(num):
    sum=0
    if num<0 :
        num = -num
    while num != 0 :
        sum+=num%10
        num//=10
    return sum

def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))

if __name__ == '__main__':
    main()