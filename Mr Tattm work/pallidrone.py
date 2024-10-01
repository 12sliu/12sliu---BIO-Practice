def pallidrone(n: str):
    print("yes" if n.lower() == n.lower()[::-1] else "no")


pallidrone(input())
