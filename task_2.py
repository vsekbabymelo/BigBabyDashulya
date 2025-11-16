import re
from decimal import Decimal
import argparse

pattern = re.compile(
    r'^"(?P<user>[^"]+)"\s*-\s*(?P<account>\d+):\s*(?P<amount>[+-]\d+(?:\.\d+)?)$'
)

data = {}

def parse_file(file):
    with open(file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            match = pattern.match(line)
            if not match:
                print("Ошибка")
                continue

            user = match.group("user")
            account = int(match.group("account"))
            amount = Decimal(match.group("amount"))

            if user not in data:
                data[user] = {}
            if account not in data[user]:
                data[user][account] = Decimal("0")

            data[user][account] += amount


def print_data():
    for user in data:
        print('"{}" - {}'.format(user, ", ".join(str(acc)+": "+str(bal) for acc, bal in data[user].items())))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()
    parse_file(args.file)
    print_data()
