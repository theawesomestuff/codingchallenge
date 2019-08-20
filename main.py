import argparse

from glasses import TriangularGlassStack


def main():
    description = (
        'Water Overflow Problem: '
        'Given a stack of water glasses in form of triangle, '
        'where each glass with capacity of 250ml, '
        "calculate how much liquid is in the j'th glass '"
        "of the i'th row when K litres is poured"
    )

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('i', metavar='i', type=int,
                        help='row index (starts from zero)')
    parser.add_argument('j', metavar='j', type=int,
                        help='glass index (starts from zero)')
    parser.add_argument('k', metavar='k', type=float,
                        help='amount of liquid in litres')

    args = parser.parse_args()

    stack = TriangularGlassStack()
    liquid_ml = args.k * 1000  # Convert k from litres to ml
    stack.add_liquid(liquid_ml)
    print(stack.get_liquid(args.i, args.j))


if __name__ == '__main__':
    main()
