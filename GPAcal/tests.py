from django.test import TestCase
from django.test import SimpleTestCase
from GPAcal.scripts import *
# Create your tests here.


class GPAcalTestCase(SimpleTestCase):
    def setUp(self):
        pass

    def test_unweighted(self):
        assert getGPA_u(['A', 'A', 'A', 'A', 'A', 'A', 'A'], [
                        '1', '1', '1', '1', '1', '1', '1']) == 4.0

    def test_weighted(self):
        assert getGPA_w(['A', 'A', 'A', 'A', 'A', 'A', 'A'], [
                        'R', 'R', 'AP/IB', 'R', 'R', 'R', 'R'], ['1', '1', '1', '1', '1', '1', '1']) == 29/7

    def test_max(self):
        assert getMaxGPA(['R', 'R', 'R', 'AP/IB', 'R', 'R', 'R']) == 29/7
