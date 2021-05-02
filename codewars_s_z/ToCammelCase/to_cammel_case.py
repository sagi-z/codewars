#!/usr/bin/env python3

def to_camel_case1(text):
    word = []
    words = []
    for c in text:
        if c in '-_':
            if word:
                words.append(word)
                word = []
        else:
            word.append(c)
    if word:
        words.append(word)
    for word in words[1:]:
        word[0] = word[0].upper()
    return ''.join([c for word in words for c in word])


def to_camel_case2(text):
    words = [
        w for word in [w.split('-') for w in text.split('_')] for w in word
    ]
    res_words = words[:1]
    for word in words[1:]:
        res_words.append(word.capitalize())
    return ''.join(res_words)


def to_camel_case3(text: str):
    return text[0] + text.title().translate(str.maketrans('', '', '_-'))[1:] \
        if text else text



def main():
    for f in [to_camel_case1, to_camel_case2, to_camel_case3]:
        print(f)
        assert(f('') == '')
        assert(f('the-one_ring') == 'theOneRing')
        assert(f('The_one-ring') == 'TheOneRing')
        print("Success")

if __name__ == '__main__':
    main()
