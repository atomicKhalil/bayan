# بيان bayan - Architecture Documentation

This document explains the internal architecture and design decisions of **bayan**.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Paper (API)                          │
│                    Main User Interface                       │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                  │
           ▼                  ▼                  ▼
┌──────────────────┐  ┌──────────────┐  ┌──────────────────┐
│   PDFParser      │  │  TextCleaner │  │   LLMClient      │
│  (parser.py)     │  │ (cleaner.py) │  │ (llm_client.py)  │
│                  │  │              │  │                  │
│ • PyMuPDF        │  │ • Normalize  │  │ • OpenAI        │
│ • Text Extract   │  │ • Unicode    │  │ • Anthropic     │
│ • Layout Info    │  │ • Ligatures  │  │ • HuggingFace   │
└──────────────────┘  └──────────────┘  └──────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│                     Extractors Layer                         │
├──────────────────┬──────────────────┬──────────────────────┤
│  PaperExtractor  │ TableExtractor   │    TextUtils        │
│  (extractor.py)  │   (tables.py)    │    (utils.py)       │
│                  │                  │                      │
│ • Metadata       │ • Tables         │ • DOI/arXiv         │
│ • Sections       │ • Figures        │ • Regex Patterns    │
│ • References     │ • Equations      │ • Heuristics        │
└──────────────────┴──────────────────┴──────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│                   PaperExporter                              │
│                   (exporter.py)                              │
│                                                              │
│  • JSON    • Markdown    • CSV    • TXT    • BibTeX        │
└─────────────────────────────────────────────────────────────┘
```

---

## Module Overview

### 1. Paper (`__init__.py`)

**Purpose:** Main API and orchestration layer

**Responsibilities:**
- Provide simple, unified interface
- Coordinate between modules
- Manage resource lifecycle
- Cache extracted data

**Key Methods:**
- `extract_metadata()` - Get paper metadata
- `extract_sections()` - Get sections
- `extract_references()` - Get citations
- `extract_tables()` - Get tables
- `extract_figures()` - Get figures
- `export()` - Export to formats
- `enable_llm()` - Enable AI features

**Design Pattern:** Facade Pattern

```python
class Paper:
    def __init__(self, pdf_path):
        self.parser = PDFParser(pdf_path)
        self.extractor = PaperExtractor(self.parser)
        self.table_extractor = TableExtractor(self.parser)
        self.exporter = PaperExporter()
        self.llm_client = None
```

---

### 2. PDFParser (`parser.py`)

**Purpose:** Low-level PDF parsing and text extraction

**Dependencies:**
- PyMuPDF (fitz) - Main PDF library
- pdfminer.six - Fallback/alternative

**Key Features:**
- Page-by-page text extraction
- Block-level layout information
- Font metadata (size, style)
- Image extraction
- Table of contents parsing
- Text search

**Design Pattern:** Wrapper Pattern

```python
class PDFParser:
    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)
        self.cleaner = TextCleaner()

    def get_page_text(self, page_num) -> str
    def get_page_blocks(self, page_num) -> List[Dict]
    def get_text_with_fonts(self, page_num) -> List[Dict]
```

**Performance:**
- Lazy loading of pages
- Minimal memory footprint
- Caching where appropriate

---

### 3. PaperExtractor (`extractor.py`)

**Purpose:** Extract structured information from raw PDF text

**Responsibilities:**
- Metadata extraction (title, authors, etc.)
- Section detection and segmentation
- Reference parsing
- Abstract extraction

**Extraction Strategies:**

#### Title Extraction (Multi-Strategy)
1. PDF metadata (if available)
2. Largest font size on first page
3. First lines heuristics
4. Validation with `is_likely_title()`

#### Author Extraction
1. Pattern matching after title
2. Affiliation marker removal
3. Delimiter splitting (comma, "and")
4. Validation with `is_likely_author()`

#### Section Detection
1. Regex pattern matching
2. Layout analysis (headers)
3. Standard section names mapping
4. Custom section preservation

**Design Pattern:** Strategy Pattern

---

### 4. TableExtractor (`tables.py`)

**Purpose:** Extract tables, figures, and equations

**Responsibilities:**
- Table caption detection
- Table content parsing
- Figure caption extraction
- Image metadata extraction
- Equation extraction

**Table Parsing:**
```
1. Find caption (regex)
2. Locate table content (nearby text)
3. Detect delimiters (tabs, spaces, pipes)
4. Parse rows and columns
5. Export to structured format
```

**Challenges:**
- Varied table layouts
- Multi-column tables
- Merged cells (partial support)
- Complex nested tables

---

### 5. TextCleaner (`cleaner.py`)

**Purpose:** Normalize and clean extracted text

**Features:**
- Ligature replacement (ﬁ → fi)
- Unicode normalization
- Hyphenation handling (line-break words)
- Whitespace normalization
- Bullet point normalization
- Reference marker removal

**Cleaning Pipeline:**
```
Raw Text
   ↓
Ligature Fix
   ↓
Unicode Normalization
   ↓
Hyphenation Fix
   ↓
Whitespace Normalization
   ↓
Clean Text
```

**Preserves:**
- Paragraph structure
- Sentence boundaries
- Important spacing

---

### 6. PaperExporter (`exporter.py`)

**Purpose:** Export data to various formats

**Supported Formats:**
- **JSON** - Full structured data
- **Markdown** - Human-readable
- **CSV** - Flattened for analysis
- **TXT** - Plain text
- **BibTeX** - Citations

**Export Strategy:**
```python
def export(data, format, path):
    if format == "json":
        return to_json(data, path)
    elif format == "markdown":
        return to_markdown(data, path)
    # ... etc
```

**Design Pattern:** Strategy Pattern

---

### 7. TextUtils & RegexPatterns (`utils.py`)

**Purpose:** Shared utilities and regex patterns

**Components:**

#### RegexPatterns
- DOI patterns
- arXiv ID patterns
- Email patterns
- URL patterns
- Year patterns
- Section headers
- Reference patterns
- Table/figure captions

#### TextUtils
- `extract_dois(text)` - Find DOIs
- `extract_years(text)` - Find years
- `extract_emails(text)` - Find emails
- `split_by_sections(text)` - Split into sections
- `is_likely_title(text)` - Heuristic validation
- `is_likely_author(text)` - Heuristic validation

#### FormatUtils
- `format_author_list()` - Pretty author names
- `format_citation()` - APA/MLA/Chicago
- `bytes_to_human_readable()` - File sizes

---

### 8. LLMClient (`llm_client.py`)

**Purpose:** Optional AI-powered features

**Supported Providers:**
- OpenAI (GPT models)
- Anthropic (Claude)
- HuggingFace (BART, T5, etc.)
- Local (Ollama, custom APIs)

**Features:**
- Text summarization
- Paper classification
- Domain detection
- Contribution extraction

**Provider Interface:**
```python
class LLMClient:
    def __init__(self, provider, **config)
    def summarize(text, max_length) -> str
    def classify_paper(metadata, sections) -> Dict
    def extract_key_contributions(sections) -> List[str]
```

**Design Pattern:** Adapter Pattern

---

## Data Flow

### Extraction Pipeline

```
PDF File
   ↓
PDFParser.get_full_text()
   ↓
TextCleaner.clean()
   ↓
PaperExtractor.extract_metadata()
PaperExtractor.extract_sections()
PaperExtractor.extract_references()
TableExtractor.extract_tables()
TableExtractor.extract_figures()
   ↓
Structured Data (Dict)
   ↓
PaperExporter.export()
   ↓
JSON / Markdown / CSV / TXT
```

### LLM Pipeline (Optional)

```
Extracted Data
   ↓
LLMClient.summarize()
   ↓
API Call (OpenAI/Anthropic/Local)
   ↓
Summary Text
```

---

## Design Decisions

### 1. Why PyMuPDF?

**Pros:**
- Fast and efficient
- Good layout preservation
- Active development
- Rich metadata support

**Cons:**
- Some complex layouts challenging
- AGPL license (wrapper approach mitigates)

**Alternative:** pdfminer.six (included as dependency)

### 2. Multiple Extraction Strategies

Different papers have different layouts. We use:
- Primary strategy (most papers)
- Fallback strategies (unusual cases)
- Heuristic validation (filter false positives)

### 3. Caching

Extracted data is cached to avoid re-processing:
```python
if self._metadata is None:
    self._metadata = self.extractor.extract_metadata()
return self._metadata
```

Use `force_refresh=True` to bypass cache.

### 4. Modular Design

Each module is independent:
- Can be used standalone
- Easy to test
- Easy to extend
- Clear responsibilities

### 5. Optional Dependencies

Core features work without LLM libraries:
```python
try:
    from openai import OpenAI
except ImportError:
    raise ImportError("Install openai: pip install openai")
```

---

## Performance Considerations

### Memory

- Pages loaded on-demand
- Cached data stored in memory
- PDF closed explicitly with `close()`

### Speed

- Typical paper: 1-5 seconds
- Mostly I/O bound (reading PDF)
- LLM operations: 2-10 seconds (API dependent)

### Optimization Opportunities

1. **Parallel processing** for batch operations
2. **Incremental parsing** for large papers
3. **Smart caching** of regex matches
4. **Lazy evaluation** of expensive operations

---

## Error Handling

### Graceful Degradation

If extraction fails:
- Return empty/default values
- Continue with other extractions
- Log warnings (future)

Example:
```python
def _extract_title(self, ...):
    try:
        # Strategy 1
        ...
    except:
        try:
            # Strategy 2
            ...
        except:
            return "Unknown Title"
```

### User-Facing Errors

Clear error messages:
```python
if not self.pdf_path.exists():
    raise FileNotFoundError(f"PDF file not found: {pdf_path}")
```

---

## Testing Strategy

### Unit Tests
- Individual module testing
- Mock PDF data
- Regex pattern validation

### Integration Tests
- Full pipeline testing
- Real PDF fixtures
- Export validation

### Example:
```python
def test_metadata_extraction():
    paper = Paper("test.pdf")
    meta = paper.extract_metadata()
    assert "title" in meta
    assert isinstance(meta["authors"], list)
```

---

## Future Architecture Enhancements

### Version 0.2.0
- CLI module (`cli.py`)
- Batch processing module
- Progress tracking

### Version 0.3.0
- OCR module for scanned PDFs
- Citation graph module
- Enhanced table parser

### Version 1.0.0
- Web API module
- Plugin system
- Caching layer (Redis/file)

---

## Code Quality

### Style
- PEP 8 compliant
- Black formatted (line length: 100)
- Type hints throughout

### Documentation
- Docstrings for all public methods
- Google-style format
- Usage examples

### Maintainability
- Clear module boundaries
- Minimal coupling
- High cohesion
- Single Responsibility Principle

---

## Conclusion

**bayan** is designed to be:
- **Simple** - Easy to use API
- **Robust** - Multiple strategies, graceful degradation
- **Modular** - Independent, reusable components
- **Extensible** - Easy to add features
- **Performant** - Fast enough for most use cases

The architecture balances simplicity with flexibility, making it suitable for both quick scripts and production systems.

---

**بيان bayan** — *Architecture for clarity.*
