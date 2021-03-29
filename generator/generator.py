from __future__ import print_function
import random

buzz = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly', 'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boots')


def sample(l, n=1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result


def generator_buzz():
    buzz_words = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_words[0], sample(adverbs), sample(verbs), buzz_words[1]])
    return phrase.title()


if __name__ == '__main__':
    print(generator_buzz())
