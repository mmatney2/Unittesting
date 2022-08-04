#Building unit tests might seem time consuming and tedious, but they can be a critical part of any CI pipeline and are invaluable tools for catching bugs early on before they move further down the pipeline and become more costly to address.

import unittest
 
# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height
 
# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
# run the test
unittest.main()


class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
    def test_negative_case(self): 
        """expect -1 as output to denote error when looking at negative area"""
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "incorrect negative output")

#testcase class:
def test_geq(self):
  """tests if value is greater than or equal to a particular target"""
  self.assertGreaterEqual(self.rectangle.get_area(), -1)

#exceptions thrown during execution:
def test_assert_raises(self): 
  """using assertRaises to detect if an expected error is raised when running a particular block of code"""
  with self.assertRaises(ZeroDivisionError):
    a = 1 / 0

"""Now, we look at building up our tests. What if we had some code that we needed to run to set up before running each test? Well, we can override the setUp method in unittest.TestCase."""
class TestGetAreaRectangleWithSetUp(unittest.TestCase):
  def setUp(self):
    self.rectangle = Rectangle(0, 0)

  def test_normal_case(self):
    self.rectangle.set_width(2)
    self.rectangle.set_height(3)
    self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")

  def test_negative_case(self): 
    """expect -1 as output to denote error when looking at negative area"""
    self.rectangle.set_width(-1)
    self.rectangle.set_height(2)
    self.assertEqual(self.rectangle.get_area(), -1, "incorrect negative output")

"""To run the method only once per TestCase class, we can also use the setUpClass method as follows:"""
class TestGetAreaRectangleWithSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.rectangle = Rectangle(0, 0)


##COMPLETED TESTING CASE
"""Bringing everything together, this is what the complete script for the unit test would look like:"""
class TestGetAreaRectangleWithSetUp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    #this method is only run once for the entire class rather than being run for each test which is done for setUp()
    self.rectangle = Rectangle(0, 0)

  def test_normal_case(self):
    self.rectangle.set_width(2)
    self.rectangle.set_height(3)
    self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")

  def test_geq(self):
    """tests if value is greater than or equal to a particular target"""
    self.assertGreaterEqual(self.rectangle.get_area(), -1)

  def test_assert_raises(self): 
    """using assertRaises to detect if an expected error is raised when running a particular block of code"""
    with self.assertRaises(ZeroDivisionError):
      a = 1 / 0

