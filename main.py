def rombusz_kerület(a: float) -> float:
    kerület: float = 4 * a
    return kerület

def rombusz_terület(a: float, m: float) -> float:
    terület: float = a * m
    return terület


def main() -> None:
    print("Rombusz kerület terület számítás")
    print("")
    print("Az adatokat cm-ben adja meg!")

    a = float(input("Adja meg a rombusz egyik oldalát: "))
    m = float(input("Adja meg a rombusz magasságát: "))
    if a <= 0 or m <= 0:
        print("Egyik érték sem lehet negatív szám vagy nulla")
    else:
        kerület: float = round(rombusz_kerület(a), 2)
        terület: float = round(rombusz_terület(a, m), 2)
        print(f"A rombusz kerülete: {kerület} cm")
        print(f"A rombusz területe: {terület} cm²")


if __name__ == '__main__':
    main()