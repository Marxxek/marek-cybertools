"""
Projekt: Git Setup Checker
Lekce 1 — Git a GitHub

Tento skript ověří, že máš Git správně nastavený pro práci s GitHubem.
Spusť ho před tím, než začneš s marek-cybertools repozitářem.

Instrukce: Doplň všechna místa označená # TODO
"""

import subprocess
import os
import sys
from pathlib import Path


def spust_prikaz(prikaz: list[str]) -> tuple[str, int]:
    """Spustí příkaz a vrátí (stdout, návratový kód)."""
    try:
        vysledek = subprocess.run(
            prikaz,
            capture_output=True,
            text=True,
            timeout=10
        )
        return vysledek.stdout.strip(), vysledek.returncode
    except FileNotFoundError:
        return "", 127  # příkaz nenalezen
    except subprocess.TimeoutExpired:
        return "timeout", 1


def zkontroluj_git() -> bool:
    """Ověří, že je Git nainstalovaný a zjistí verzi."""
    print("─── Git ─────────────────────────────────")

    # TODO: Spusť příkaz ["git", "--version"] pomocí funkce spust_prikaz()
    # Nápověda: vystup, kod = spust_prikaz(["git", "--version"])
    vystup, kod = None, None  # doplň volání spust_prikaz

    if kod == 0:
        print(f"  ✓ Git nainstalován: {vystup}")
        return True
    else:
        print("  ✗ Git nenalezen — nainstaluj Git for Windows")
        return False


def zkontroluj_konfiguraci() -> bool:
    """Zkontroluje, zda má Git nastaveného uživatele."""
    print("─── Git konfigurace ─────────────────────")

    # TODO: Zjisti jméno uživatele pomocí: ["git", "config", "--global", "user.name"]
    jmeno, _ = None, None  # doplň volání spust_prikaz

    # TODO: Zjisti email pomocí: ["git", "config", "--global", "user.email"]
    email, _ = None, None  # doplň volání spust_prikaz

    ok = True

    if jmeno:
        print(f"  ✓ Jméno:  {jmeno}")
    else:
        print('  ✗ Jméno není nastaveno — spusť: git config --global user.name "Tvoje Jméno"')
        ok = False

    if email:
        print(f"  ✓ Email:  {email}")
    else:
        print('  ✗ Email není nastaven — spusť: git config --global user.email "tvuj@email.cz"')
        ok = False

    return ok


def zkontroluj_ssh_klic() -> bool:
    """Zkontroluje, zda existuje SSH klíč pro GitHub."""
    print("─── SSH klíč ────────────────────────────")

    # Cesty kde ssh-keygen ukládá klíče
    mozne_cesty = [
        Path.home() / ".ssh" / "id_ed25519.pub",
        Path.home() / ".ssh" / "id_rsa.pub",
        Path.home() / ".ssh" / "id_ecdsa.pub",
    ]

    # TODO: Projdi mozne_cesty a zkontroluj, zda některá existuje pomocí .exists()
    # Nápověda: for cesta in mozne_cesty: if cesta.exists(): ...
    nalezeny_klic = None  # nastav na nalezenou cestu nebo ponech None

    if nalezeny_klic:
        print(f"  ✓ SSH klíč nalezen: {nalezeny_klic}")
        print(f"\n  Veřejný klíč (zkopíruj na GitHub → Settings → SSH Keys):")
        print("  " + "─" * 50)
        # TODO: Přečti obsah souboru nalezeny_klic a vypiš ho
        # Nápověda: obsah = nalezeny_klic.read_text().strip()
        obsah = None  # doplň čtení souboru
        print(f"  {obsah}")
        print("  " + "─" * 50)
        return True
    else:
        print("  ✗ SSH klíč nenalezen")
        print('  Vytvoř ho: ssh-keygen -t ed25519 -C "tvuj@email.cz"')
        return False


def zkontroluj_ssh_spojeni() -> None:
    """Otestuje SSH spojení s GitHubem."""
    print("─── SSH spojení s GitHubem ───────────────")

    print("  Testuju spojení (může trvat pár sekund)...")

    # TODO: Spusť příkaz ["ssh", "-T", "-o", "StrictHostKeyChecking=no", "git@github.com"]
    # Nápověda: vystup, kod = spust_prikaz([...])
    vystup, kod = None, None  # doplň volání spust_prikaz

    # SSH vrací kód 1 i při úspěchu (GitHub neotevírá shell) — hledáme text "successfully"
    if vystup and "successfully" in vystup:
        print(f"  ✓ GitHub autentizace OK: {vystup}")
    elif kod == 127:
        print("  ✗ SSH není nainstalováno (součást Git for Windows)")
    else:
        print(f"  ✗ Připojení selhalo: {vystup or 'žádná odpověď'}")
        print("  Zkontroluj, zda jsi veřejný klíč přidal na GitHub")


def main() -> None:
    print("\n╔══════════════════════════════════════════╗")
    print("║      GIT SETUP CHECKER — Lekce 1         ║")
    print("╚══════════════════════════════════════════╝\n")

    git_ok = zkontroluj_git()

    if not git_ok:
        print("\n  Git není nainstalovaný. Postupuj podle kořenového README.md.")
        sys.exit(1)

    konfig_ok = zkontroluj_konfiguraci()
    ssh_ok = zkontroluj_ssh_klic()

    if ssh_ok:
        zkontroluj_ssh_spojeni()

    print("\n─────────────────────────────────────────")
    stav = "✓ VŠE PŘIPRAVENO" if (git_ok and konfig_ok and ssh_ok) else "⚠ OPRAV VÝŠE OZNAČENÉ PROBLÉMY"
    print(f"  {stav}")
    print("─────────────────────────────────────────\n")


if __name__ == "__main__":
    main()
