import random

max_len = 15

digits = '0123456789'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()/:+<>,~'

combined_list = digits + upper_case + lower_case + symbols

password = ''.join(random.choice(combined_list) for _ in range(max_len))

print(password)
