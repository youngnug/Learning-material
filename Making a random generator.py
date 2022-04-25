import random
import string

i = 0
while i < 100:
    random_user_gen = (''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(0,10)]))
    random_pass_gen = (''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(0,10)]))
    logininfo = {f"Your default username: {random_user_gen} \n:Default password {random_pass_gen}"}
    print(logininfo)
    i += 1
