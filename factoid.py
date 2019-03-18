#!/bin/python3
import random
import argparse

factoids = ["Cats have a limited understanding of cause and effect relationships. When presented with a string that releases food when pulled, they will quickly learn to pull the string for food. However when they are presented multiple strings, only one of which releases food when pulled, they will pull the strings randomly and never appear to learn which string releases food.",
    "Leonhard Euler is the most published mathematician in history, publishing between 60 and 80 volumes over his career, many of which were published after and he went mostly blind, and even more were published posthumously.",
"Later in his life, Sir Isaac Newton pursued occult studies, producing works on chronology, alchemy and biblical interpretation.",
"Though often considered the father of geometry, the earliest versions of Euclid's \"Elements\" contain no reference to him as the author, and many of the results in the text originate from earlier mathematicians."]



def main(test_args = None):
    options = range(0, len(factoids))
    parser = argparse.ArgumentParser(description='Outputs a factoid')
    parser.add_argument('-n', type=int, choices=options, default=random.choice(options), 
        help='Desired factoid (Default: random)')
    if test_args is None:
        n = parser.parse_args().n
        print(factoids[n])
    
    else:
        n = parser.parse_args(test_args).n
        return n, factiods[n]


if __name__ == "__main__":
    main()
