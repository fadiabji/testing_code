import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """ Test Employee calss"""
    def setUp(self):
        """ Generate a employee object"""
        fname = ''
        lname = ''
        salary = 
        self.my_employee = Employee(fname, lname, salary)

    def test_give_defult_raise(self):
        """test the give raise method , by defult add 5000 to the annual salary and 7000 a custom raise"""
        self.my_employee.give_raise()
        sample_test = self.my_employee.salary
        self.assertEqual(sample_test, 35000)

    def test_give_custom_raise(self):
        """Test give_raise() method for custom belop"""
        self.my_employee.give_raise(7000)
        sample_test = self.my_employee.salary
        self.assertEqual(sample_test,37000)

if __name__ == '__main__':
    unittest.main()