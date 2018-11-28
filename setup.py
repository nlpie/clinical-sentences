"""Sentence detection for clinical notes."""
from setuptools import setup, find_packages

setup(name='nlpie-clinical-sentences',
      version='1.0',
      packages=find_packages(),
      python_requires='>3.5.0',
      include_package_data=True,
      description='Sentence detection for clinical notes',
      author='Ben Knoll',
      author_email='benknoll@umn.edu',
      license='Apache v2.0',
      install_requires=[
          'numpy',
          'scikit_learn',
          'pyyaml',
          'h5py'
      ],
      extras_require={
          'tf': 'tensorflow',
          'tf-gpu': 'tensorflow-gpu'
      },
      zip_safe=False)
