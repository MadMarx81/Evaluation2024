from devine_steve.py import *

def test_devine_steve_decomposer_invalide():
    assert decomposer(10) == NONE
    assert decomposer(1000) == NONE

def test_devine_steve_decomposer_valide():
    assert decomposer(999) == (9,9,9)
    assert decomposer(100) == (1,0,0)


def test_devine_steve_divisible():
    assert divisible(999) == True
    assert divisible(900) == True
    assert divisible(1000) == False


def test_devine_steve_somme():
    assert somme(1,3,2) == True
    assert somme(2,3,1) == True
    assert somme(2,4,2) == True

    assert somme(2,2,2) == None
    assert somme(1,9,9) == None 
