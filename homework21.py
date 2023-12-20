import pytest
from AtomCounter import AtomCounter


def test_count_atoms_positive_1():
    formula = "H2O"
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2, 'O': 1}


def test_count_atoms_positive_2():
    formula = "(NaCl)2"
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'Na': 2, 'Cl': 2}


def test_count_atoms_positive_3():
    formula = "C6H12O6"
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'C': 6, 'H': 12, 'O': 6}


def test_count_atoms_negative_1():
    formula = "("
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {}


def test_count_atoms_negative_2():
    formula = "H2O)"
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2, 'O': 2}


def test_count_atoms_negative_3():
    formula = "H2[O"
    counter = AtomCounter(formula)
    atoms = counter.count_atoms()
    assert atoms == {'H': 2}


pytest.main()
