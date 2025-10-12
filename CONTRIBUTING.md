# Contributing to bayan

Thank you for your interest in contributing to **bayan**! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/atomicKhalil/bayan.git
   cd bayan
   ```
3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```
4. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv
- Git

### Install Dependencies

```bash
# Core dependencies
pip install -r requirements.txt

# Development dependencies
pip install pytest black flake8 mypy

# Optional LLM dependencies
pip install openai anthropic transformers torch
```

### Run Tests

```bash
pytest tests/ -v
```

### Code Formatting

We use Black for code formatting:

```bash
black bayan/
```

### Linting

```bash
flake8 bayan/
```

### Type Checking

```bash
mypy bayan/
```

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Check if the issue already exists
- Include:
  - Python version
  - bayan version
  - Steps to reproduce
  - Expected vs actual behavior
  - Sample PDF (if possible)

### Suggesting Features

- Open an issue with the label "enhancement"
- Describe the feature and use case
- Explain why it would be useful
- Consider implementation complexity

### Submitting Code

1. **Write clear, documented code**
   - Follow PEP 8 style guide
   - Add docstrings to functions/classes
   - Include type hints where appropriate

2. **Add tests**
   - Write tests for new functionality
   - Ensure existing tests pass
   - Aim for good coverage

3. **Update documentation**
   - Update README if needed
   - Add docstrings
   - Update CHANGELOG.md

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes
   - Link related issues

## Coding Standards

### Style Guide

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Use meaningful variable names
- Keep functions focused and small

### Documentation

- Add docstrings to all public functions/classes
- Use Google-style docstrings:
  ```python
  def extract_metadata(self) -> Dict:
      """
      Extract paper metadata.

      Returns:
          Dictionary containing metadata fields

      Raises:
          ValueError: If PDF is invalid
      """
  ```

### Testing

- Write unit tests for new features
- Use pytest fixtures for common setup
- Mock external dependencies (APIs, files)
- Test edge cases

### Commit Messages

Use clear, descriptive commit messages:

- `Add: New feature description`
- `Fix: Bug fix description`
- `Update: Changes to existing feature`
- `Docs: Documentation updates`
- `Test: Test additions/changes`
- `Refactor: Code restructuring`

## Project Structure

```
bayan/
├── __init__.py          # Main Paper interface
├── parser.py            # PDF parsing
├── extractor.py         # Metadata/section extraction
├── tables.py            # Table/figure extraction
├── cleaner.py           # Text normalization
├── exporter.py          # Export functionality
├── utils.py             # Shared utilities
└── llm_client.py        # LLM integration

tests/
├── test_basic.py        # Basic tests
└── fixtures/            # Test PDFs

examples/
└── example.py           # Usage examples
```

## Areas for Contribution

We especially welcome contributions in these areas:

### High Priority
- [ ] CLI implementation (bayan command)
- [ ] Better table parsing for complex layouts
- [ ] Support for scanned PDFs (OCR)
- [ ] More robust section detection

### Medium Priority
- [ ] Citation graph extraction
- [ ] PDF generation from extracted data
- [ ] Web interface
- [ ] arXiv direct download support

### Low Priority
- [ ] Multi-language support
- [ ] Advanced figure analysis
- [ ] Batch processing optimizations
- [ ] Plugin system

## Code Review Process

1. All submissions require review
2. Maintainers will review your PR
3. Address feedback promptly
4. Once approved, we'll merge your PR

## Questions?

- Open an issue for questions
- Use GitHub Discussions for broader topics
- Tag maintainers if urgent: @atomicKhalil

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to **bayan**! Your help makes research more accessible to everyone.
