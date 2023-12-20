"""Homework 21: Testing AtomCounter Class"""

import pytest
from AtomCounter import AtomCounter


def test_count_atoms_positive_1():
    """Test counting atoms in a simple formula (H2O)."""
    formula = 'H2O'
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2, 'O': 1}


def test_count_atoms_positive_2():
    """Test counting atoms in a formula with parentheses and numbers ((NaCl)2)."""
    formula = '(NaCl)2'
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'Na': 2, 'Cl': 2}


def test_count_atoms_positive_3():
    """Test counting atoms in a complex formula (C6H12O6)."""
    formula = 'C6H12O6'
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'C': 6, 'H': 12, 'O': 6}


def test_count_atoms_negative_1():
    """Test counting atoms in an invalid formula (unbalanced parentheses)."""
    formula = '('
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {}


def test_count_atoms_negative_2():
    """Test counting atoms in an invalid formula (unbalanced parentheses)."""
    formula = 'H2O)'
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2, 'O': 2}


def test_count_atoms_negative_3():
    """Test counting atoms in an invalid formula (unclosed bracket)."""
    formula = 'H2[O'
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2}


pytest.main()
