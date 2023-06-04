from setuptools import setup, find_packages

# Read the contents of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define the setup configuration
setup(
    name="amaryllis-ai",
    version="1.0.0",
    author="FultonArtProductions",
    author_email="Admin@fultonarts.cp,",
    description="A versatile AI chatbot named Amaryllis AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/amaryllis-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add your project dependencies here with version numbers, for example:
        "numpy>=1.19.5",
        "pandas>=1.1.5",
        "tensorflow==2.3.1",
        "keras==2.3.1",
        "nltk>=3.5",
        "spacy>=3.0.0",
        "gensim>=3.8.3",
        "flask>=1.1.2",
        "django>=3.1.7",
        "PyQt5>=5.15.2",
        "wxPython>=4.1.1",
        "tkinter>=0.0.0",  # No version number is needed for tkinter, as it's part of the Python standard library
        # ...
    ],
    extras_require={
        "dev": [
            # Add development dependencies here, for example:
            "pytest>=6.2.2",
            "black>=20.8b1",
            "flake8>=3.8.4",
            "mypy>=0.812",
            # ...
        ],
    },
    entry_points={
        "console_scripts": [
            # Add any command-line scripts here, for example:
            "amaryllis-ai=main:main",  # Adjust this according to your project structure
        ],
    },
)