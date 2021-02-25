class DigitRecover:
    def __init__(self, s, val):
        self.s = sorted(s)
        self.val = val

    def is_match(self, st):
        return sorted(st[:len(self.s)]) == self.s

    def add2dict(self, d):
        for letter in self.s:
            digit_set = d.get(letter)
            if digit_set is None:
                digit_set = set()
                d[letter] = digit_set
            digit_set.add(self)

DIGITS = [
        DigitRecover("ZERO", 0),
        DigitRecover("ONE", 1),
        DigitRecover("TWO", 2),
        DigitRecover("THREE", 3),
        DigitRecover("FOUR", 4),
        DigitRecover("FIVE", 5),
        DigitRecover("SIX", 6),
        DigitRecover("SEVEN", 7),
        DigitRecover("EIGHT", 8),
        DigitRecover("NINE", 9)
]

RECOVERY = {}
for digit in DIGITS:
    digit.add2dict(RECOVERY)


def recover(st):
    res = []
    for i in range(len(st)):
        curr_st = st[i:]
        digits = RECOVERY.get(st[i])
        if digits:
            for digit in digits:
                if digit.is_match(curr_st):
                    res.append(str(digit.val))
                    break
    if res:
        return ''.join(res)
    else:
        return 'No digits found'
