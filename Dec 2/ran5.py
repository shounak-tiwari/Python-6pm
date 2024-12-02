import string
import random

chart = string.ascii_letters+string.digits+string.punctuation

password = "".join(random.choices(chart,k=8))

print(password)