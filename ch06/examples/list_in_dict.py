# some flavors/versions of the three main PC Operating Systems
flavors_of = {
    "linux": ["debian", "fedora", "arch", "manjaro", "gentoo"],
    "windows": ["95", "xp", "vista", "7", "8", "10"],
    "mac": ["cheetah", "tiger", "leopard", "lion", "mojave"],
}

for os in flavors_of:
    print(f"Some flavors of {os}: {flavors_of[os]}")
