from setuptools import setup, find_packages

setup(name="demo_service",
      version="0.1",
      package_dir={'': 'src'}, # tell distutils packages are under `src`
      packages=find_packages('src'))