import argparse
import logging
from .evaluator import Evaluator

def main():
    parser = argparse.ArgumentParser(description='LLM Evals Framework')
    parser.add_argument('--model', type=str, required=True, help='Name of the model to evaluate')
    parser.add_argument('--dataset', type=str, required=True, help='Path to the dataset')
    parser.add_argument('--output', type=str, default='results.json', help='Path to save evaluation results')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    evaluator = Evaluator(model=args.model, dataset=args.dataset)
    results = evaluator.run_evaluation()
    evaluator.generate_report(results)

    from .utils import save_results
    save_results(results, args.output)
    logger.info(f"Evaluation results saved to {args.output}")

if __name__ == '__main__':
    main()