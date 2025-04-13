import random

def unique_id():
    return random.randint(100000,999999)


if __name__ == "__main__":
    print(unique_id())