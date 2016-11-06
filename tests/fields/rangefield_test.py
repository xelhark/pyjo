import unittest

from pyjo import Model, RangeField
from pyjo.exceptions import RequiredField, InvalidType


class RangeFieldTest(unittest.TestCase):

    def test_range_field(self):

        class A(Model):
            foo = RangeField(min=18, max=80)

        with self.assertRaises(RequiredField):
            A()

        a = A(foo=20)
        self.assertEqual(a.foo, 20)
        self.assertEqual(a.to_pyjson()['foo'], 20)

        with self.assertRaises(InvalidType):
            a.foo = 17


if __name__ == '__main__':
    unittest.main()