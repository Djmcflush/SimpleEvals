import json
import logging

def load_dataset(path):
    """
    Load dataset from a JSON file.

    Args:
        path (str): Path to the dataset file.

    Returns:
        list: A list of data samples.
    """
    logging.info(f"Loading dataset from {path}")
    with open(path, 'r') as file:
        data = json.load(file)
    logging.info(f"Loaded {len(data)} samples.")
    return data

def save_results(results, path):
    """
    Save evaluation results to a JSON file.

    Args:
        results (dict): Evaluation results.
        path (str): Path to save the results.
    """
    logging.info(f"Saving results to {path}")
    with open(path, 'w') as file:
        json.dump(results, file, indent=4)
    logging.info("Results saved successfully.")