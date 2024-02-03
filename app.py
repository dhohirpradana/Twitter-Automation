import random
import time

from function import update_name, update_banner


def delay():
    delay_seconds = random.randint(7, 13)

    for i in range(delay_seconds):
        print(f"Waiting {delay_seconds - i} seconds...")
        time.sleep(1)


if __name__ == "__main__":
    print("Updating name")
    UPDATE_NAME = update_name()
    if UPDATE_NAME:
        print("Success update name")
    else:
        print("Failed update name")
        exit()

    # delay()
    # UPDATE_BANNER = update_banner()
    # if UPDATE_BANNER:
    #     print("Success update banner")
    # else:
    #     print("Failed update banner")
    #     exit()
