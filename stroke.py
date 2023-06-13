import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# Load data from Google Drive link
#file_id = '1RPRn2gUaCesisx24IwQGZHcAGvR40nMh'
#url = f"https://drive.google.com/uc?id={file_id}"
stroke = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Create a sidebar
st.sidebar.title('Filter')

# Add a checkbox to filter by marital status
selected_married = st.sidebar.selectbox('Select status', [''] + stroke['ever_married'].unique().tolist())

selected_area = st.sidebar.selectbox('Select area', [''] + stroke['Residence_type'].unique().tolist())

selected_residence = st.sidebar.selectbox('Select work type', [''] + stroke['work_type'].unique().tolist())

selected_smoking = st.sidebar.selectbox('Select smoking', [''] + stroke['smoking_status'].unique().tolist())

# Filter the data based on the selected values
if selected_married == '' and selected_area == '' and selected_residence == '' and selected_smoking == '':
    filtered_data = stroke.copy()  # No filter applied, use the entire data frame
else:
    filtered_data = stroke[
        (stroke['ever_married'].isin([selected_married])) &
        (stroke['Residence_type'].isin([selected_area])) &
        (stroke['work_type'].isin([selected_residence])) &
        (stroke['smoking_status'].isin([selected_smoking]))
]




# Replace values in the stroke column
stroke['stroke'] = stroke['stroke'].replace({1: 'Yes', 0: 'No'})

# Interactive visualizations
st.title("Stroke Dataset Dashboard")

# Add welcome message to sidebar
st.sidebar.title("Welcome to Nour El Hajj's Dashboard")

# Add image
image_url = "https://drive.google.com/uc?id=1ZoNOvhrTviIZ8MhY-pnysX9pVWHfH4C6"
st.image(image_url, use_column_width=True)

# Interactive visualizations
st.title("Age Distribution")

# Filter the data for stroke cases
stroke_data = filtered_data[filtered_data['stroke'] == 1]

# Create a histogram of age groups for stroke cases
fig, ax = plt.subplots()
ax.hist(stroke_data['age'], bins=10, alpha=0.5, label='Stroke')
ax.set_xlabel('Age')
ax.set_ylabel('Count')
ax.set_title('Age Distribution for Stroke Cases')
ax.legend()
# Display the histogram in the Streamlit app
st.pyplot(fig)

# Box plot - Age vs. Stroke
fig_age_stroke = px.box(filtered_data, x='stroke', y='age', color='stroke',
                        title="Age vs. Stroke", color_discrete_map={'No': 'blue', 'Yes': 'red'},
                        labels={'stroke': 'Stroke (0 = No, 1 = Yes)'})
fig_age_stroke.update_traces(showlegend=True)
st.plotly_chart(fig_age_stroke)

# Count plot - Hypertension vs. Stroke
fig_hypertension_stroke = px.histogram(filtered_data, x='hypertension', color='stroke',
                                       title="Hypertension vs. Stroke", color_discrete_map={'No': 'blue', 'Yes': 'red'},
                                       labels={'hypertension': 'Hypertension (0 = No, 1 = Yes)'})
fig_hypertension_stroke.update_traces(xbins={'size': 1}, showlegend=True)
st.plotly_chart(fig_hypertension_stroke)

# Count plot - Heart Disease vs. Stroke
fig_heart_disease_stroke = px.histogram(filtered_data, x='heart_disease', color='stroke',
                                         title="Heart Disease vs. Stroke", color_discrete_map={'No': 'blue', 'Yes': 'red'},
                                         labels={'heart_disease': 'Heart Disease (0 = No, 1 = Yes)'})
fig_heart_disease_stroke.update_traces(xbins={'size': 1}, showlegend=True)
st.plotly_chart(fig_heart_disease_stroke)

# Box plot - Average Glucose Level vs. Stroke
fig_glucose_stroke = px.box(filtered_data, x='stroke', y='avg_glucose_level', color='stroke',
                            title="Average Glucose Level vs. Stroke", color_discrete_map={'No': 'blue', 'Yes': 'red'},
                            labels={'stroke': 'Stroke (0 = No, 1 = Yes)'})
fig_glucose_stroke.update_traces(showlegend=True)
st.plotly_chart(fig_glucose_stroke)

# Bar chart - Smoking Status vs. Stroke
fig_smoking_stroke = px.bar(filtered_data, x='smoking_status', color='stroke',
                            title="Smoking Status vs. Stroke", color_discrete_map={'No': 'blue', 'Yes': 'red'},
                            labels={'stroke': 'Stroke (0 = No, 1 = Yes)', 'smoking_status': 'Smoking Status'})
fig_smoking_stroke.update_traces(showlegend=True)
st.plotly_chart(fig_smoking_stroke)

