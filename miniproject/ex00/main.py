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
    board2 = """
        ..
        .K
"""

    checkmate(board)
    checkmate(board2)


if __name__ == "__main__":
    main()
