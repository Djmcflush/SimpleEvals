from .utils import load_dataset

class DataHandler:
    def __init__(self, dataset_path):
        self.dataset = load_dataset(dataset_path)

    def get_samples(self):
        return self.dataset

    def get_sample(self, index):
        return self.dataset[index]