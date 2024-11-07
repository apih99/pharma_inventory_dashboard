import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv('filtered_stock_movement.csv')

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home","Descriptive Statistics","Dataset", "Data Overview","Segments Visualization", "Correlation Analysis",])
# Display the data

# Page: Home
if page == "Home":
    st.title('🧪 Pharmaceutical Inventory Dashboard - Hafiz')
    st.header('📊 Dataset Overview')
    
    # Description of the dataset with markdown
    st.markdown("""
    <div style="background-color: blue; padding: 10px; border-radius: 5px;">
        <p style="font-size: 16px;">
        This dashboard provides insights into the <strong>pharmaceutical inventory dataset</strong>. 
        The dataset includes information about various pharmaceutical products, 
        including their <em>descriptions</em>, <em>quantities</em>, and <em>values</em>. It is designed to help 
        users analyze inventory levels, identify top-performing products, and visualize 
        data trends.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Display basic information about the dataset
    st.subheader('📋 Dataset Information')
    st.write(f"**Number of records:** {data.shape[0]}")
    st.write(f"**Number of columns:** {data.shape[1]}")
    st.write("**Columns:** ", ', '.join(data.columns.tolist()))

    # Display a sample of the dataset
    st.subheader('🔍 Sample Data')
    st.dataframe(data.head())

elif page == "Descriptive Statistics":
    st.title('Descriptive Statistics')

    # Calculate summary statistics
    st.subheader('Summary Statistics for Quantity and Value')
    summary_stats = data[['Quantity', 'Value']].describe()
    st.write(summary_stats)

    # Additional statistics
    st.subheader('Additional Statistics')
    st.write(f"Median Quantity: {data['Quantity'].median()}")
    st.write(f"Median Value: {data['Value'].median()}")
    st.write(f"Quantity Standard Deviation: {data['Quantity'].std()}")
    st.write(f"Value Standard Deviation: {data['Value'].std()}")

elif page == "Dataset":
    st.title('Pharmaceutical Inventory Dashboard')
    
    # Display the dataframe with increased height and width
    st.dataframe(data, height=600, width=1000) 


# Filter by product category (assuming 'Category' is a column in your dataset)
# Page: Data Overview
elif page == "Data Overview":
    st.title('Pharmaceutical Inventory Dashboard - Data Overview')

    # Filter by product category
    categories = data['Description'].unique()
    selected_category = st.selectbox('Select a Category', categories)
    filtered_data = data[data['Description'] == selected_category]

    # Sort by column
    sort_by = st.selectbox('Sort by', ['Quantity', 'Value'])
    sorted_data = filtered_data.sort_values(by=sort_by, ascending=False)

    # Display the filtered and sorted data
    st.dataframe(sorted_data)


elif page == "Segments Visualization":
    st.title('Product Segments Visualization')
    
    # Selectbox for choosing the metric
    metric = st.selectbox('Select metric to display products:', ['Quantity', 'Value'], index=0)
    
    # Selectbox for choosing the segment
    segment = st.selectbox('Select segment to display:', ['Top', 'Middle', 'Bottom'], index=0)
    
    # Selectbox for choosing the number of products
    number = st.selectbox('Select number of products:', [5, 10], index=0)
    
    # Determine the products to display based on the selected segment and number
    if segment == 'Top':
        products = data.nlargest(number, metric)
    elif segment == 'Middle':
        middle_index = len(data) // 2
        half_number = number // 2
        products = data.iloc[middle_index-half_number:middle_index+half_number].sort_values(by=metric, ascending=False)
    elif segment == 'Bottom':
        products = data.nsmallest(number, metric)
    
    # Display the selected products in a dataframe
    st.write(f'{segment} {number} Products by {metric}:')
    st.dataframe(products)
    
    # Selectbox for choosing the chart type
    chart_type = st.selectbox('Select chart type:', ['Bar Chart', 'Pie Chart'], index=0)
    
    # Create a chart based on the selected type
    if chart_type == 'Bar Chart':
        st.subheader(f'{segment} {number} Products by {metric} - Bar Chart')
        bar_chart = px.bar(products, x='Description', y=metric, title=f'{segment} {number} Products by {metric}', labels={'Description': 'Product Description', metric: metric})
        st.plotly_chart(bar_chart)
    elif chart_type == 'Pie Chart':
        st.subheader(f'{segment} {number} Products by {metric} - Pie Chart')
        pie_chart = px.pie(products, names='Description', values=metric, title=f'{segment} {number} Products by {metric}')
        st.plotly_chart(pie_chart)

elif page == "Correlation Analysis":
    st.title('Correlation Analysis')

    # Calculate correlation matrix
    st.subheader('Correlation Matrix')
    correlation_matrix = data[['Quantity', 'Value']].corr()
    st.write(correlation_matrix)

    # Visualize the correlation matrix as a heatmap
    st.subheader('Correlation Heatmap')
    heatmap = px.imshow(correlation_matrix, text_auto=True, aspect="auto", title='Correlation Heatmap')
    st.plotly_chart(heatmap)


