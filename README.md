# Mark Analysis Tool

## Overview
The **Mark Analysis Tool** is a Python-based application designed to analyze and visualize academic performance data. It provides a menu-driven interface for performing various operations on a dataset, such as fetching data, viewing statistics, modifying records, and generating visualizations.

## Features
1. **Data Loading**:
   - Load a dataset from a CSV file.

2. **Dataframe Statistics**:
   - View properties of the dataset, such as transpose, column names, indexes, shape, dimensions, data types, and size.

3. **Display Records**:
   - Display top or bottom records.
   - View specific records or details of a specific subject.

4. **Modify Records**:
   - Insert, delete, or update records (rows).
   - Add or delete columns.

5. **Search Functionality**:
   - Search for specific rows or columns.

6. **Data Visualization**:
   - Generate line plots, bar plots (vertical and horizontal), and histograms for various metrics.

7. **Data Analytics**:
   - Identify subjects with maximum or minimum average marks, highest marks, or percentages of A1 and A2 grades.

## Prerequisites
- Python 3.6 or higher
- Required Python libraries:
  - `pandas`
  - `matplotlib`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dev-091/mark-analysis-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mark-analysis-tool
   ```
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python Result.py
   ```
2. Follow the on-screen menu to perform various operations:
   - Fetch data by selecting option `1`.
   - Navigate through the menus to analyze and visualize the data.

## File Structure
- `Result.py`: The main script containing the menu-driven application.
- `result.csv`: The dataset file (ensure it is placed in the correct directory).

## Example Dataset
The dataset should be in CSV format with the following structure:
| Subject | Appeared | Highest | Average | A1 | A2 | Percentage | B1 | B2 | C1 | C2 | D | E |
|---------|----------|---------|---------|----|----|------------|----|----|----|----|---|---|
| Math    | 100      | 98      | 85      | 10 | 15 | 25%        | 20 | 25 | 15 | 10 | 5 | 0 |

## Notes
- Ensure the dataset file path is correctly specified in the script.
- The program will prompt you to fetch data before performing any operations.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the tool.

## Author
Developed by **Dev-091**.
