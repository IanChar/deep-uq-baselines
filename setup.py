import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="deep_uq_baselines", # Replace with your own username
    version="1.0.0",
    author="Willie Neiswanger, Youngseog Chung, Ian Char",
    author_email="willie.neiswanger@gmail.com",
    description=("Simple implementations for deep models.."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uncertainty-toolbox/deep-uq-baselines",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
