#NOT WORKING ALL CODES!!!!

import random
import string

def generate_random_code():
    first_char = random.choice(string.ascii_uppercase)
    numbers = ''.join(random.choices(string.digits, k=8))
    random_code = first_char + numbers
    return random_code

def generate_multiple_codes(n):
    codes = [generate_random_code() for _ in range(n)]
    return codes

random_codes = generate_multiple_codes(50)
for code in random_codes:
    print(code)

#NOT WORKING ALL CODES!!!!