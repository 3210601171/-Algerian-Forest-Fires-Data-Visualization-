`Algerian-Forest-Fires-Data-Visualization`
# Algerian Forest Fires Dataset Visualization

This project visualizes the Algerian Forest Fires Dataset using a scatter plot to show the relationship between temperature and relative humidity, with date (month-day) information displayed on hover.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Visualization](#visualization)
- [License](#license)

## Features
- Scatter plot showing temperature vs. relative humidity.
- Hover tooltip displaying date (month-day) and relative humidity.
- Visual map for humidity range (high to low).
- Toolbox for saving, restoring, and other operations on the chart.

## Prerequisites
- Python 3.6 or higher.
- Libraries: `pandas`, `pyecharts`, `glob`, `os`. You can install them via:
  ```bash
  pip install pandas pyecharts
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/algerian-forest-fires-visualization.git
   cd algerian-forest-fires-visualization
   ```
2. Ensure you have the `Algerian_forest_fires_dataset_UPDATE.csv` file in the appropriate path. If not, place it in the project directory or provide the correct path when prompted.

## Usage
1. Run the Python script:
   ```bash
   python algerian_forest_fires_english.py
   ```
2. If the data file (`Algerian_forest_fires_dataset_UPDATE.csv`) is not automatically found, you will be prompted to enter its path.
3. The script will generate an HTML file (`algerian_forest_fires_scatter.html`) with the visualization. Open this file in a web browser to view the chart.

## Data
The dataset used is the [Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++). It contains information related to forest fires in Algeria, including temperature, relative humidity, and date (day, month, year).

## Visualization
- **X-axis**: Temperature (°C).
- **Y-axis**: Relative Humidity (%).
- **Color**: The color of scatter points represents humidity levels (from high to low, indicated by the visual map on the right).
- **Tooltip**: On hover, shows the date (month-day) and relative humidity.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
