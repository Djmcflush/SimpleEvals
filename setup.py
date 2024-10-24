from setuptools import setup, find_packages

setup(
    name='llm-evals',
    version='1.0.0',
    author='djmcflush',
    author_email='alexander@darelabs.net',
    description='A framework for evaluating large language models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/llm-evals',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scikit-learn>=0.24.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)