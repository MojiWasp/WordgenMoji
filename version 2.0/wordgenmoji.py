
from itertools import permutations
import os
from datetime import datetime


# =============================================
# 1. version 1 mode
# =============================================
def generate_simple(words):
    """
    Generates combinations using basic rules:
    - All permutations of input words
    - Case variations + common suffixes/prefixes like 123, @, !, #
    """
    combos = set()
    for r in range(1, len(words) + 1):
        for perm in permutations(words, r):
            base = ''.join(perm)
            combos.update([
                base,
                base.lower(),
                base.upper(),
                base.capitalize(),
                base + "123",
                "123" + base,
                "@" + base,
                base + "@",
                "!" + base,
                base + "!",
                "#" + base,
                "#" + base 
            ])
    return sorted(combos)


# =============================================
# 2. Advanced (Version 1.1 mode)
# =============================================
def generate_advanced(words):
    """
    More aggressive rules: over 30+ variations per permutation
    Includes numbers, symbols,  double chars, etc.
    """
    combos = set()
    for r in range(1, len(words) + 1):
        for perm in permutations(words, r):
            base = ''.join(perm)
            combos.update([
                base, base.lower(), base.upper(), base.capitalize(),
                base + "123", "123" + base,
                "@" + base, base + "@",
                "!" + base, base + "!",
                "#" + base, base + "#",
                base + "0", "0" + base, "1" + base, base + "1",
                "2" + base, base + "2",
                "X" + base, base + "X",
                "00" + base, base + "00",
                "#@" + base, base + "#@",
                "@#" + base, base + "@#",
                "*" + base, base + "*",
                "0" + base + "0",
                "00" + base + "0",
                "123" + base + "321",
                "@" + base + "@",
                "#" + base + "#",
                "#" + base + "@",
                "@" + base + "#",
                "#" + base + "!",
                "@!" + base + "#",
                "@" + base + "!"
            ])
    return sorted(combos)

def main():
    # clear terminal (works on Windows or Linux or mac)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 55)
    print("       WordgenMoji 2.0 - TERMINAL Mode")
    print("=" * 55)

    # --- Choose generation mode 
    while True:
        print("\nSelect generation mode:")
        print("1 → Simple Wordlist (version 1)")
        print("2 → Advanced Wordlist (version 1.1)")
        choice = input("\nEnter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Please enter 1 or 2 !!!")

    # --- output method 
    while True:
        output_mode = input("\nOutput to terminal or file? (t = terminal, f = file): ").strip().lower()
        if output_mode in ['t', 'f']:
            break
        print("Please type 't' for terminal or 'f' for file.")

    # --- collect input words
    print("\nEnter words one by one (press Enter with no input to finish):")
    words = []
    while True:
        word = input(f"Word {len(words)+1}: ").strip()
        if not word:
            if not words:
                print("You must enter at least one word!")
                continue
            break
        words.append(word)

    print(f"\nGenerating wordlist from {len(words)} word(s)...")

    # --- Generate combinations
    if choice == '1':
        result = generate_simple(words)
        mode_name = "Simple"
    else:
        result = generate_advanced(words)
        mode_name = "Advanced"

    total = len(result)
    print(f"Done! Generated {total:,} combinations ({mode_name} mode)")

    
    if output_mode == 'f':
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"wordlist_{mode_name.lower()}_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for line in result:
                f.write(line + '\n')
        print(f"Saved to: {filename}")

    else:  # Terminal output with safety pause
        print(f"\n--- Showing results ({total} lines total) ---")
        for i, line in enumerate(result, 1):
            print(line)
            if i == 500 and total > 500:
                cont = input(f"\n... {total - 500} more lines. Continue? (y/n): ")
                if cont.lower() != 'y':
                    print("Stopped by user.")
                    break
        print("\n--- End of output ---")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
