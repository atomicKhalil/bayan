# 🎉 New Features in بيان bayan

## Version 0.2.0 - Data Analysis & Visualization

We've added powerful new features for working with tables and figures!

---

## 🐼 Feature 1: pandas DataFrame Support

Convert extracted tables directly to pandas DataFrames for easy analysis!

### Basic Usage

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Get a specific table as DataFrame
df = paper.table_extractor.get_table_as_dataframe("1")

# Access table metadata
print(f"Caption: {df.attrs['caption']}")
print(f"Page: {df.attrs['page']}")
print(f"Table Number: {df.attrs['table_number']}")

# Use all pandas operations!
print(df.head())
print(df.describe())
print(df.shape)

# Save to CSV
df.to_csv("table_1.csv", index=False)
```

### Get All Tables

```python
# Get all tables as a dictionary of DataFrames
tables_df = paper.table_extractor.get_all_tables_as_dataframes()

for table_num, df in tables_df.items():
    print(f"\nTable {table_num}")
    print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"  Caption: {df.attrs['caption'][:50]}...")

    # Analyze each table
    print(df.head())

    # Save to CSV
    df.to_csv(f"table_{table_num}.csv")
```

### Why This is Awesome

- ✅ **Instant Analysis:** Use all pandas operations (groupby, pivot, describe, etc.)
- ✅ **Metadata Included:** Caption, page number stored in `df.attrs`
- ✅ **Easy Export:** Convert to CSV, Excel, JSON with pandas
- ✅ **Data Science Ready:** Perfect for matplotlib, seaborn, sklearn
- ✅ **Smart Headers:** Automatically detects header rows

---

## 📈 Feature 2: matplotlib Figure Plotting

Visualize figures from PDFs directly with matplotlib!

### Plot a Single Figure

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Plot figure 1
fig = paper.table_extractor.plot_figure(
    "1",                      # Figure number
    figsize=(12, 8),          # Size in inches
    save_path="figure_1.png"  # Optional: save to file
)

# Display it (if using Jupyter or interactive mode)
import matplotlib.pyplot as plt
plt.show()
```

### Plot All Figures

```python
# Plot all figures at once
figs = paper.table_extractor.plot_all_figures(
    figsize=(10, 8),
    save_dir="figures/"  # Saves to directory
)

print(f"Plotted {len(figs)} figures")
```

### Save Raw Images

```python
# Save the raw image without matplotlib wrapper
success = paper.table_extractor.save_figure_image(
    "1",
    "figure_1_raw.png"
)

if success:
    print("✓ Image saved!")
```

### Why This is Awesome

- ✅ **Direct Visualization:** No need to extract images manually
- ✅ **High Quality:** 300 DPI output
- ✅ **Automatic Captions:** Figure captions shown as titles
- ✅ **Batch Processing:** Plot all figures with one command
- ✅ **matplotlib Integration:** Returned figures can be further customized

---

## 📦 Installation

```bash
# Install pandas and matplotlib support
pip install pandas matplotlib Pillow
```

Or install from requirements:
```bash
pip install -r requirements.txt
```

---

## 🚀 Complete Example

```python
from bayan import Paper

# Load paper
paper = Paper("research_paper.pdf")

print("=" * 60)
print("ANALYZING RESEARCH PAPER")
print("=" * 60)

# 1. Extract and analyze tables
print("\n📊 TABLES:")
tables_df = paper.table_extractor.get_all_tables_as_dataframes()

for table_num, df in tables_df.items():
    print(f"\nTable {table_num}: {df.attrs['caption'][:50]}...")
    print(f"  Dimensions: {df.shape}")

    # Statistical analysis
    if df.select_dtypes(include=['number']).shape[1] > 0:
        print(f"  Numeric columns: {df.select_dtypes(include=['number']).columns.tolist()}")

    # Save
    df.to_csv(f"table_{table_num}.csv")
    print(f"  ✓ Saved to table_{table_num}.csv")

# 2. Plot and save figures
print("\n🖼️  FIGURES:")
figs = paper.table_extractor.plot_all_figures(
    figsize=(10, 8),
    save_dir="figures/"
)
print(f"✓ Plotted {len(figs)} figures to 'figures/' directory")

# 3. Export everything
paper.export("json", "paper_data.json")
print("\n✓ Complete data exported to paper_data.json")

paper.close()
print("\n" + "=" * 60)
print("ANALYSIS COMPLETE!")
print("=" * 60)
```

---

## 📊 Real-World Use Cases

### Use Case 1: Meta-Analysis

```python
import pandas as pd
from bayan import Paper

# Extract performance tables from multiple papers
results = []

for pdf in ["paper1.pdf", "paper2.pdf", "paper3.pdf"]:
    paper = Paper(pdf)

    # Get results table
    df = paper.table_extractor.get_table_as_dataframe("1")

    if df is not None:
        df['source'] = pdf
        results.append(df)

# Combine all results
combined = pd.concat(results, ignore_index=True)

# Analyze
print(combined.groupby('Model')['Accuracy'].mean())

# Save combined results
combined.to_csv("meta_analysis.csv")
```

### Use Case 2: Figure Extraction for Presentations

```python
from bayan import Paper

paper = Paper("paper.pdf")

# Extract all figures for your presentation
figs = paper.table_extractor.plot_all_figures(
    figsize=(12, 8),
    save_dir="presentation_figures/"
)

print(f"✓ Extracted {len(figs)} figures for presentation")
```

### Use Case 3: Automated Reporting

```python
from bayan import Paper
import matplotlib.pyplot as plt

paper = Paper("paper.pdf")

# Get all tables as DataFrames
tables = paper.table_extractor.get_all_tables_as_dataframes()

# Generate report
with open("report.md", "w") as f:
    f.write("# Paper Analysis Report\n\n")

    f.write("## Tables\n\n")
    for table_num, df in tables.items():
        f.write(f"### Table {table_num}\n")
        f.write(f"**Caption:** {df.attrs['caption']}\n\n")
        f.write(df.to_markdown() + "\n\n")

    f.write("## Figures\n\n")
    figures = paper.extract_figures()
    for fig in figures:
        f.write(f"### Figure {fig['number']}\n")
        f.write(f"**Caption:** {fig['caption']}\n\n")

print("✓ Report generated!")
```

---

## 🎯 Method Reference

### DataFrame Methods

| Method | Description |
|--------|-------------|
| `get_table_as_dataframe(table_num)` | Get specific table as DataFrame |
| `get_all_tables_as_dataframes()` | Get all tables as dict of DataFrames |

**DataFrame Attributes:**
- `df.attrs['table_number']` - Table number
- `df.attrs['caption']` - Table caption
- `df.attrs['page']` - Page number

### Plotting Methods

| Method | Description |
|--------|-------------|
| `plot_figure(fig_num, figsize, save_path)` | Plot specific figure |
| `plot_all_figures(figsize, save_dir)` | Plot all figures |
| `save_figure_image(fig_num, output_path)` | Save raw image |

**Parameters:**
- `fig_num` (str): Figure number (e.g., "1", "2a")
- `figsize` (tuple): Size in inches (width, height)
- `save_path` (str): Optional path to save figure
- `save_dir` (str): Optional directory for batch saving

---

## 🔧 Technical Details

### How It Works

**DataFrames:**
1. Extracts table content as rows/columns
2. Detects header rows automatically
3. Creates pandas DataFrame
4. Attaches metadata as attributes
5. Returns DataFrame object

**Plotting:**
1. Extracts figure from PDF page
2. Finds largest image on page
3. Converts to PIL Image
4. Creates matplotlib figure
5. Adds caption as title
6. Optionally saves to file

### Error Handling

Both features include graceful error handling:

```python
# DataFrames - checks for pandas
try:
    df = paper.table_extractor.get_table_as_dataframe("1")
except ImportError:
    print("Install pandas: pip install pandas")

# Plotting - checks for matplotlib and PIL
try:
    fig = paper.table_extractor.plot_figure("1")
except ImportError:
    print("Install matplotlib: pip install matplotlib Pillow")
```

---

## 🎓 Tips & Best Practices

### For DataFrames

1. **Check shape first:** `print(df.shape)` before analysis
2. **Inspect datatypes:** `df.dtypes` to see column types
3. **Clean data:** Use `df.fillna()`, `df.dropna()` as needed
4. **Access metadata:** Always check `df.attrs` for context

### For Plotting

1. **Adjust figsize:** Larger figures for details, smaller for overviews
2. **Use save_dir:** Batch save all figures to organized directory
3. **Check page numbers:** Some PDFs have figures on multiple pages
4. **High DPI:** Figures saved at 300 DPI for publication quality

---

## 🐛 Troubleshooting

### "No tables found"
- PDF might have tables as images (OCR needed)
- Try checking `paper.extract_tables()` first

### "No images found on page"
- Figure might be embedded differently
- Some PDFs use vector graphics (not images)
- Try `save_figure_image()` as alternative

### "ImportError: No module named pandas"
```bash
pip install pandas matplotlib Pillow
```

---

## 🎉 What's Next?

Future enhancements planned:
- Table editing and manipulation
- Figure annotation
- Interactive plotting with plotly
- Export DataFrames to Excel with formatting
- Merge multiple tables

---

**بيان bayan** — *Now with data science superpowers!*

📖 [Full Documentation](README.md) | 🚀 [Quick Start](QUICKSTART.md) | 💻 [Examples](example.py)
