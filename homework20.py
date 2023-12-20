"""Homework 20: Unit Testing with unittest."""

import unittest
from AtomCounter import AtomCounter


class TestAtomCounter(unittest.TestCase):
    """Test cases for the AtomCounter class."""

    def test_count_atoms_positive(self):
        """Test cases for counting atoms in various molecular formulas."""
        # Test a simple molecular formula
        formula = 'H2O'
        counter = AtomCounter(formula)
        expected_atoms = {'H': 2, 'O': 1}
        self.assertEqual(counter.count_atoms(), expected_atoms)

        # Test a more complex molecular formula
        formula = 'C6H12O6'
        counter = AtomCounter(formula)
        expected_atoms = {'C': 6, 'H': 12, 'O': 6}
        self.assertEqual(counter.count_atoms(), expected_atoms)

        # Test a formula with nested parentheses
        formula = 'Na3(Fe(CN)6)2'
        counter = AtomCounter(formula)
        expected_atoms = {'Na': 3, 'Fe': 2, 'C': 12, 'N': 12}
        self.assertEqual(counter.count_atoms(), expected_atoms)

    def test_count_atoms_negative(self):
        """Test cases for handling invalid molecular formulas."""
        # Test an invalid formula with missing closing parenthesis
        formula = 'Na3(Fe(CN)6'
        counter = AtomCounter(formula)
        self.assertRaises(IndexError, counter.count_atoms)

        # Test an invalid formula with invalid characters
        formula = 'C6H12O@6'
        counter = AtomCounter(formula)
        self.assertRaises(ValueError, counter.count_atoms)


if __name__ == '__main__':
    unittest.main()
