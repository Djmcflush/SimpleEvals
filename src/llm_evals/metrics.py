import numpy as np
from sklearn.metrics import accuracy_score, f1_score

class Metrics:
    def calculate_accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    def calculate_f1(self, y_true, y_pred, average='weighted'):
        return f1_score(y_true, y_pred, average=average)