"""
Example usage of bayan library for extracting information from research papers.
"""

from bayan import Paper


def basic_example():
    """Basic usage example."""
    print("=" * 80)
    print("BASIC EXAMPLE - Extracting Paper Information")
    print("=" * 80)

    # Load a paper
    paper = Paper("research_paper.pdf")

    # Extract metadata
    print("\n1. METADATA")
    print("-" * 80)
    meta = paper.extract_metadata()
    print(f"Title: {meta['title']}")
    print(f"Authors: {', '.join(meta['authors'])}")
    print(f"Year: {meta['year']}")
    print(f"DOI: {meta.get('doi', 'Not found')}")
    print(f"Page Count: {meta['page_count']}")

    # Extract abstract
    print("\n2. ABSTRACT")
    print("-" * 80)
    sections = paper.extract_sections()
    abstract = sections.get("abstract", "Not found")
    print(abstract[:300] + "..." if len(abstract) > 300 else abstract)

    # Extract references
    print("\n3. REFERENCES")
    print("-" * 80)
    references = paper.extract_references()
    print(f"Found {len(references)} references")
    for ref in references[:3]:  # Show first 3
        print(f"[{ref['id']}] {ref['text'][:100]}...")

    # Extract tables
    print("\n4. TABLES")
    print("-" * 80)
    tables = paper.extract_tables()
    print(f"Found {len(tables)} tables")
    for table in tables:
        print(f"Table {table['number']}: {table['caption']}")

    # Extract figures
    print("\n5. FIGURES")
    print("-" * 80)
    figures = paper.extract_figures()
    print(f"Found {len(figures)} figures")
    for figure in figures:
        print(f"Figure {figure['number']}: {figure['caption']}")

    # Export
    print("\n6. EXPORTING")
    print("-" * 80)
    paper.export("json", "output.json")
    print("✓ Exported to output.json")

    paper.export("markdown", "output.md")
    print("✓ Exported to output.md")

    paper.close()


def llm_example():
    """Example with LLM integration."""
    print("\n" + "=" * 80)
    print("LLM EXAMPLE - AI-Powered Analysis")
    print("=" * 80)

    paper = Paper("research_paper.pdf")

    # Enable LLM (requires API key)
    # paper.enable_llm(provider="openai", api_key="your-api-key-here")

    print("\nNote: LLM features require an API key.")
    print("Uncomment the enable_llm line and add your API key to test.")

    # Example LLM operations (commented out)
    # summary = paper.summarize("methodology", max_length=150)
    # print(f"\nMethodology Summary:\n{summary}")

    # classification = paper.classify()
    # print(f"\nPaper Classification:")
    # print(f"  Type: {classification['paper_type']}")
    # print(f"  Domain: {classification['domain']}")

    paper.close()


def batch_example():
    """Example of batch processing multiple papers."""
    print("\n" + "=" * 80)
    print("BATCH EXAMPLE - Processing Multiple Papers")
    print("=" * 80)

    import glob
    import json

    # Get all PDFs in a directory
    pdf_files = glob.glob("papers/*.pdf")

    if not pdf_files:
        print("\nNo PDF files found in 'papers/' directory.")
        print("Create a 'papers/' directory and add some PDFs to test batch processing.")
        return

    results = []

    for pdf_path in pdf_files:
        print(f"\nProcessing: {pdf_path}")

        try:
            paper = Paper(pdf_path)
            meta = paper.extract_metadata()

            results.append({
                "file": pdf_path,
                "title": meta["title"],
                "authors": meta["authors"],
                "year": meta["year"],
                "doi": meta.get("doi")
            })

            paper.close()
            print(f"✓ {meta['title'][:50]}...")

        except Exception as e:
            print(f"✗ Error: {e}")

    # Save batch results
    with open("batch_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Processed {len(results)} papers")
    print("✓ Results saved to batch_results.json")


def advanced_example():
    """Advanced usage with custom exports."""
    print("\n" + "=" * 80)
    print("ADVANCED EXAMPLE - Custom Processing")
    print("=" * 80)

    paper = Paper("research_paper.pdf")

    # Extract everything
    data = paper.extract_all()

    # Custom filtering - extract only methodology
    methodology = data["sections"].get("methodology", "")

    if methodology:
        print("\nMethodology Section:")
        print("-" * 80)
        print(methodology[:500] + "...")

        # Save just methodology
        with open("methodology.txt", "w", encoding="utf-8") as f:
            f.write(methodology)
        print("\n✓ Saved methodology to methodology.txt")

    # Export specific table to CSV
    if data["tables"]:
        table_num = data["tables"][0]["number"]
        csv_data = paper.table_extractor.export_table_to_csv(table_num)

        if csv_data:
            with open(f"table_{table_num}.csv", "w") as f:
                f.write(csv_data)
            print(f"✓ Saved Table {table_num} to table_{table_num}.csv")

    # Create custom summary
    summary = {
        "title": data["metadata"]["title"],
        "authors": data["metadata"]["authors"],
        "abstract": data["sections"].get("abstract", "")[:200] + "...",
        "key_sections": list(data["sections"].keys()),
        "table_count": len(data["tables"]),
        "figure_count": len(data["figures"]),
        "reference_count": len(data["references"])
    }

    with open("custom_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("✓ Saved custom summary to custom_summary.json")

    paper.close()


def main():
    """Run all examples."""
    print("\n🔬 BAYAN - Research Paper Extraction Examples")
    print("=" * 80)

    # Check if example PDF exists
    import os

    if not os.path.exists("research_paper.pdf"):
        print("\n⚠ No 'research_paper.pdf' found in current directory.")
        print("\nTo run these examples:")
        print("1. Place a research paper PDF named 'research_paper.pdf' in this directory")
        print("2. Run this script again: python example.py")
        print("\nYou can also modify the file paths in this script to match your PDFs.")
        return

    # Run examples
    try:
        basic_example()
    except Exception as e:
        print(f"\nError in basic example: {e}")

    try:
        llm_example()
    except Exception as e:
        print(f"\nError in LLM example: {e}")

    try:
        batch_example()
    except Exception as e:
        print(f"\nError in batch example: {e}")

    try:
        advanced_example()
    except Exception as e:
        print(f"\nError in advanced example: {e}")

    print("\n" + "=" * 80)
    print("✓ Examples completed!")
    print("=" * 80)


if __name__ == "__main__":
    main()
