import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    def plot_metrics(self, results):
        metrics = list(results.keys())
        values = list(results.values())

        sns.barplot(x=metrics, y=values)
        plt.title('Evaluation Metrics')
        plt.ylabel('Score')
        plt.xlabel('Metrics')
        plt.ylim(0, 1)
        plt.show()