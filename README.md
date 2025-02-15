This will:
- Remove the virtual environment
- Clear Python cache files
- Remove compiled Python files

### Updating Dependencies

1. Update `pyproject.toml` with new version requirements
2. Run:
   ```bash
   poetry update
   ```

## Troubleshooting

### Common Issues

1. **Poetry installation fails**:
   ```bash
   pip install --user poetry
   ```

2. **Virtual environment issues**:
   ```bash
   # Remove and recreate
   make clean
   make setup
   ```

3. **Dependencies conflicts**:
   ```bash
   # Show detailed dependency tree
   poetry show --tree
   ```

### Poetry Commands Reference

- **Show environment info**:
  ```bash
  poetry env info
  ```

- **List all available packages**:
  ```bash
  poetry show
  ```

- **Export requirements.txt**:
  ```bash
  poetry export -f requirements.txt --output requirements.txt
  ```

## Contributing

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

## License

[Specify your license here]

## Contact

[Your contact information or contribution guidelines]

# Sow and Reap Support

## First Time Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Make (recommended)

### Initial Setup Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sow_and_reap_support
   ```

2. Create and activate the virtual environment:
   ```bash
   # Create virtual environment
   python -m venv .venv

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

   Alternatively, you can use the single command:
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

If you've already set up the project before:

```bash
# Activate the existing virtual environment
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Update dependencies if needed
poetry install
```

### Common Issues During Setup

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

### Deactivating the Environment

When you're done working:
```bash
deactivate
```
