import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_luku(1)
    joukko.lisaa_luku(2)
    joukko.lisaa_luku(3)
    joukko.lisaa_luku(2)

    print(joukko.joukon_luvut())


if __name__ == "__main__":
    main()
