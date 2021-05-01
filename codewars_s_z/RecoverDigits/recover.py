# This version is VERY fast - no sort, no string comparison.
# Using a lookup table.
from itertools import permutations

class _LUT:
    def __init__(self):
        self._head = {}
        self._populate("ZERO", 0)
        self._populate("ONE", 1)
        self._populate("TWO", 2)
        self._populate("THREE", 3)
        self._populate("FOUR", 4)
        self._populate("FIVE", 5)
        self._populate("SIX", 6)
        self._populate("SEVEN", 7)
        self._populate("EIGHT", 8)
        self._populate("NINE", 9)

    def _populate(self, s, val):
        for perm in permutations(s, len(s)):
            loc = self._head
            for letter in perm:
                digit_dict = loc.get(letter)
                if digit_dict is None:
                    digit_dict = {'v': None}
                    loc[letter] = digit_dict
                loc = digit_dict
            loc['v'] = str(val)

    def val(self, st, start):
        loc = self._head
        for i in range(start, len(st)):
            loc = loc.get(st[i])
            if loc is None:
                return None
            else:
                v = loc['v']
                if v is not None:
                    return v
        return None

                

LUT = _LUT()

def recover(st):
    res = []
    for i in range(len(st)):
        val = LUT.val(st, i)
        if val is not None:
            res.append(val)
    if res:
        return ''.join(res)
    else:
        return 'No digits found'
