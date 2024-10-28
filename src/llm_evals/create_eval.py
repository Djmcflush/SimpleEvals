from typing import Optional, List

class CustomEval:
    def __init__(self, input: str, actual_output: str, expected_output: Optional[str] = None,
                 context: Optional[List[str]] = None, retrieval_context: Optional[List[str]] = None):
        self.input = input
        self.actual_output = actual_output
        self.expected_output = expected_output
        self.context = context
        self.retrieval_context = retrieval_context
