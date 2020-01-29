


############### Triangle Class ###############

def classifyTriangle(a,b,c):
    
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    
    
    # For three sides to be a triangle, the sum of two sides should be less than the third side so we have to ensure that before checking         which type of triangle it is
    if (a >= b + c) or (c >= a + b) or (b >= a + c):
        return "It is not a Triangle"
    
    # Now checking type of Triangle
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        return "Right Angled Triangle"
    elif (a != b) and (b != c) and (a != c):
        return "Scalene Triangle"
    elif a == b and b == c:
        return "Equilateral Triangle"
    else:
        return "Isoceles Triangle"


############## Testing ##################

 import unittest

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_equilateralTriangle_1(self):
        self.assertEqual(classifyTriangle(10, 10, 10), "Equilateral Triangle")
        
    def test_equilateralTriangle_2(self):
        self.assertEqual(classifyTriangle(11, 11, 11), "Equilateral Triangle")
        
    def test_equilateralTriangle_3(self):
        self.assertEqual(classifyTriangle(12, 12, 12), "Equilateral Triangle")
        
    def test_isocelesTriangle_1(self):
        self.assertEqual(classifyTriangle(5, 5, 9), "Isoceles Triangle")
    
    def test_isocelesTriangle_2(self):
        self.assertEqual(classifyTriangle(4, 4, 7), "Isoceles Triangle")
        
    def test_isocelesTriangle_3(self):
        self.assertEqual(classifyTriangle(3, 3, 5), "Isoceles Triangle")
        
    def test_scaleneTriangle_1(self):
        self.assertEqual(classifyTriangle(5, 6, 10), "Scalene Triangle")
        
    def test_scaleneTriangle_2(self):
        self.assertEqual(classifyTriangle(5, 6, 7), "Scalene Triangle")
        
    def test_scaleneTriangle_3(self):
        self.assertEqual(classifyTriangle(7, 8, 9), "Scalene Triangle")
        
    def test_rightAngledTriangle_1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right Angled Triangle")
        
    def test_rightAngledTriangle_2(self):
        self.assertEqual(classifyTriangle(6, 8, 10), "Right Angled Triangle")        
        
    def test_rightAngledTriangle_3(self):
        self.assertEqual(classifyTriangle(5, 12, 13), "Right Angled Triangle")
        
    def test_notTriangle_1(self):
        self.assertEqual(classifyTriangle(2, 2, 5), "It is not a Triangle")
    
    def test_notTriangle_2(self):
        self.assertEqual(classifyTriangle(3, 3, 7), "It is not a Triangle")
        
    def test_notTriangle_3(self):
        self.assertEqual(classifyTriangle(9, 9, 19), "It is not a Triangle")
    

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)