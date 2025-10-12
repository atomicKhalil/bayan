"""
Simple demo of bayan's DataFrame and plotting features.
"""

from bayan import Paper

# Load paper
paper = Paper("test_paper.pdf")

print("=" * 70)
print("DEMO: Tables as DataFrames & Figure Plotting")
print("=" * 70)

# Example 1: Get all tables as pandas DataFrames
print("\n📊 TABLES AS DATAFRAMES\n")

tables_df = paper.table_extractor.get_all_tables_as_dataframes()

for table_num, df in tables_df.items():
    print(f"Table {table_num}: {df.attrs['caption'][:60]}...")
    print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"  Page: {df.attrs['page']}")

    # You can now use pandas operations!
    print(f"  First row: {df.iloc[0].values if len(df) > 0 else 'Empty'}")

    # Save to CSV
    df.to_csv(f"table_{table_num}.csv")
    print(f"  ✓ Saved to table_{table_num}.csv\n")

# Example 2: Get specific table
print("\n📋 GET SPECIFIC TABLE\n")

df = paper.table_extractor.get_table_as_dataframe("1")
if df is not None:
    print(f"Table 1: {df.attrs['caption'][:60]}...")
    print(f"\nDataFrame:\n{df}\n")

    # You can analyze it with pandas
    print(f"DataFrame has {len(df)} rows and {len(df.columns)} columns")

# Example 3: Plot figures with matplotlib
print("\n🖼️  PLOTTING FIGURES\n")

# Plot a specific figure
fig = paper.table_extractor.plot_figure(
    "3",  # Figure number
    figsize=(12, 8),  # Size in inches
    save_path="my_figure.png"  # Save location
)

if fig:
    print("✓ Figure 3 plotted and saved to my_figure.png")
else:
    print("Figure 3 not available")

# Plot all figures at once
print("\nPlotting all figures...")
figs = paper.table_extractor.plot_all_figures(save_dir="all_figures")
print(f"✓ Plotted {len(figs)} figures to 'all_figures/' directory")

# Example 4: Save raw figure image
print("\n💾 SAVE RAW IMAGES\n")

success = paper.table_extractor.save_figure_image("3", "figure_3_raw.png")
if success:
    print("✓ Figure 3 saved as raw image")

paper.close()

print("\n" + "=" * 70)
print("✓ DEMO COMPLETE!")
print("=" * 70)
print("""
NEW FEATURES:

1️⃣  Tables as pandas DataFrames:
    • df = paper.table_extractor.get_table_as_dataframe("1")
    • dfs = paper.table_extractor.get_all_tables_as_dataframes()
    • Access metadata: df.attrs['caption'], df.attrs['page']
    • Use all pandas operations: df.head(), df.describe(), etc.

2️⃣  Plot figures with matplotlib:
    • fig = paper.table_extractor.plot_figure("1")
    • figs = paper.table_extractor.plot_all_figures()
    • Customize: figsize=(width, height), save_path="file.png"

3️⃣  Save raw images:
    • paper.table_extractor.save_figure_image("1", "output.png")

Install: pip install pandas matplotlib Pillow
""")
