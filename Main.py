from Deck import Deck

# pip install --r requirements.txt
import numpy
import rich
import seaborn
import autopep8
import pipreqs

if __name__ == '__main__':
    single = Deck()

    print("DEALER-----")
    print(single.draw())
    print(single.draw())

    print("\nPLAYER-----")
    print(single.draw())
    print(single.draw())
