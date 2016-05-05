import unittest
from dictionary import my_hash_set

class test_my_hash_set(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(my_hash_set()), 0)
    def test_add_one(self):
        s = my_hash_set()
        s[1] = "one"
        self.assertEquals(len(s), 1)
        self.assertEquals(s[1], "one")
    def test_add_two(self):
        s = my_hash_set()
        s[1] = "one"
        s[2] = "two"
        self.assertEquals(len(s), 2)
    def test_add_twice(self):
        s = my_hash_set()
        s[1] = "one"
        s[1] = "one"
        self.assertEquals(len(s), 1)
    def test_remove(self):
        s = my_hash_set()
        s["one"] = 1
        del s["one"]

        try:
            del s["two"]
            self.assertTrue(False)
        except KeyError:
            pass

        self.assertEquals(len(s), 0)
    def test_one_in(self):
        s = my_hash_set()
        s["one"] = 1
        self.assertTrue("one" in s)
        self.assertFalse("two" in s)
        self.assertRaises(KeyError, lambda: s[0])
    def test_collide(self):
        s = my_hash_set()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEquals(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)
        self.assertFalse(20 in s)
    def test_rehash(self):
        s = my_hash_set()
        s[0] = "zero"
        s[10] = "ten"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        s[6] = "six"
        s[7] = "seven"
        s[8] = "eight"
        s[9] = "nine"
        s[11] = "eleven"
        self.assertEquals(len(s), 12)
        expected = \
'''[[0, 'zero'], [1, 'one'], [2, 'two'], [3, 'three'], \
[4, 'four'], [5, 'five'], [6, 'six'], [7, 'seven'], \
[8, 'eight'], [9, 'nine'], [10, 'ten'], [11, 'eleven']]'''
        self.assertEquals(str(s), expected)
        t = my_hash_set(s)
        self.assertEquals(str(t), expected)
    def test_store_false(self):
        s = my_hash_set()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])
    def test_store_none(self):
        s = my_hash_set()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEquals(s[1], None)
    def test_none_key(self):
        s = my_hash_set()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEquals(s[None], 1)
    def test_False_key(self):
        s = my_hash_set()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEquals(s[False], 1)
    def test_set_dup(self):
        s = my_hash_set()
        s[1] = "a"
        s[1] = "b"
        self.assertEquals(s[1],"b")

if __name__ == '__main__':
    unittest.main()
