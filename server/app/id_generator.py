import random


def generate_user_id():

    number = random.randint(
        10000000,
        99999999
    )

    return f"wm{number}"