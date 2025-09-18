#!/usr/bin/python3
from checkmate import checkmate


def main():
    # (required) board must be square
    board = """
        R...
        .K..
        ..P.
        ....
"""

    checkmate(board)


if __name__ == "__main__":
    main()
