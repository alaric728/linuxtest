#!/usr/bin/python3
import unittest
import factoid
import random
import string

class TestFactoid(unittest.TestCase):

    # Test default case, no argument supplied
    def test_default(self):
        n, fact = factoid.main([])
        self.assertTrue(n in range(len(factoid.factoids)))
        self.assertEqual(fact, factoid.factoids[n])
        print("Default case passed!")

    # Test argument supplied is gibberish/random (definitely invalid)
    def test_arg_malformed(self):
        chars = string.ascii_letters + string.digits + string.whitespace
        num_chars = random.randrange(1, 32)
        args = ''.join(random.choice(chars) for _ in range(num_chars)) # Small chance this is valid
        with self.assertRaises(SystemExit):
            factoid.main(args.split())
        print("Malformed argument case passed!")

    # Test argument supplied is out of bounds
    def test_arg_oob(self):
        neg_test = ("-n", str(random.randrange(32)*-1))
        pos_test = ("-n", str(random.randrange(len(factoid.factoids), 32)))
        with self.assertRaises(SystemExit) as neg_exit:
            factoid.main(neg_test)
        self.assertEqual(neg_exit.exception.code, 2)
        with self.assertRaises(SystemExit) as pos_exit:
            factoid.main(pos_test)
        self.assertEqual(pos_exit.exception.code, 2)

        print("Argument out of bounds test passed!")

    # Test command option specified is invalid
    def test_arg_undefined(self):
        chars = string.ascii_letters.replace("n", '')
        arg = ("-" + random.choice(chars))
        with self.assertRaises(SystemExit):
            factoid.main(arg)

        print("Arg undefined test passed!")

    # Test too many arguments specified after n
    def test_too_many_args(self):
        valid_nums = range(len(factoid.factoids)) # Want extras to be valid
        num_additional = random.randrange(1,32) # Get random extras
        additional_args = tuple(random.choice(valid_nums) for _ in range(num_additional))
        arg = ("-n", "1") + additional_args # Form final argv
        with self.assertRaises(Exception):
            factoid.main(arg)

        print("Too many args test passed!")

    # Test a valid selection of factoid
    def test_n_valid(self):
        fact_no = random.randrange(0, len(factoid.factoids) - 1)
        arg = ("-n", str(fact_no))
        n, fact = factoid.main(arg)
        self.assertEqual(fact_no, n)
        self.assertEqual(fact, factoid.factoids[fact_no])

        print("Valid n test case passed!")

if __name__== "__main__":
    unittest.main()
