import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter
import os
import glob

# Find and read data file
csv_files = glob.glob('**/Algerian_forest_fires_dataset_UPDATE.csv', recursive=True)

if not csv_files:
    print("Data file not found. Please enter the full path to the CSV file:")
    print("Example: D:/data/Algerian_forest_fires_dataset_UPDATE.csv")
    csv_path = input("Please enter the path: ").strip()
else:
    csv_path = csv_files[0]
    print(f"Found data file: {csv_path}")

if not os.path.exists(csv_path):
    print(f"Error: File not found - {csv_path}")
    exit(1)

# Read and process data
df = pd.read_csv(csv_path, header=1)

# Data type conversion and cleaning
df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
df[' RH'] = pd.to_numeric(df[' RH'], errors='coerce')
df['day'] = df['day'].fillna('').astype(str).str.zfill(2)
df['month'] = df['month'].fillna('').astype(str).str.zfill(2)
df['year'] = df['year'].fillna('').astype(str)

# Filter out null values
df_clean = df.dropna(subset=['Temperature', ' RH', 'day', 'month'])

# Prepare basic data
basic_data = [
    [row['Temperature'], row[' RH']]
    for _, row in df_clean.iterrows()
]

# Prepare additional information (date: month-day)
extra_data = [
    f"{row['month']}-{row['day']}"  # Formatted as "MM-DD"
    for _, row in df_clean.iterrows()
]

# Create scatter plot
scatter = (
    Scatter()
    .add_xaxis(xaxis_data=[item[0] for item in basic_data])
    .add_yaxis(
        series_name="Humidity",
        y_axis=[item[1] for item in basic_data],
        symbol_size=10,
        label_opts=opts.LabelOpts(is_show=False),
        # Custom tooltip display
        tooltip_opts=opts.TooltipOpts(
            formatter=lambda params: f"Date: {extra_data[params.dataIndex]}<br>Relative Humidity: {params.value[1]}%",
            axis_pointer_type="cross"
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Algerian Forest Fires Dataset Data Set"),
        visualmap_opts=opts.VisualMapOpts(
            min_=df_clean[' RH'].min(),
            max_=df_clean[' RH'].max(),
            dimension=1,
            orient="vertical",
            pos_right=10,
            pos_top="center",
            range_text=["HIGH", "LOW"],
            is_calculable=True,
            range_color=["#FF9966", "#FFCC99", "#FFFFCC", "#CCFFCC", "#99FFCC"],
        ),
        xaxis_opts=opts.AxisOpts(
            type_="value",
            name="Temperature (°C)",
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="Relative Humidity (%)",
            splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        toolbox_opts=opts.ToolboxOpts(is_show=True)
    )
)

# Save chart
output_path = "algerian_forest_fires_scatter.html"
scatter.render(output_path)
print(f"Chart generated successfully: {os.path.abspath(output_path)}")
    