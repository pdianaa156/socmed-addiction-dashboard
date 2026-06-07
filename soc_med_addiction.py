#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px

#st.image(r'C:\Users\Pter\Desktop\Dashboard\banner2.png')
st.image('banner2.png')

#st.date_input("Select a date")

st.title("""Welcome to my Dashboard""")

st.subheader("Prepared by:")
st.markdown("""
- **Putri Diana binti Abdul Rasyid** (2518420)  
- **Nur Khairina Najihah binti Haitul Nizam (251)**
""")

st.subheader("Project Background")
st.write("""In the modern digital era, social media platforms have changed from a mere communication tool into platforms that strongly influence daily human activity. Platforms such as Instagram, TikTok, and WhatsApp has engagement features like personalized content and constant notification that makes the users tend to constantly stay on their screen for a long period of time. As a result, younger groups, especially students in schools and universities become more vulnerable to addictive online behaviour. Although social media provides many benefits such as global communication, and educational sources, uncontrolled usage has become a growing concern around the world.\n 
Social media addiction is increasingly recognized as a behavioural dependency that involves a strong psychological focus on digital notifications, constant FOMO (Fear of Missing Out), and compulsive scrolling habits. This dependency can replace the important lifestyle habits in the teenagers and young adults that are necessary for healthy development. This addiction drives the user to excessively immerse in their screen and disrupt their normal sleep habits. The common habits of using screens before sleeping exposes users to blue light and increased mental stimulation, which studies have linked to shorter sleeping hour (Alshoaibi et al., 2023; Mohd Saat et al., 2024).\n
Aside from that, excessive social media usage also changes interpersonal relationships and social behaviour. As online engagement increases, face-to-face social interaction often decreases significantly, causing students to move away from meaningful real-world relationships and increasing feelings of social isolation. In addition, the combined effects of sleep deprivation and reduced social interaction may eventually affect students’ academic performance, such as CGPA which is student’s Cumulative Grade Point Average.\n
To address these growing lifestyle concerns, research-based and data-driven findings are needed to clearly identify how excessive digital usage leads to behavioural problems. This study uses an anonymous student dataset that records digital activity together with lifestyle outcomes, including addiction levels, night-time screen habits, sleep duration, and real-world social interaction indicators. By examining these connected variables, this mini project aims to identify the point at which normal social media use becomes harmful dependency, while also providing useful insights for academic counsellors, students, and educational policymakers who aim to restore healthy digital and academic balance.
""")

st.subheader("Project Objective")
st.markdown("""
- To examine the relationship between social media addiction and psychological well-being indicators, specially on students’ sleep duration and screen time before sleep.  (graph:  scatter plot with a tradeline)
- To investigate the consequences of excessive digital consumption by analyzing relationship between a student’s social media addiction and their social interaction level. (Clustered bar chart)
""")

#upload data
#upload_file = st.file_uploader("Please upload here:", type = 'csv')


#df = pd.read_csv(r"C:\Users\welcome\Desktop\BSMS1306\streamlit\Tips.csv")
df = pd.read_csv("Social_Media_Addiction.csv")
#df = pd.read_csv(upload_file)

#show data
st.subheader("Raw Data")
st.write(df)

DF = pd.read_csv('socmed_cleaned.csv')

#show data
st.subheader("Cleaned Data")
st.write(DF)

# Filter teenagers (age 13–19)
teenagers = DF[(DF["Age"] >= 13) & (DF["Age"] <= 19)]

# Count number of teenagers in each Addiction Category
counts = teenagers["Addiction Category"].value_counts().reset_index()
counts.columns = ["Addiction Category", "Count"]

# Explicitly set category order
order = ["Low", "Medium", "High"]
counts["Addiction Category"] = pd.Categorical(
    counts["Addiction Category"], categories=order, ordered=True
)

st.subheader("Pie Chart")
fig, ax = plt.subplots(figsize=(7,7))
ax.pie(
    counts["Count"],
    labels=counts["Addiction Category"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#8fd9b6", "#f6c85f", "#ff6f61"]  # optional custom colors
)
ax.set_title("Percentage of Teenagers by Addiction Category")

# Show chart in Streamlit
st.pyplot(fig)

st.subheader("Scatter Plot")
st.markdown("**Addiction Level vs Daily Social Media Usage per hour**")

# Create regression plot
fig, ax = plt.subplots(figsize=(8,6))
sns.regplot(
    x="Daily Social Media per hour",
    y="Addiction Level",
    data=DF,
    scatter_kws={"alpha":0.6},
    line_kws={"color":"red"},
    ax=ax
)

ax.set_title("Relationship between Addiction Level and Daily Social Media Usage")
ax.set_xlabel("Daily Social Media per hour")
ax.set_ylabel("Addiction Level")

# Show chart in Streamlit
st.pyplot(fig)

st.markdown("**Addiction Level vs Sleep Hours**")
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

# Create bar plot
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(
    data=DF, 
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

st.subheader("Discussion")
st.subheader("Conclusion")




