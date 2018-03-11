import sys


def main():
    dic = {
        "W": "Q",
        "E": "W",
        "R": "E",
        "T": "R",
        "Y": "T",
        "U": "Y",
        "I": "U",
        "O": "I",
        "P": "O",
        "S": "A",
        "D": "S",
        "F": "D",
        "G": "F",
        "H": "G",
        "J": "H",
        "K": "J",
        "L": "K",
        "X": "Z",
        "C": "X",
        "V": "C",
        "B": "V",
        "N": "B",
        "M": "N",
        # Accents
        "[": "P",
        ";": "L",
        ",": "M",
        ".": ",",
        "/": ".",
        " ": " ",
        "\n": "\n",
        # Numbers
        "2": "1",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
        "0": "9",
    }

    for line in sys.stdin:
        for letter in line:
            print(dic[letter], end="")



if __name__ == "__main__":
    main()
