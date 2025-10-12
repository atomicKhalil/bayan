# Getting Started with بيان bayan

Welcome! This guide will help you get **bayan** up and running in minutes.

---

## What You Need

- Python 3.8 or higher
- A research paper in PDF format
- 5 minutes of your time

---

## Step 1: Install Dependencies

Open your terminal and run:

```bash
pip install PyMuPDF pdfminer.six
```

This installs the two required libraries for PDF parsing.

---

## Step 2: Navigate to bayan

```bash
cd "c:\Users\khali\OneDrive\Documents\libraries"
```

Or wherever you cloned/downloaded bayan.

---

## Step 3: Install bayan

```bash
pip install -e .
```

This installs bayan in "editable" mode, so you can modify the code if needed.

---

## Step 4: Test the Installation

```bash
python -c "from bayan import Paper; print('✓ bayan is ready!')"
```

You should see: `✓ bayan is ready!`

---

## Step 5: Your First Extraction

Create a file called `test.py`:

```python
from bayan import Paper

# Replace with your PDF path
paper = Paper("research_paper.pdf")

# Extract metadata
meta = paper.extract_metadata()
print(f"Title: {meta['title']}")
print(f"Authors: {', '.join(meta['authors'])}")
print(f"Year: {meta['year']}")

# Get the abstract
sections = paper.extract_sections()
abstract = sections.get('abstract', 'Not found')
print(f"\nAbstract:\n{abstract[:300]}...")

# Export to JSON
paper.export("json", "paper_data.json")
print("\n✓ Exported to paper_data.json")

# Don't forget to close
paper.close()
```

Run it:

```bash
python test.py
```

---

## Step 6: Explore the Output

Check the generated `paper_data.json`:

```bash
# Windows
notepad paper_data.json

# Mac/Linux
cat paper_data.json
```

You should see structured data with metadata, sections, references, tables, and figures!

---

## What's Next?

### Try Different Exports

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Export as Markdown (readable)
paper.export("markdown", "paper.md")

# Export as CSV (for spreadsheets)
paper.export("csv", "paper.csv")

# Export as plain text
paper.export("txt", "paper.txt")

paper.close()
```

### Extract Specific Elements

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Just get metadata
meta = paper.extract_metadata()

# Just get references
refs = paper.extract_references()

# Just get tables
tables = paper.extract_tables()

# Get everything at once
data = paper.extract_all()

paper.close()
```

### Use Context Manager (Recommended)

```python
from bayan import Paper

with Paper("paper.pdf") as paper:
    data = paper.extract_all()
    paper.export("json", "output.json")
# Automatically closed!
```

### Process Multiple Papers

```python
from bayan import Paper
import glob

# Get all PDFs in a folder
papers = glob.glob("papers/*.pdf")

for pdf_path in papers:
    with Paper(pdf_path) as paper:
        meta = paper.extract_metadata()
        print(f"Processed: {meta['title']}")
        paper.export("json", f"{pdf_path}.json")
```

---

## Optional: Enable AI Features

If you want to use summarization and classification:

### Install OpenAI

```bash
pip install openai
```

### Use in Code

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Enable OpenAI (you need an API key)
paper.enable_llm(provider="openai", api_key="sk-your-key-here")

# Summarize a section
summary = paper.summarize("methodology", max_length=150)
print(summary)

# Classify the paper
classification = paper.classify()
print(f"Type: {classification['paper_type']}")
print(f"Domain: {classification['domain']}")

paper.close()
```

### Other LLM Providers

```python
# Anthropic Claude
paper.enable_llm(provider="anthropic", api_key="sk-ant-...")

# HuggingFace (requires: pip install transformers torch)
paper.enable_llm(provider="huggingface", model_name="facebook/bart-large-cnn")

# Local Ollama
paper.enable_llm(provider="local", base_url="http://localhost:11434", model_name="llama2")
```

---

## Examples in Action

Check out [example.py](example.py) for complete working examples:

```bash
python example.py
```

This will show you:
- Basic extraction
- LLM integration
- Batch processing
- Advanced features

---

## Common Issues

### "PDF file not found"
Make sure the PDF path is correct. Use absolute paths if needed:

```python
paper = Paper("c:/path/to/your/paper.pdf")
```

### "Module not found"
Make sure you installed dependencies:

```bash
pip install PyMuPDF pdfminer.six
```

### "No sections detected"
Some papers have unusual layouts. Try:

```python
sections = paper.extract_sections()
print(sections.keys())  # See what was detected
```

### Poor quality extraction
- Make sure the PDF is text-based (not a scanned image)
- Try a different PDF
- OCR support is coming in v0.3.0

---

## Learn More

- 📖 **Full Documentation:** [README.md](README.md)
- ⚡ **Quick Reference:** [QUICKSTART.md](QUICKSTART.md)
- 🧪 **Run Tests:** `pytest tests/`
- 🤝 **Contribute:** [CONTRIBUTING.md](CONTRIBUTING.md)
- 📊 **Project Overview:** [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

---

## Need Help?

- Open an issue on GitHub
- Check existing issues
- Read the documentation

---

## Success Checklist

- [ ] Dependencies installed (`PyMuPDF`, `pdfminer.six`)
- [ ] bayan installed (`pip install -e .`)
- [ ] Test script runs successfully
- [ ] Can extract metadata from a paper
- [ ] Can export to JSON
- [ ] Explored example.py

---

**🎉 Congratulations! You're ready to use bayan!**

Now go extract some papers and bring clarity to research!

---

**بيان bayan** — *Bring clarity to research papers.*
