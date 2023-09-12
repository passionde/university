import os

import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB


def get_rows(dir_name: str) -> list[str]:
    result = []
    file_names = os.listdir(dir_name)
    for name in file_names:
        with open(f"{dir_name}/{name}") as f:
            result.append(f.read())
    return result


def get_words(words: set[str]) -> dict[str:int]:
    result = {}
    for idx, word in enumerate(words):
        result[word] = idx
    return result


if __name__ == "__main__":
    negative_reviews = get_rows("data/movie/neg")
    positive_reviews = get_rows("data/movie/pos")

    Y = np.array([1] * len(positive_reviews) + [0] * len(negative_reviews))

    reviews = positive_reviews + negative_reviews
    words = get_words(set(" ".join(reviews).split()))

    X = np.zeros((len(reviews), len(words)))

    seq: str
    for i, seq in enumerate(reviews):
        for j in seq.split():
            X[i, words.get(j)] = 1

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=0
    )

    clf = BernoulliNB()
    clf.fit(X_train, Y_train)

    Y_pred = clf.predict(X_test)
    accuracy = metrics.accuracy_score(Y_test, Y_pred)
    print(f"Accuracy: {accuracy}")
