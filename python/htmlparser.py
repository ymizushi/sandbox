#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

class TestMerge(unittest.TestCase):
    def test_solve(self):
        input    = 1
        expected = "1"
        self.assertEqual(str(input), expected)

class Element:
    def __init__(self, attribute, child):
        self.attribute = attribute
        self.child = child

class ElementBuilder:
    def __init__(self, token):
        pass

class Token:
    START_TAG = "START_TAG"
    END_TAG = "END_TAG"
    START_AND_END_TAG = "START_AND_END_TAG"
    VALUE = "VALUE"

    def __init__(self, token_string):
        self.token_string

    @property
    def type(self):
        pass

class Tokenizer:
    start_tag_re = re.compile('<([^\/]*)\s+(\w+)\=(\w+)\s*[^\/]*>')
    end_tag_re = re.compile('<\/\s*(\w+)>')
    start_and_end_tag_re = re.compile('<([\w^\/]*)(\s+\w+\=\w+)*\s*\/>')

    def __init__(self, sentence):
        self.sentence = sentence
    def tokenize(self):
        token = ''
        while(1):
            char = self.sentence.getChar()
            if char:
                token += char
                if self.start_tag_re.match(token):
                    pass
                elif char =='>':
                    pass
                elif char == '':
                    pass
                pass
            else:
                return token

if __name__ == '__main__':
    unittest.main()
