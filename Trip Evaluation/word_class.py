from enum import Enum

class Dire(Enum):
    NONE = 1
    START = 2
    DEST = 3

class Impact(Enum):
    NONE = 1
    WEAK = 2
    STRONG = 3

class WordSense:
    def __init__(self, word, direction: Dire, strength: Impact):
        self.word = word
        self.direction = direction
        self.strength = strength

    def __str__(self):
        return f"Word '{self.word}' has a direction of {self.direction.name} and a {self.strength.name} strength."

    def __repr__(self):
        return f"Word '{self.word}' has a direction of {self.direction.name} and a {self.strength.name} strength."

class LinkedWordSense:
    def __init__(self, word, fixedWord, direction: Dire, strength: Impact):
        self.word = word
        self.fixedWord = fixedWord
        self.direction = direction
        self.strength = strength

    def __str__(self):
        return f"Words '{self.word}' fixed with '{self.fixedWord}' has a direction of {self.direction.name} and a {self.strength.name} strength."

    def __repr__(self):
        return f"Words '{self.word}' fixed with '{self.fixedWord}' has a direction of {self.direction.name} and a {self.strength.name} strength."
