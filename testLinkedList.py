import unittest
from linkedList import linked_list

class test_linked_list (unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back())
    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())
    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())
    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(), 1)
        self.assertEquals(ll.pop_back(), 2)
        self.assertEquals(ll.pop_back(), 3)
        self.assertTrue(ll.empty())
    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3,2,1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(),[3,2,1])
        self.assertEquals(ll.pop_back(), "foo")
        self.assertEquals(ll.pop_back(), 1)
        self.assertTrue(ll.empty())
    def test_len(self):
        ll = linked_list()
        self.assertEquals(len(ll),0)
        ll.push_back(1)
        self.assertEquals(len(ll),1)
        ll.push_back(2)
        self.assertEquals(len(ll),2)
        ll.pop_back()
        self.assertEquals(len(ll),1)
        ll.pop_back()
        self.assertEquals(len(ll),0)
    def test_str(self):
        ll = linked_list()
        self.assertEquals(str(ll),"[]")
        ll.push_back(1)
        self.assertEquals(str(ll),"[1]")
        ll.push_back(2)
        self.assertEquals(str(ll),"[1,2]")
        ll.pop_back()
        self.assertEquals(str(ll),"[1]")
        ll.pop_back()
        self.assertEquals(str(ll),"[]")

if __name__ == '__main__':
    unittest.main()
