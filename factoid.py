#!/usr/bin/python3
import random
import argparse
import shutil
import textwrap

factoids = ["Cats have a limited understanding of cause and effect relationships. When presented with a string that releases food when pulled, they will quickly learn to pull the string for food. However when they are presented multiple strings, only one of which releases food when pulled, they will pull the strings randomly and never appear to learn which string releases food.",
    "Leonhard Euler is the most published mathematician in history, publishing between 60 and 80 volumes over his career, many of which were published after and he went mostly blind, and even more were published posthumously.",
"Later in his life, Sir Isaac Newton pursued occult studies, producing works on chronology, alchemy and biblical interpretation.",
"Though often considered the father of geometry, the earliest versions of Euclid's \"Elements\" contain no reference to him as the author, and many of the results in the text originate from earlier mathematicians.",
"It is though that chickens have no oflactory microvillus neurons, which means that they cannot detect pheremones. However, recent research from my partner, Alison Koontz, suggests that they do!",
"Cyanoacrylate glue, often called superglue, bonds in the absence of oxygen. If you think you might have superglue on your hands, don't touch anything!", 
"The demilich, a terrifying monster caused by the failure of a lich to form completely, was first introduced in the famous \"Tomb of Horrors\" adventure for Advanced Dungeons and Dragons.",
"Though people have been playing wargames since the late 1700s, the first documented use of miniature figures to represent units in a wargame was by Robert Louis Stevenson in 1881, when he used toy soldiers in his homemade wargame."]


# Sets up our argv parser
def make_arg_handler():
    options = range(0, len(factoids))
    parser = argparse.ArgumentParser(description='Outputs a factoid')
    parser.add_argument('-n', type=int, choices=options, default=random.choice(options), 
        help='Desired factoid (Default: random)')
    return parser


def main(test_args = None):
    parser = make_arg_handler()

    if test_args is None:  # If we're being tested
        n = parser.parse_args().n
        width, _ = shutil.get_terminal_size() # Make sure it doesn't wrap on words
        fact = textwrap.fill(factoids[n], width)
        print(fact)
    
    else:
        n = parser.parse_args(test_args).n 
        return n, factoids[n]


if __name__ == "__main__":
    main()
