"""
generate data file which contains 10^6 (4 bytes int, 12 bytes string) items.
"""

import random
import string


def random_string(string_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for k in range(string_length))


if __name__ == '__main__':
    number = random.sample(range(0xFFFFFFFF), 10 ** 6)
    items = []
    for i in range(10 ** 6):
        items.append((number[i], random_string(12)))

    with open('data', 'wb') as f:
        for item in items:
            f.write(item[0].to_bytes(4, byteorder='big'))
            f.write(item[1].encode(encoding='utf-8'))



