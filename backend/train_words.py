from random import shuffle

from loading_words import LoadWords


class TrainWords:
    def __init__(self):
        self._words = LoadWords("words.txt").get_words()

    def train(self):
        score = {}
        words = {i: self._words[i] for i in shuffle(self._words)}
        for word in self._words.keys():
            score[word] = 0

        while not all(sc == 3 for sc in score.values()):
            for word in self._words.keys():
                if score[word] == 3:
                    continue
                result = yield word
                if result in words[word]:
                    score[word] += 1


if __name__ == '__main__':
    train = TrainWords().train()
    next(train)
    for _ in train:
        train_word = next(train)
        print(train_word)
        word = input()
        train.send(word)
