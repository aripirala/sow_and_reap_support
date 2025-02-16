# Sow and Reap Support

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Package Management](#package-management)
- [Development Workflow](#development-workflow)
- [Troubleshooting](#troubleshooting)
- [Additional Information](#additional-information)

## Introduction
[Project description and purpose]

## Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)
- Make (recommended)

### First Time Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sow_and_reap_support
   ```

2. Create and activate the virtual environment:
   ```bash
   # Create virtual environment
   python3.11 -m venv .venv

   # Activate virtual environment
   # On Unix/macOS:
   source .venv/bin/activate
   # On Windows:
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   # Install Poetry (package manager)
   pip install poetry

   # Install project dependencies
   poetry install
   ```

   Alternatively, use the single command:
   ```bash
   make setup
   ```

4. Verify installation:
   ```bash
   # Should show the virtual environment path
   which python
   
   # Should show installed packages
   pip list
   ```

### Quick Start for Returning Users
```bash
# Activate the existing virtual environment
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Update dependencies if needed
poetry install
```

## Development Environment

### Managing Environment

1. **Activate environment**:
   ```bash
   source .venv/bin/activate  # Unix/macOS
   .venv\Scripts\activate     # Windows
   ```

2. **Deactivate environment**:
   ```bash
   deactivate
   ```

3. **Clean environment**:
   ```bash
   make clean   # Removes virtual environment and cache files
   ```

## Package Management

### Installing Packages

1. **Install a new package**:
   ```bash
   # For main dependencies
   poetry add package-name

   # For development dependencies
   poetry add --group dev package-name

   # Install specific version
   poetry add package-name==1.2.3
   ```

2. **Install from requirements.txt**:
   ```bash
   poetry add $(cat requirements.txt)
   ```

### Updating Packages

1. **Update all packages**:
   ```bash
   poetry update
   ```

2. **Update specific package**:
   ```bash
   poetry update package-name
   ```

3. **Show outdated packages**:
   ```bash
   poetry show --outdated
   ```

### Removing Packages
```bash
# Remove main dependency
poetry remove package-name

# Remove development dependency
poetry remove --group dev package-name
```

### Viewing Package Information

1. **List all installed packages**:
   ```bash
   poetry show
   ```

2. **View dependency tree**:
   ```bash
   poetry show --tree
   ```

3. **View package details**:
   ```bash
   poetry show package-name
   ```

### Package Management Best Practices

1. Always activate virtual environment before operations:
   ```bash
   source .venv/bin/activate  # Unix/macOS
   .venv\Scripts\activate     # Windows
   ```

2. **Avoid using pip install directly**:
   - Using `pip install` bypasses Poetry's dependency management
   - If you've used `pip install`:
     ```bash
     # 1. List the pip-installed package
     pip freeze | grep package-name
     
     # 2. Add it to Poetry properly
     poetry add package-name
     
     # 3. Remove the pip-installed version
     pip uninstall package-name
     
     # 4. Let Poetry install the managed version
     poetry install
     ```

3. After adding/removing packages:
   ```bash
   # Verify installation
   poetry install

   # Check for conflicts
   poetry check
   ```

4. Before committing changes:
   ```bash
   # Update lock file
   poetry lock

   # Run tests
   make test
   ```

## Development Workflow

### Contributing

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure all tests pass:
   ```bash
   make lint
   make test
   ```

3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```

4. Push to your branch and create a pull request

### Common Development Tasks

1. **Export dependencies**:
   ```bash
   poetry export -f requirements.txt --output requirements.txt
   ```

2. **Lock file management**:
   ```bash
   # Update lock file without installing
   poetry lock

   # Install from lock file
   poetry install --sync
   ```

## Troubleshooting

### Common Issues

1. **Python version mismatch**:
   - Ensure you have Python 3.9+ installed:
     ```bash
     python --version
     ```

2. **Virtual environment not activating**:
   - Check if .venv directory exists:
     ```bash
     ls .venv  # On Unix/macOS
     dir .venv  # On Windows
     ```
   - If not, recreate it:
     ```bash
     make clean
     make setup
     ```

3. **Poetry installation fails**:
   ```bash
   pip install --user poetry
   ```

4. **Dependencies conflicts**:
   ```bash
   # Show detailed dependency tree
   poetry show --tree
   ```

### Poetry Commands Reference

- **Show environment info**:
  ```bash
  poetry env info
  ```

- **List available packages**:
  ```bash
  poetry show
  ```

## Additional Information

### Project Structure
```
├── src/
│   └── sow_and_reap_support/
│       └── __init__.py
├── tests/
├── .gitignore
├── Makefile
├── poetry.toml
├── pyproject.toml
└── README.md
```

### License
[Specify your license here]

### Contact
[Your contact information or contribution guidelines]
