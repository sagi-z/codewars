#!/usr/bin/env python3

# Recursion depth is problematic for large numbers
def digital_root1(n):
    sum = 0
    while n > 10:
        sum += n % 10
        n = int(n / 10)
    sum += n
    if sum < 10:
        return sum
    else:
        return digital_root1(sum)


# Recursion depth is problematic for large numbers
def digital_root2(n):
    sum = 0
    for d in str(n):
        sum += int(d)
    if sum < 10:
        return sum
    else:
        return digital_root2(sum)


def digital_root3(n):
    while True:
        sum = 0
        while n >= 10:
            sum += n % 10
            n = n // 10
        sum += n
        if sum < 10:
            return sum
        else:
            n = sum


def digital_root4(n):
    # The explanation to this is mathematical:
    #  1023 = 1*(999+1)+0*(99+1)+2*(9+1)+3 = (1*999+0*99+2*9)+1+0+2+3
    #  if n % 9 != 0, return it
    #  if n % 9 == 0, then
    #       if n == 0 then return 0
    #       else return 9 (the numbers will always be reduced to 2 numbers
    #                      which sum up to 9)
    return n%9 or n and 9


def main():
    for f in [digital_root3, digital_root4]:
        print(f)
        assert(f(0) == 0)
        assert(f(9) == 9)
        assert(f(5) == 5)
        assert(f(16) == 7)
        assert(f(942) == 6)
        assert(f(132189) == 6)
        assert(f(493193) == 2)
        assert(f(3072975576055479914) == 5)
        print("Success")


if __name__ == '__main__':
    main()
