import unittest
from palindrome import *

class test_remove_spaces (unittest.TestCase):
    def test_remove_space_none(self):
        self.assertEquals (remove_spaces (None), None)
    def test_remove_space_empty(self):
        self.assertEquals (remove_spaces (""), "")
    def test_remove_space_one(self):
        self.assertEquals (remove_spaces (" "), "")
    def test_remove_space_two(self):
        self.assertEquals (remove_spaces ("  "), "")
    def test_remove_space_inside(self):
        self.assertEquals (remove_spaces ("a b c"), "abc")
    def test_remove_space_before(self):
        self.assertEquals (remove_spaces (" a b c"), "abc")
    def test_remove_space_after(self):
        self.assertEquals (remove_spaces ("a b c "), "abc")
    def test_remove_space_before_and_after(self):
        self.assertEquals (remove_spaces (" a b c "), "abc")
    def test_special_characters(self):
        self.assertEquals (remove_spaces (" ! 9 & "), "!9&")
    def test_raise_typerror_int(self):
        self.assertRaises (TypeError, lambda: remove_spaces (1))
    def test_raise_typerror_float(self):
        self.assertRaises (TypeError, lambda: remove_spaces (1.0))
    def test_raise_typerror_list(self):
        self.assertRaises (TypeError, lambda: remove_spaces ([1,2,3]))

class test_palindrome (unittest.TestCase):
    def test_none(self):
        self.assertFalse (palindrome (None))
    def test_empty(self):
        self.assertTrue (palindrome (""))
    def test_one_letter(self):
        self.assertTrue (palindrome ("v"))
    def test_two_letters(self):
        self.assertTrue (palindrome ("vv"))
    def test_toyota(self):
        self.assertTrue (palindrome ("atoyota"))
    def test_toyota_with_spaces(self):
        self.assertTrue (palindrome (remove_spaces ("a toyota")))
    def test_odd_even(self):
        self.assertTrue (palindrome (remove_spaces ("never odd or even")))
    def test_rat(self):
        self.assertTrue (palindrome (remove_spaces ("Was It a Rat I saW")))
    def test_rat_diff_case(self):
        self.assertFalse (palindrome (remove_spaces ("was It a Rat I saW")))
    def test_not(self):
        self.assertFalse (palindrome (remove_spaces ("i'm not a palindrome")))
    def test_special_characters_palindrome(self):
        self.assertTrue (palindrome (remove_spaces ("! 9 & 9 !")))
    def test_special_characters_no_palindrome(self):
        self.assertFalse (palindrome (remove_spaces ("! 9 & 8 !")))
    def test_raise_typerror_int(self):
        self.assertRaises (TypeError, lambda: palindrome (1))
    def test_raise_typerror_float(self):
        self.assertRaises (TypeError, lambda: palindrome (1.0))
    def test_raise_typerror_list(self):
        self.assertRaises (TypeError, lambda: palindrome ([1,2,3]))

if __name__ == '__main__':
    unittest.main()
