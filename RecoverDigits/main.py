#!/usr/bin/env python
from RecoverDigits.recover import recover


def main():
    assert(recover('ONE') == '1')
    assert(recover('NEO') == '1')
    assert(recover('NEOTW') == '12')
    assert(recover('NEOTWD') == '12')

if __name__ == '__main__':
    main()

