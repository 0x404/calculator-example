from argparse import ArgumentParser

def add(a: int, b: int) -> int:
    return a + b

def min_fn(a: int, b: int) -> int:
    return min(a, b)

def max_fn(a, b):
    return max(a, b)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("--op", type=str)

    args = parser.parse_args()
    if args.op == "add":
        print(add(args.a, args.b))
    if args.op == "min":
        print(min_fn(args.a, args.b))
