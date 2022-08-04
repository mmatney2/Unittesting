def getEven(arr):
    arr2 = []
    for num in arr:
        if num % 2 == 0:
            arr2.append(num)
    return arr2
print(getEven([1,2,3,4,5]))
    
import unittest

# write a function that takes in a list of integers and
# returns a new list of only the even numbers


class TestFunction(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(getEven([]),[])
    def test_1(self):
        self.assertEqual(getEven([1,1,1]),[])
    def test_even(self):
        self.assertEqual(getEven([2,2,4,6,8]), [2,2,4,6,8])
    def test_mix(self):
        self.assertEqual(getEven([1,2,45,6,8]), [2,6,8])


if __name__ == '__main__':
    unittest.main()