# Pharmaceutical Inventory Dashboard

## Overview

The **Pharmaceutical Inventory Dashboard** is an interactive web application built with Streamlit. It provides insights into a pharmaceutical inventory dataset, allowing users to analyze inventory levels, identify top-performing products, and visualize data trends. The application is designed to help users make informed decisions about inventory management.

## Features

- **Home Page**: Overview of the dataset with basic statistics and a sample of the data.
- **Descriptive Statistics**: Summary statistics for key metrics such as Quantity and Value.
- **Correlation Analysis**: Visualize the correlation between different numerical features using a heatmap.
- **Segments Visualization**: Explore top, middle, and bottom segments of products based on Quantity or Value, with options to view as bar or pie charts.
- **Dataset View**: View the entire dataset with adjustable table size for better readability.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pharmaceutical-inventory-dashboard.git
   cd pharmaceutical-inventory-dashboard
   ```

2. **Install the required packages**:
   Make sure you have Python installed. Then, install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run Pharma.py
   ```

## Usage

- **Home Page**: Provides an introduction to the dataset and displays basic information.
- **Descriptive Statistics**: Navigate to this page to view detailed statistics about the dataset.
- **Correlation Analysis**: Use this page to explore relationships between different metrics.
- **Segments Visualization**: Choose different segments and metrics to visualize product performance.
- **Dataset View**: Access the full dataset for a comprehensive view.

## Dataset

The dataset used in this project includes information about various pharmaceutical products, such as their descriptions, quantities, and values. It is stored in a CSV file named `filtered_stock_movement.csv`. This dataset comes from one of the district hospital in Malaysia.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, please contact [Hafiz](mailto:hafizcr716@gmail.com).
