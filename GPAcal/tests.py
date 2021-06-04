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

        assert getGPA_u(['A', 'B-', 'C+', 'A+'], ['1', '1', '1', '1']) == 3.325

        assert getGPA_u(['B+', 'A', 'A-', 'C', 'A+', 'C+', 'A'],
                        ['1', '1', '1', '1', '1', '1', '1']) == 3.3714285714285714

        assert getGPA_u(['B+', 'C-', 'D+', 'C+', 'A+', 'B-', 'A+'],
                        ['1', '1', '1', '1', '1', '1', '1']) == 2.8428571428571425

        assert getGPA_u(['A-', 'A+', 'A+', 'A-', 'B', 'B+', 'C-'],
                        ['1', '1', '1', '1', '1', '1', '1']) == 3.4285714285714284

        assert getGPA_u(['C-', 'F', 'A+', 'A', 'A-', 'A', 'B'],
                        ['1', '1', '1', '1', '1', '1', '1']) == 2.957142857142857

        assert getGPA_u(['C-', 'A+', 'A+', 'A+', 'B-', 'A-', 'A-'],
                        ['1', '1', '1', '1', '1', '1', '1']) == 3.5285714285714285

    def test_weighted(self):
        assert getGPA_w(['A', 'A', 'A', 'A', 'A', 'A', 'A'], [
                        'R', 'R', 'AP/IB', 'R', 'R', 'R', 'R'], ['1', '1', '1', '1', '1', '1', '1']) == 29/7

        assert getGPA_w(['A', 'B-', 'C+', 'A+'], ['R', 'H', 'C',
                        'AP/IB'], ['1', '1', '1', '1']) == 3.825

        assert getGPA_w(['B+', 'A', 'A-', 'C', 'A+', 'C+', 'A'], ['AP/IB', 'R', 'AP/IB', 'R',
                        'AP/IB', 'H-', 'AP/IB'], ['1', '1', '1', '1', '1', '1', '1']) == 4.014285714285714

        assert getGPA_w(['B+', 'C-', 'D+', 'C+', 'A+', 'B-', 'A+'], ['R', 'AP/IB', 'AP/IB', 'H+',
                        'AP/IB', 'AP/IB', 'R'], ['1', '1', '1', '1', '1', '1', '1']) == 3.5571428571428574

        assert getGPA_w(['A-', 'A+', 'A+', 'A-', 'B', 'B+', 'C-'], ['H-', 'R', 'AP/IB', 'H+',
                        'AP/IB', 'AP/IB', 'H+'], ['1', '1', '1', '1', '1', '1', '1']) == 4.214285714285714

        assert getGPA_w(['C-', 'F', 'A+', 'A', 'A-', 'A', 'B'], ['AP/IB', 'AP/IB', 'R', 'AP/IB',
                        'AP/IB', 'R', 'AP/IB'], ['1', '1', '1', '1', '1', '1', '1']) == 3.6714285714285713

        assert getGPA_w(['C-', 'A+', 'A+', 'A+', 'B-', 'A-', 'A-'], ['H-', 'H+', 'AP/IB', 'AP/IB',
                        'H+', 'H-', 'AP/IB'], ['1', '1', '1', '1', '1', '1', '1']) == 4.385714285714285

    def test_max(self):
        assert getMaxGPA(['R', 'R', 'R', 'AP/IB', 'R', 'R', 'R']) == 29/7

        assert getMaxGPA(['R', 'H', 'C', 'AP/IB']) == 4.5

        assert getMaxGPA(['AP/IB', 'R', 'AP/IB', 'R', 'AP/IB',
                         'H-', 'AP/IB']) == 4.642857142857143

        assert getMaxGPA(['R', 'AP/IB', 'AP/IB', 'H+', 'AP/IB',
                         'AP/IB', 'R']) == 4.714285714285714

        assert getMaxGPA(['H-', 'R', 'AP/IB', 'H+', 'AP/IB',
                         'AP/IB', 'H+']) == 4.785714285714286

        assert getMaxGPA(['AP/IB', 'AP/IB', 'R', 'AP/IB',
                         'AP/IB', 'R', 'AP/IB']) == 4.714285714285714

        assert getMaxGPA(['H-', 'H+', 'AP/IB', 'AP/IB', 'H+',
                         'H-', 'AP/IB']) == 4.857142857142857
