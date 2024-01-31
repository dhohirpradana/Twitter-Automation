import random
import time

from function import update_name, update_banner, new_year


def delay():
    delay_seconds = random.randint(7, 13)

    # Delay for the random duration
    print(f"Waiting {delay_seconds} seconds...")
    time.sleep(delay_seconds)


if __name__ == "__main__":
    update_name()

    delay()
    update_banner()

    delay()
    new_year()
