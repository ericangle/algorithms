from linkedList import linked_list

class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

        stack = linked_list()
        while a > 1:
            stack.push_front(a)
            a -= 1

        result = 1
        while not stack.empty():
            result *= stack.pop_front()

        return result
