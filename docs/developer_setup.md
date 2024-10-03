# Developer Setup
This document provides instructions on how to set up the project on your local machine for development purposes.

## Prerequisites
Before you start, make sure the following tools are installed on your system:
- **Git:** Version control system to clone the project repository [Download Git](https://git-scm.com/downloads)
- **Python:** Programming language used for the project [Download Python](https://www.python.org/downloads/)

## Setup
Follow the steps below to set up the project on your local machine:

### Pre-commit hooks

To ensure the quality of the codebase, we use pre-commit hooks to run linting and formatting checks before committing the code. This will help to catch any issues early and maintain a consistent code style.

```bash
ln -s ../../scripts/pre-commit .git/hooks/pre-commit
```

## Usage
To run the project, you can use the following commands:
```bash
python fizzbuzz.py
```

## Testing
We use [Pytest](https://docs.pytest.org/en/stable/) for running unit tests. You can run the tests using the following command:
```bash
pytest
```