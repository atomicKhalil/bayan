# Quick Start Guide

Get started with **bayan** in 5 minutes!

## Installation

```bash
pip install PyMuPDF pdfminer.six
```

Then navigate to the bayan directory and install in development mode:

```bash
cd bayan
pip install -e .
```

## Your First Extraction

Create a file `test_bayan.py`:

```python
from bayan import Paper

# Load your paper
paper = Paper("my_paper.pdf")

# Extract metadata
meta = paper.extract_metadata()
print(f"Title: {meta['title']}")
print(f"Authors: {', '.join(meta['authors'])}")
print(f"Year: {meta['year']}")

# Get the abstract
sections = paper.extract_sections()
print(f"\nAbstract:\n{sections.get('abstract', 'Not found')}")

# Export everything to JSON
paper.export("json", "paper_data.json")
print("\n✓ Exported to paper_data.json")

paper.close()
```

Run it:

```bash
python test_bayan.py
```

## What Can You Extract?

### Metadata
- Title
- Authors
- Affiliations
- DOI / arXiv ID
- Publication year
- Keywords

### Content
- Abstract
- Introduction
- Methodology
- Results
- Discussion
- Conclusion
- References

### Structured Elements
- Tables (with captions and content)
- Figures (with captions)
- Equations

## Export Formats

```python
from bayan import Paper

paper = Paper("paper.pdf")

# JSON - Full structured data
paper.export("json", "paper.json")

# Markdown - Readable format
paper.export("markdown", "paper.md")

# CSV - Flattened data
paper.export("csv", "paper.csv")

# Plain text - Simple format
paper.export("txt", "paper.txt")
```

## Context Manager

Use with context manager for automatic cleanup:

```python
from bayan import Paper

with Paper("paper.pdf") as paper:
    data = paper.extract_all()
    paper.export("json", "output.json")
# Automatically closed
```

## Optional: AI-Powered Features

To enable summarization and classification:

```bash
pip install openai  # or anthropic
```

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Enable OpenAI
paper.enable_llm(provider="openai", api_key="sk-...")

# Summarize a section
summary = paper.summarize("methodology", max_length=150)
print(summary)

# Classify the paper
classification = paper.classify()
print(f"Type: {classification['paper_type']}")
print(f"Domain: {classification['domain']}")
```

## Common Use Cases

### 1. Extract Metadata for Bibliography

```python
from bayan import Paper
import glob
import json

papers = glob.glob("papers/*.pdf")
bibliography = []

for pdf in papers:
    paper = Paper(pdf)
    meta = paper.extract_metadata()
    bibliography.append({
        "title": meta["title"],
        "authors": meta["authors"],
        "year": meta["year"],
        "doi": meta.get("doi")
    })
    paper.close()

with open("bibliography.json", "w") as f:
    json.dump(bibliography, f, indent=2)
```

### 2. Extract All Tables

```python
from bayan import Paper

paper = Paper("paper.pdf")
tables = paper.extract_tables()

for table in tables:
    print(f"\nTable {table['number']}: {table['caption']}")

    # Export to CSV
    csv_data = paper.table_extractor.export_table_to_csv(table["number"])
    with open(f"table_{table['number']}.csv", "w") as f:
        f.write(csv_data)

paper.close()
```

### 3. Create a Summary Document

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Get key information
meta = paper.extract_metadata()
sections = paper.extract_sections()

# Create summary
summary = f"""
# {meta['title']}

**Authors:** {', '.join(meta['authors'])}
**Year:** {meta['year']}

## Abstract
{sections.get('abstract', 'N/A')}

## Key Sections
"""

for section_name in ['introduction', 'methodology', 'results', 'conclusion']:
    if section_name in sections:
        summary += f"\n### {section_name.title()}\n"
        summary += sections[section_name][:300] + "...\n"

with open("summary.md", "w") as f:
    f.write(summary)

paper.close()
```

## Troubleshooting

### PDFs won't parse
- Ensure the PDF is not encrypted
- Try updating PyMuPDF: `pip install --upgrade PyMuPDF`

### Missing sections
- Some papers have non-standard layouts
- Check `sections.keys()` to see what was detected
- Sections may be under different names

### Poor quality extraction
- Scanned PDFs (images) may not extract well
- OCR is not currently supported (planned feature)

## Next Steps

- Read the full [README.md](README.md)
- Check out [example.py](example.py) for more examples
- Star the repo and contribute!

## Need Help?

- File an issue on GitHub
- Check the documentation
- Join discussions

---

**بيان bayan** — Bring clarity to research papers.
