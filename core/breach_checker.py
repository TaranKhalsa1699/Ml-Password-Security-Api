import hashlib
import requests

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    for line in res.text.splitlines():
        hash_suff, count = line.split(":")
        if hash_suff == suffix:
            return int(count)
    return 0
