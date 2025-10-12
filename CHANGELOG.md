# Changelog

All notable changes to **bayan** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- CLI implementation
- Batch processing support
- OCR for scanned PDFs
- Citation graph extraction
- Web interface
- arXiv direct download

## [0.1.0] - 2025-01-XX

### Added
- Initial release of bayan
- Core PDF parsing with PyMuPDF
- Metadata extraction (title, authors, affiliations, DOI, year)
- Section detection (abstract, introduction, methodology, results, etc.)
- Reference parsing (numbered and author-year formats)
- Table extraction with captions
- Figure extraction with captions
- Text cleaning and normalization
- Export to JSON, Markdown, CSV, and TXT formats
- BibTeX export for citations
- Optional LLM integration:
  - OpenAI support
  - Anthropic Claude support
  - HuggingFace models support
  - Local model support (Ollama)
- Summarization capabilities
- Paper classification (type and domain)
- Context manager support
- Comprehensive documentation
- Example scripts
- Basic test suite

### Core Modules
- `parser.py` - PDF parsing and text extraction
- `extractor.py` - Metadata and section extraction
- `tables.py` - Table and figure extraction
- `cleaner.py` - Text normalization
- `exporter.py` - Multi-format export
- `utils.py` - Utilities and regex patterns
- `llm_client.py` - Optional LLM integration

### Documentation
- README with comprehensive examples
- Quick start guide
- Contributing guidelines
- MIT License
- Example usage scripts

## Version History

### Version Naming
- **0.1.x** - Initial development releases
- **0.2.x** - CLI and batch processing
- **0.3.x** - Advanced features (OCR, graphs)
- **1.0.0** - First stable release

---

## Guidelines for Future Releases

### Adding to CHANGELOG
When making changes, add them under `[Unreleased]` using these categories:

- **Added** - New features
- **Changed** - Changes to existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security improvements

### Release Process
1. Update version in `__init__.py`
2. Update version in `setup.py` and `pyproject.toml`
3. Move unreleased changes to new version section
4. Add release date
5. Create git tag: `git tag v0.1.0`
6. Build and publish to PyPI

---

**بيان bayan** — Bring clarity to research papers.
