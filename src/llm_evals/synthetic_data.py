from deepeval.synthesizer import Synthesizer, Evolution

class SyntheticDataGenerator:
    def __init__(self, model='gpt-4o', critic_model='gpt-4o', embedder='text-embedding-ada-002'):
        self.synthesizer = Synthesizer(
            model=model,
            critic_model=critic_model,
            embedder=embedder
        )

    def generate_from_scratch(self, scenario, task, input_format, num_initial_goldens, num_evolutions=1, evolutions=None):
        self.synthesizer.generate_goldens_from_scratch(
            scenario=scenario,
            task=task,
            input_format=input_format,
            num_initial_goldens=num_initial_goldens,
            num_evolutions=num_evolutions,
            evolutions=evolutions
        )

    def save_generated_goldens(self, file_type='json', directory='./synthetic_data'):
        self.synthesizer.save_as(file_type=file_type, directory=directory)
