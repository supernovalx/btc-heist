from bit import Key
from itertools import count
from rich import print
from rich.console import Console
import time

print("Loading...")

with open("addresses.txt", "r") as f:
    addresses = set([line.rstrip() for line in f.readlines()])

print(f"Loaded {len(addresses):,} addresses")


def save_key(key: Key):
    open(f"./found/{key.address}.txt", "w").write(
        f"""
        WIF: {key.to_wif()}\n
        PEM: {key.to_pem()}\n
        INT: {key.to_int()}\n
    """
    )


con = Console()

with con.status("[bold green]Working on tasks...") as status:
    for i in count(1):
        key = Key()

        if i % 10 == 0:
            status.update(f"{i:>15,} {key.address}")
            time.sleep(0.3)

        if key.address in addresses or key.segwit_address in addresses:
            print(f"FOUND: {key.address}")
            save_key(key)

        # if i == 3:
        #     break
