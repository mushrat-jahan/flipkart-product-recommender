from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = [line.strip() for line in f.read().splitlines() if line.strip() and not line.startswith("#")]

setup(
    name="flipkart-recommender",
    version="0.1.0",
    author="Mushrat",
    description="Flipkart Product Recommender using RAG",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)