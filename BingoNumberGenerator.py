from pathlib import Path
import random

FILE_PATH = Path("numbers.csv")
MIN_NUMBER = 1
MAX_NUMBER = 90


def load_drawn_numbers(path: Path) -> set[int]:
    if not path.exists():
        return set()

    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return set()

    numbers: set[int] = set()
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        value = int(token)
        if MIN_NUMBER <= value <= MAX_NUMBER:
            numbers.add(value)
    return numbers


def save_drawn_numbers(path: Path, numbers: set[int]) -> None:
    ordered = sorted(numbers)
    path.write_text(",".join(str(number) for number in ordered), encoding="utf-8")


def main() -> None:
    drawn_numbers = load_drawn_numbers(FILE_PATH)
    available_numbers = [n for n in range(MIN_NUMBER, MAX_NUMBER + 1) if n not in drawn_numbers]

    if not available_numbers:
        print("Fertig! Nummern komplett!!")
        return

    random_number = random.choice(available_numbers)
    drawn_numbers.add(random_number)
    save_drawn_numbers(FILE_PATH, drawn_numbers)

    print("------------------")
    print(f"------- {random_number} -------")
    print("------------------")


if __name__ == "__main__":
    main()






