import unittest
from generator import generator


def test_sample_single_word():
    l = ('foo', 'far', 'foobar')
    word = generator.sample(l)
    assert word in l


def test_sample_multiple_words():
    l = ('foo', 'bar', 'foobar')
    word = generator.sample(l, 2)
    assert len(word) == 2
    assert word[0] in l
    assert word[1] in l
    assert word[0] is not word[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generator_buzz()
    assert len(phrase.split()) >= 5
