import logging
from .metrics import Metrics
from .visualization import Visualization

class Evaluator:
    def __init__(self, model, dataset):
        self.model = model
        self.dataset = dataset
        self.metrics = Metrics()
        self.visualization = Visualization()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run_evaluation(self):
        self.logger.info(f"Starting evaluation for model: {self.model} on dataset: {self.dataset}")
        results = {}
        # Placeholder for actual evaluation logic
        results['accuracy'] = self.metrics.calculate_accuracy()
        results['f1_score'] = self.metrics.calculate_f1()
        self.logger.info("Evaluation completed.")
        return results

    def generate_report(self, results):
        self.logger.info("Generating report.")
        self.visualization.plot_metrics(results)
        self.logger.info("Report generated.")