#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px

st.set_page_config(layout="wide") # Forces a sleek dashboard distribution

st.markdown("""
    <style>
    div[data-testid="stMetricValue"] { color: #00F2FE; font-family: 'Roboto', sans-serif; font-weight: bold; }
    div[data-testid="stMetricLabel"] { color: #A0AEC0; }
    .kpi-container { background-color: #1A202C; padding: 15px; border-radius: 8px; border-left: 4px solid #00F2FE; }
    </style>
    """, unsafe_allow_html=True)

#st.image(r'C:\Users\Pter\Desktop\Dashboard\banner2.png')
st.image('banner2.png')

#st.date_input("Select a date")

st.title("""Welcome to my Dashboard""")

st.subheader("Prepared by:")
st.markdown("""
- **Putri Diana binti Abdul Rasyid** (2518420)  
- **Nur Khairina Najihah binti Hairul Nizam** (2518796)
""")

#upload data
#upload_file = st.file_uploader("Please upload here:", type = 'csv')


#df = pd.read_csv(r"C:\Users\welcome\Desktop\BSMS1306\streamlit\Tips.csv")
df = pd.read_csv("Social_Media_Addiction.csv")
#df = pd.read_csv(upload_file)

#Create two columns
col1, col2 = st.columns(2)

#show data
with col1:
    st.subheader("Raw Data")
    st.write(df)

DF = pd.read_csv('socmed_cleaned.csv')

#show data
with col2:
    st.subheader("Cleaned Data")
    st.write(DF)

# Age selection widget (dropdown)
#selected_age = st.selectbox("Select Age", options=range(13, 20))

# Filter teenagers by selected age
#teenagers = DF[(DF["Age"] == selected_age)]

st.subheader("Pie Chart")

# Age selection widget (dropdown)
age_pie = st.selectbox("Select Age for Pie Chart", options=["All Ages"] + list(range(13, 20)))

# Filter teenagers by selected age
if age_pie == "All Ages":
    df_pie = DF[(DF["Age"] >= 13) & (DF["Age"] <= 19)]
else:
    df_pie = DF[DF["Age"] == age_pie]

# Count number of teenagers in each Addiction Category
counts = df_pie["Addiction Category"].value_counts().reset_index()
counts.columns = ["Addiction Category", "Count"]

# Explicitly set category order
order = ["Low", "Medium", "High"]
counts["Addiction Category"] = pd.Categorical(
    counts["Addiction Category"], categories=order, ordered=True
)

fig, ax = plt.subplots(figsize=(7,7))
ax.pie(
    counts["Count"],
    labels=counts["Addiction Category"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#8fd9b6", "#f6c85f", "#ff6f61"]  # optional custom colors
)
ax.set_title(f"Percentage of Teenagers ({age_pie}) by Addiction Category")

# Show chart in Streamlit
st.pyplot(fig)

st.subheader("Scatter Plot")

# Age selection widget (dropdown)
age_reg = st.selectbox("Select Age for Regression Plot", options=["All Ages"] + list(range(13, 20)))
#df_reg = DF[DF["Age"] == age_reg]

if age_reg == "All Ages":
    df_reg = DF[(DF["Age"] >= 13) & (DF["Age"] <= 19)]
    age_label = "All Ages"
else:
    df_reg = DF[DF["Age"] == age_reg]
    age_label = f"Age {age_reg}"

# Title using safe label
st.markdown(f"**Addiction Level vs Daily Social Media Usage per hour for {age_label}**")

# Create regression plot
fig, ax = plt.subplots(figsize=(8,6))
sns.regplot(
    x="Daily Social Media per hour",
    y="Addiction Level",
    data=df_reg,
    scatter_kws={"alpha":0.6},
    line_kws={"color":"red"},
    ax=ax
)

ax.set_title("Relationship between Addiction Level and Daily Social Media Usage")
ax.set_xlabel("Daily Social Media per hour")
ax.set_ylabel("Addiction Level")

# Show chart in Streamlit
st.pyplot(fig)

# Age selection widget (dropdown)
age_usage = st.selectbox(
    "Select Age for Regression Plot",
    options=["All Ages"] + list(range(13, 20)),
    key="age_regression_select"   # ✅ unique key
)

if age_usage == "All Ages":
    df_usage = DF[(DF["Age"] >= 13) & (DF["Age"] <= 19)]
    age_mark = "All Ages"
else:
    df_usage = DF[DF["Age"] == age_reg]
    age_mark = f"Age {age_reg}"

# Title using safe label
st.markdown(f"**Addiction Level vs Sleep Hours for {age_mark}**")

#st.markdown("**Addiction Level vs Sleep Hours**")
# Create regression plot
fig, ax = plt.subplots(figsize=(8,6))
sns.regplot(
    x="Sleep Hours",
    y="Addiction Level",
    data=DF,
    scatter_kws={"alpha":0.6},
    line_kws={"color":"red"},
    ax=ax
)

ax.set_title("Relationship between Addiction Level and Sleep Hours")
ax.set_xlabel("Sleep Hours")
ax.set_ylabel("Addiction Level")

# Show chart in Streamlit
st.pyplot(fig)

#Bar chart
st.subheader("Bar Chart")
st.markdown("**Average Addiction Level by Social Interaction Category**")

age_bar = st.selectbox(
    "Select Age for Bar Chart",
    options=["All Ages"] + list(range(13, 20)),
    key="age_bar_select"          # different unique key for bar chart
)

if age_reg == "All Ages":
    df_reg = DF[(DF["Age"] >= 13) & (DF["Age"] <= 19)]
    age_reg_label = "All Ages"
else:
    df_reg = DF[DF["Age"] == age_reg]
    age_reg_label = f"Age {age_reg}"
    
# Create bar plot
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(
    data=df_reg, 
    x='Social Interaction Level', 
    y='Addiction Level', 
    hue='Social Interaction Level',   # Explicitly sets hue to match x
    order=['low', 'medium', 'high'],
    palette='Blues_r',
    errorbar=None,
    ax=ax
)

# Add labels and title
ax.set_title('Average Social Media Addiction Level by Social Interaction Category',
             fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Real-World Social Interaction Level', fontsize=11)
ax.set_ylabel('Average Addiction Level Score', fontsize=11)

plt.tight_layout()

# Show chart in Streamlit
st.pyplot(fig)
# In[ ]:




