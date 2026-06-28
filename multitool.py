"""
MultiTool CLI — Lekce 2: Python pro Céčkaře
============================================
Spuštění:
    python projekt.py hash <text>
    python projekt.py b64 encode <text>
    python projekt.py b64 decode <text>
    python projekt.py genpass <délka>

Doplň logiku tam, kde je označeno # TODO.
"""

import argparse
import hashlib
import base64
import secrets
import string
import codecs

# ─── Funkce pro každou subkomanadu ─────────────────────────────────────────

def vypis_hashe(text: str) -> None:
    """Výpočet a výpis MD5, SHA-1 a SHA-256 hashe zadaného textu."""
    data = text.encode("utf-8")

    # TODO: Spočítej MD5 hash z proměnné `data` pomocí hashlib
    #       a ulož výsledek (hexadecimální řetězec) do proměnné md5
    md5 = hashlib.md5(data).hexdigest()  # <- nahraď toto správným výpočtem

    # TODO: Totéž pro SHA-1 (hashlib.sha1)
    sha1 = hashlib.sha1(data).hexdigest() 

    # TODO: Totéž pro SHA-256 (hashlib.sha256)
    sha256 = hashlib.sha256(data).hexdigest()

    print(f"Text:   {text}")
    print(f"MD5:    {md5}")
    print(f"SHA-1:  {sha1}")
    print(f"SHA-256:{sha256}")


def base64_operace(operace: str, text: str) -> None:
    """Zakódování nebo dekódování Base64."""
    if operace == "encode":
        # TODO: Zakóduj `text` do Base64.
        #       Kroky: text → bytes (encode) → base64 → zpět na str (decode)
        vysledek = base64.b64encode(text.encode("utf-8")).decode()  # <- nahraď toto
        print(f"Base64: {vysledek}")
    elif operace == "decode":
        # TODO: Dekóduj Base64 řetězec `text` zpět na čitelný text.
        #       Kroky: text → bytes (encode) → base64.b64decode → str (decode)
        vysledek = base64.b64decode(text.encode("utf-8")).decode()   # <- nahraď toto
        print(f"Decoded: {vysledek}")
    else:
        print(f"Neznámá operace: {operace}. Použij 'encode' nebo 'decode'.")


def generuj_heslo(delka: int) -> None:
    """Generátor kryptograficky bezpečného hesla."""
    # TODO: Sestav abecedu (znaky, ze kterých se heslo skládá).
    #       Použij string.ascii_letters, string.digits a string.punctuation.
    abeceda = string.ascii_letters + string.digits + string.punctuation  # <- nahraď toto

    # TODO: Vygeneruj heslo o délce `delka` pomocí secrets.choice.
    #       Tip: použij list comprehension a pak "".join(...)
    heslo = join([secrets.choice(abeceda) for _ in range(delka)])  # <- nahraď toto

    print(f"Heslo ({delka} znaků): {heslo}")

def rot13(operace: str, text: str) -> None:
    """Zakóduje nebo dekóduje text pomocí šifry ROT13 (Caesar s posunem 13)."""
    if operace == "encode":
        zakodovane = codecs.encode(text, "rot13")
        print(f"rot13: {zakodovane}")
    elif operace == "decode":
        dekodovane = codecs.encode(text, "rot13")
        print(f"text: {dekodovane}")
    else:
        print(f"Neznámá operace: {operace}. Použij 'encode' nebo 'decode'.")

def ip(operace: str, text: str) -> None:
    """převádí IPv4 adresu na 32-bitový binární řetězec a zpět"""
    if operace == "bin":
        octety =  text.split(".")
        bin = ".".join(format(int(octet), "08b") for octet in octety)
        print(f"Binárně: {bin}")
    elif operace == "dec":
       octety = text.split(".")
       ip = ".".join(str(int(octet, 2)) for octet in octety)
       print(f"IP adresa: {ip}")
    else:
       print(f"Neznámá operace: {operace}. Použij 'bin' nebo 'dec'.") 

def mac():
    """vygeneruje náhodnou MAC adresu a vypíše ji ve třech formátech"""
    mac = secrets.token_bytes(6)

    mac_colon = ":".join(f"{b:02X}" for b in mac)
    print(f"MAC (colon) {mac_colon}")

    hex_str = "".join(f"{b:02x}" for b in mac)  
    mac_cisco = ".".join(hex_str[i:i+4] for i in range(0, 12, 4))
    print(f"MAC (Cisco) {mac_cisco}")

    mac_raw = "".join(f"{b:02x}"for b in mac)
    print(f"MAC (raw) {mac_raw}")
# ─── CLI rozhraní ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="multitool",
        description="Sada kryptografických utilit — Lekce 2"
    )

    # TODO: Vytvoř subparsers objekt pomocí parser.add_subparsers(dest="prikaz")
    #       a nastav mu required=True, aby argparse vyžadoval zadání subkomandy.
    subparsers = parser.add_subparsers(dest="prikaz", required=True)  # <- nahraď toto

    # TODO: Přidej subparser pro "hash":
    #       - Nápověda: "Spočítá MD5, SHA-1 a SHA-256 hash textu"
    #       - Jeden poziční argument: "text" (str)
    # parser_hash = subparsers.add_parser(...)
    # parser_hash.add_argument(...)
    parser_hash = subparsers.add_parser("hash", help="Spočítá MD5, SHA-1 a SHA-256 hash textu")
    parser_hash.add_argument("text", type=str)
    # TODO: Přidej subparser pro "b64":
    #       - Nápověda: "Zakóduj nebo dekóduj Base64"
    #       - Dva poziční argumenty: "operace" (choices=["encode","decode"]) a "text" (str)
    parser_b64 = subparsers.add_parser("b64", help="Zakóduj nebo dekóduj Base64")
    parser_b64.add_argument("operace", type=str, choices=["encode", "decode"])
    parser_b64.add_argument("text", type=str)
    # TODO: Přidej subparser pro "genpass":
    #       - Nápověda: "Generátor bezpečného hesla"
    #       - Jeden poziční argument: "delka" (int)
    parser_genpass = subparsers.add_parser("genpass",help="generátor bezpečného hesla")
    parser_genpass.add_argument("--delka", type=int)

    parser_rot13 = subparsers.add_parser("rot13", help = "Zakoduj dekoduj pomoci sifry rot13")
    parser_rot13.add_argument("operace", type=str, choices=["encode", "decode"])
    parser_rot13.add_argument("text", type=str)

    parser_ip = subparsers.add_parser("ip", help = "převádí IPv4 adresu na 32-bitový binární řetězec a zpět")
    parser_ip.add_argument("operace", type=str, choices= ["bin", "dec"])
    parser_ip.add_argument("text", type=str)

    parser_mac = subparsers.add_parser("mac", help = "vygeneruje náhodnou MAC adresu a vypíše ji ve třech formátech")

    args = parser.parse_args()

    # Dispatch — volání správné funkce podle zadané subkomandy
    # TODO: Doplň podmínky if/elif pro "hash", "b64", "genpass"
    #       a zavolej odpovídající funkci s argumenty z `args`
    if args.prikaz == "hash":
        vypis_hashe(args.text)  # <- zavolej vypis_hashe
    elif args.prikaz == "b64":
        base64_operace(args.operace, args.text)  # <- zavolej base64_operace
    elif args.prikaz == "genpass":
        generuj_heslo(args.delka)
          # <- zavolej generuj_heslo
    elif args.prikaz == "rot13":
        rot13(args.operace, args.text)
    elif args.prikaz == "ip":
        ip(args.operace, args.text)
    elif args.prikaz == "mac":
        mac()

if __name__ == "__main__":
    main()
