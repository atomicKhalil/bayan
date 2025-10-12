"""
Simple example demonstrating ALL bayan features.

Instructions:
1. Place your PDF file in the same directory
2. Update the PDF filename below
3. Run: python simple_example.py
"""

from bayan import Paper

# =============================================================================
# CONFIGURATION
# =============================================================================
PDF_FILE = "test_paper.pdf"  # Change this to your PDF filename

# =============================================================================
# LOAD PAPER
# =============================================================================
print("=" * 80)
print("BAYAN - Complete Feature Demo")
print("=" * 80)

paper = Paper(PDF_FILE)
print(f"\n✓ Loaded: {PDF_FILE}")
print(f"  Pages: {paper.parser.page_count}")

# =============================================================================
# 1. EXTRACT METADATA
# =============================================================================
print("\n" + "=" * 80)
print("1. METADATA EXTRACTION")
print("=" * 80)

meta = paper.extract_metadata()

print(f"\nTitle: {meta['title']}")
print(f"Authors: {', '.join(meta['authors'][:3])}{'...' if len(meta['authors']) > 3 else ''}")
print(f"Year: {meta.get('year', 'N/A')}")
print(f"DOI: {meta.get('doi', 'N/A')}")
print(f"arXiv ID: {meta.get('arxiv_id', 'N/A')}")
print(f"Total Authors: {len(meta['authors'])}")
print(f"Affiliations: {len(meta.get('affiliations', []))}")
print(f"Keywords: {', '.join(meta.get('keywords', ['None'])[:5])}")

# =============================================================================
# 2. EXTRACT SECTIONS
# =============================================================================
print("\n" + "=" * 80)
print("2. SECTION EXTRACTION")
print("=" * 80)

sections = paper.extract_sections()

print(f"\nFound {len(sections)} sections:")
for section_name, content in sections.items():
    print(f"  - {section_name}: {len(content)} characters")

# Show abstract
if 'abstract' in sections:
    print(f"\nAbstract Preview:")
    print(f"{sections['abstract'][:300]}...")

# =============================================================================
# 3. EXTRACT REFERENCES
# =============================================================================
print("\n" + "=" * 80)
print("3. REFERENCE EXTRACTION")
print("=" * 80)

references = paper.extract_references()

print(f"\nFound {len(references)} references")
if references:
    print(f"\nFirst 3 references:")
    for ref in references[:3]:
        print(f"  [{ref.get('id')}] {ref.get('text', '')[:80]}...")

# =============================================================================
# 4. EXTRACT TABLES (Basic)
# =============================================================================
print("\n" + "=" * 80)
print("4. TABLE EXTRACTION (Basic)")
print("=" * 80)

tables = paper.extract_tables()

print(f"\nFound {len(tables)} tables:")
for table in tables:
    print(f"  Table {table['number']}: {table['caption'][:60]}...")
    print(f"    - Page: {table.get('page', 'N/A')}")
    print(f"    - Rows: {len(table['content'])}")

# =============================================================================
# 5. EXTRACT TABLES AS DATAFRAMES (NEW FEATURE!)
# =============================================================================
print("\n" + "=" * 80)
print("5. TABLES AS PANDAS DATAFRAMES (NEW!)")
print("=" * 80)

try:
    # Get all tables as DataFrames
    tables_df = paper.table_extractor.get_all_tables_as_dataframes()

    print(f"\n✓ Converted {len(tables_df)} tables to DataFrames\n")

    for table_num, df in tables_df.items():
        print(f"Table {table_num}:")
        print(f"  Caption: {df.attrs.get('caption', 'N/A')[:60]}...")
        print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"  Page: {df.attrs.get('page', 'N/A')}")

        # Save to CSV
        csv_filename = f"table_{table_num}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"  ✓ Saved to: {csv_filename}")

        # Show preview
        print(f"  Preview:\n{df.head(2)}\n")

except ImportError:
    print("\n✗ pandas not installed. Install with: pip install pandas")

# =============================================================================
# 6. EXTRACT FIGURES (Basic)
# =============================================================================
print("\n" + "=" * 80)
print("6. FIGURE EXTRACTION (Basic)")
print("=" * 80)

figures = paper.extract_figures()

print(f"\nFound {len(figures)} figures:")
for figure in figures:
    print(f"  Figure {figure['number']}: {figure['caption'][:60]}...")
    print(f"    - Page: {figure.get('page', 'N/A')}")

# =============================================================================
# 7. PLOT FIGURES WITH MATPLOTLIB (NEW FEATURE!)
# =============================================================================
print("\n" + "=" * 80)
print("7. PLOT FIGURES WITH MATPLOTLIB (NEW!)")
print("=" * 80)

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend

    # Plot all figures
    print("\nPlotting all figures...")
    figs = paper.table_extractor.plot_all_figures(
        figsize=(10, 8),
        save_dir="extracted_figures"
    )

    print(f"✓ Successfully plotted {len(figs)} figures")
    print(f"✓ Saved to: extracted_figures/ directory")

    # Save raw images
    print("\nSaving raw images...")
    for figure in figures[:3]:  # Save first 3
        fig_num = figure['number']
        output_path = f"figure_{fig_num}_raw.png"
        success = paper.table_extractor.save_figure_image(fig_num, output_path)
        if success:
            print(f"  ✓ Figure {fig_num} saved to: {output_path}")

except ImportError:
    print("\n✗ matplotlib/Pillow not installed.")
    print("   Install with: pip install matplotlib Pillow")

# =============================================================================
# 8. EXPORT TO DIFFERENT FORMATS
# =============================================================================
print("\n" + "=" * 80)
print("8. EXPORT TO DIFFERENT FORMATS")
print("=" * 80)

# JSON export
paper.export("json", "paper_data.json")
print("✓ Exported to: paper_data.json")

# Markdown export
paper.export("markdown", "paper_data.md")
print("✓ Exported to: paper_data.md")

# CSV export
paper.export("csv", "paper_data.csv")
print("✓ Exported to: paper_data.csv")

# Text export
paper.export("txt", "paper_data.txt")
print("✓ Exported to: paper_data.txt")

# =============================================================================
# 9. OPTIONAL: LLM FEATURES (Requires API Key)
# =============================================================================
print("\n" + "=" * 80)
print("9. OPTIONAL: LLM FEATURES")
print("=" * 80)

print("\nLLM features available (requires API key):")
print("  - paper.enable_llm(provider='openai', api_key='sk-...')")
print("  - paper.summarize('methodology', max_length=150)")
print("  - paper.classify()")
print("\nSkipping LLM demo (requires API key)")

# =============================================================================
# 10. SUMMARY
# =============================================================================
print("\n" + "=" * 80)
print("10. SUMMARY")
print("=" * 80)

print("\nExtracted Data:")
print(f"  ✓ Metadata: {len(meta)} fields")
print(f"  ✓ Sections: {len(sections)} sections")
print(f"  ✓ References: {len(references)} references")
print(f"  ✓ Tables: {len(tables)} tables")
print(f"  ✓ Figures: {len(figures)} figures")

print("\nGenerated Files:")
print("  ✓ paper_data.json (structured data)")
print("  ✓ paper_data.md (readable format)")
print("  ✓ paper_data.csv (flattened data)")
print("  ✓ paper_data.txt (plain text)")
print("  ✓ table_*.csv (individual tables)")
print("  ✓ extracted_figures/*.png (figure plots)")
print("  ✓ figure_*_raw.png (raw images)")

# Close the paper
paper.close()

print("\n" + "=" * 80)
print("✓ DEMO COMPLETE!")
print("=" * 80)

print("\n" + "=" * 80)
print("FEATURE SUMMARY")
print("=" * 80)

print("""
CORE FEATURES:
  📄 Metadata Extraction - Title, authors, affiliations, DOI, year
  📑 Section Detection - Abstract, intro, methods, results, etc.
  🔍 Reference Parsing - Structured citation extraction
  📊 Table Extraction - Tables with captions and content
  🖼️  Figure Extraction - Figures with captions

NEW FEATURES:
  🐼 pandas DataFrames - Convert tables to DataFrames
  📈 matplotlib Plotting - Visualize figures directly
  💾 Multiple Exports - JSON, Markdown, CSV, TXT

OPTIONAL FEATURES:
  🧠 LLM Integration - Summarization and classification
  🤖 AI Providers - OpenAI, Anthropic, HuggingFace, Local

INSTALLATION:
  Core:      pip install PyMuPDF pdfminer.six
  DataFrames: pip install pandas
  Plotting:   pip install matplotlib Pillow
  LLM:       pip install openai anthropic

USAGE:
  from bayan import Paper
  paper = Paper("paper.pdf")
  meta = paper.extract_metadata()
  df = paper.table_extractor.get_table_as_dataframe("1")
  fig = paper.table_extractor.plot_figure("1")
  paper.export("json", "output.json")

DOCUMENTATION:
  README.md - Full documentation
  NEW_FEATURES.md - DataFrame & plotting guide
  QUICKSTART.md - Quick start guide
  example.py - More examples
""")

print("\n" + "=" * 80)
print("Thank you for using بيان bayan!")
print("=" * 80)
