import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime, timedelta

# Generate sample data
def generate_sample_data(days=30):
    date_range = pd.date_range(end=datetime.now(), periods=days)
    instances = ['t2.micro', 't2.small', 't3.medium', 'm5a.large']
    data = []
    for date in date_range:
        for instance in instances:
            hours = np.random.uniform(1, 24)
            cost = hours * np.random.uniform(0.01, 0.5)
            data.append({
                'date': date,
                'instance': instance,
                'hours': hours,
                'cost': cost
            })
    return pd.DataFrame(data)

# Main Streamlit app
def main():
    st.title('Advanced EC2 Cost Analyzer')

    # Generate or load data
    df = generate_sample_data()

    # Sidebar for user input
    st.sidebar.header('Filters')
    selected_instances = st.sidebar.multiselect('Select Instances', df['instance'].unique(), default=df['instance'].unique())
    date_range = st.sidebar.date_input('Select Date Range', [df['date'].min(), df['date'].max()])

    # Filter data based on user input
    filtered_df = df[(df['instance'].isin(selected_instances)) & 
                     (df['date'] >= date_range[0]) & 
                     (df['date'] <= date_range[1])]

    # Display raw data
    st.subheader('Raw Data')
    st.dataframe(filtered_df)

    # Basic statistics
    st.subheader('Basic Statistics')
    st.write(filtered_df.describe())

    # Total cost by instance type
    st.subheader('Total Cost by Instance Type')
    total_cost = filtered_df.groupby('instance')['cost'].sum().sort_values(ascending=False)
    st.bar_chart(total_cost)

    # Daily cost trend
    st.subheader('Daily Cost Trend')
    daily_cost = filtered_df.groupby('date')['cost'].sum().reset_index()
    fig_daily = px.line(daily_cost, x='date', y='cost', title='Daily Total Cost')
    st.plotly_chart(fig_daily)

    # Correlation heatmap
    st.subheader('Correlation Heatmap')
    numeric_df = filtered_df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Cost distribution
    st.subheader('Cost Distribution by Instance Type')
    fig_dist = px.box(filtered_df, x='instance', y='cost', title='Cost Distribution by Instance Type')
    st.plotly_chart(fig_dist)

    # Hourly usage patterns
    st.subheader('Hourly Usage Patterns')
    filtered_df['hour'] = filtered_df['date'].dt.hour
    hourly_usage = filtered_df.groupby(['hour', 'instance'])['hours'].mean().unstack()
    fig_hourly = px.imshow(hourly_usage, title='Average Hourly Usage by Instance Type',
                           labels=dict(x="Instance Type", y="Hour of Day", color="Average Hours"))
    st.plotly_chart(fig_hourly)

if __name__ == '__main__':
    main()