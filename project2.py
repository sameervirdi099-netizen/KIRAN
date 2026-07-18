#from turtle import left, right

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from mpl_toolkits.mplot3d import Axes3D
import requests
import base64

    
st.set_page_config(
    page_title="Social Media Usage",
    layout="wide"
)

def load_data(uploaded_file=None):
    if uploaded_file is None:
        try:
            return pd.read_csv("t.csv")
        except Exception:
            return None
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    if uploaded_file.name.endswith((".xls", ".xlsx")):
        return pd.read_excel(uploaded_file)
    return None

def style_fig(fig, title="", height=450):
    fig.update_layout(
        title=title,
        height=height,
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig

if "df" not in st.session_state:
    st.session_state.df = None
sample_df = load_data(None)
df = st.session_state.df if st.session_state.df is not None else sample_df
if df is None:
    st.error("No data available. Please upload a CSV or Excel dataset.")
    st.stop()
# ...existing code...


def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def set_background(image_file):
    encoded = encode_image_to_base64(image_file)
st.markdown("""
<style>

.stApp{
    background:#120136;
    color:white;
}

.hero{
    background:linear-gradient(90deg,#3C096C,#7B2CBF,#9D4EDD);
    color:white;
    border-radius:20px;
    padding:40px;
}

.metric-card{
    background:#240046;
    border:1px solid #9D4EDD;
    border-radius:18px;
    padding:20px;
}
/* Hero Banner */
.hero{
    background: linear-gradient(135deg,#2563EB,#7C3AED);
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:25px;
    box-shadow:0px 10px 25px rgba(0,0,0,.35);
}

.hero h1{
    font-size:45px;
    margin-bottom:10px;
}

.hero p{
    font-size:20px;
    color:white;
}

/* KPI Cards */
.metric-card{
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.2);
    border-radius:20px;
    padding:25px;
    text-align:center;
    transition:.3s;
    box-shadow:0 8px 20px rgba(0,0,0,.25);
}

.sidebar-title {
            text-align: center;
            font-size: 1.8rem;
            font-weight: 800;
            color: #F5F5F5;
            padding-top: 20px;
            padding-bottom: 10px;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
        }
        
        .sidebar-divider {
            border: none;
            border-top: 1px solid #3a3a3a;
            margin: 0px 10px 15px 10px;
        }
.metric-card:hover{
    transform:translateY(-8px);
    box-shadow:0 15px 30px rgba(37,99,235,.5);
}

.metric-title{
    color:#CBD5E1;
    font-size:18px;
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:bold;
}

/* Section Titles */

.section{
    color:white;
    font-size:32px;
    font-weight:700;
    margin-top:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    
}

</style>
""",unsafe_allow_html=True)


with st.sidebar:
    st.markdown('<div class="sidebar-title">Teen Mental Health Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    set_background("background.png")
    opt = option_menu(
    "",
    options=["🏠Home","Dataset","📊Visualization","💡Insights","📌About"],
    icons=["house","file-text","activity","lightbulb","person"],
    default_index=0,
    styles={
            "container": {"padding": "0!important", "background-color": "#0b0a0a"},
            "icon": {"color": "#DFEDF3", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px 0px",
                "color": "#f5f5f5",
                "padding": "12px",
                "border-radius": "8px",
                "--hover-color": "#F5E1E1",
            },
       
        "nav-link-selected": {"background-color": "#060845", "color": "#ede5e5", "font-weight": "700"},
    
       }
    )       
    
if opt=="🏠Home":


    set_background("background.png") 
    col1, col2 = st.columns([3, 1])

    with col1:
     st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
        Teen Mental Health &<br>
        Social Media Usage Dashboard
        
    </h1>
    """, unsafe_allow_html=True)

    with col2:
     st.image("image 2.jpeg")
    st.markdown("""
        
        """, unsafe_allow_html=True)
   
    st.markdown("""
<p style="font-size:24px; line-height:1.8; color:white;">
Welcome to the <b>Teen Mental Health & Social Media Usage Dashboard</b>. This interactive dashboard explores how social media habits may influence the mental health and daily lifestyle of teenagers.
With the help of data visualization and statistical analysis, this project provides meaningful insights into screen time, sleep patterns, physical activity, and other factors related to teen well-being.
<br><br>
</p>
""", unsafe_allow_html=True)

#     st.write("""
 

# ## Welcome!

# Welcome to the **Teen Mental Health & Social Media Usage Dashboard**. This interactive dashboard explores how social media habits may influence the mental health and daily lifestyle of teenagers.

# With the help of data visualization and statistical analysis, this project provides meaningful insights into screen time, sleep patterns, physical activity, and other factors related to teen well-being.
#      """)
    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
    🎯 Project Objectives
    
    </h1>
    """, unsafe_allow_html=True)
   

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💡Analyze teenagers social media usage patterns</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📋Compare usage across different social media platforms</div>
        <div class={len(df)}</div>
    
    
     </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📵Present findings through interactive charts and visualizations</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🧠Analyzing the Impact of Social Media Usage on Teen Mental  Health </div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
     st.divider()
    st.image("image 1.jpeg",use_column_width=True)
    st.markdown("""
    <h1 style="color:white; font-size:45px;">
    📊 Dashboard Overview
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)
    
    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈interactive data filtering </div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
  
    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🧬Correlation heatmaps & graphs</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💡Key insights and conclusions</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
     
    <div class="metric-card">
        <div class="metric-title">🧭Easy-to-use navigation</div>
    <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
   
    st.write("""
    🌍 Why This Project Matters""")
    st.markdown(""" 
<p style="font-size:24px; line-height:1.8; color:white;">
Social media plays a significant role in the lives of teenagers. While it offers opportunities for communication, learning, and entertainment, excessive usage can affect sleep, physical activity, stress levels, and overall mental well-being. This dashboard helps users better understand these patterns through data-driven insights.
<br><br>
</p>
""", unsafe_allow_html=True)

    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
     🤳 Applications Used in this project
    </h1>
    """, unsafe_allow_html=True)

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)
    
    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Python</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
     
    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Streamlit</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Pandas</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Seaborn</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
### 💡 Explore the Dashboard""")
    st.markdown("""
<p style="font-size:24px; line-height:1.8; color:white;">
Use the navigation menu on the left to explore the dataset, visualize trends, discover insights, and learn more about the relationship between social media usage and teen mental health.
"Understanding data today helps build healthier digital habits for tomorrow."    
<br><br>
</p>
""", unsafe_allow_html=True)
    st.markdown("---")

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Teenagers</div>
        <div class="metric-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📱 Avg Usage</div>
        <div class="metric-value">{df['daily_social_media_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">😴 Sleep</div>
        <div class="metric-value">{df['sleep_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏃 Activity</div>
        <div class="metric-value">{df['physical_activity'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    # col1.metric("👥 Total Teenagers",len(df))
    # col2.metric("📱 Avg Social Media Hours",round(df["daily_social_media_hours"].mean(),2))
    # col3.metric("😴 Avg Sleep Hours",round(df["sleep_hours"].mean(),2))
    # col4.metric("🏃 Avg Physical Activity",round(df["physical_activity"].mean(),2)) 
    from streamlit_lottie import st_lottie
    import requests

    url = "https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json"

    animation = requests.get(url).json()

    st_lottie(animation, height=350)

elif opt== "Dataset":
    
    
    set_background("black.png")   
    st.markdown('<div class="page-subtitle"></div>', unsafe_allow_html=True)

    # st.markdown('<div class="section-heading-sm">📁 Upload Dataset</div>', unsafe_allow_html=True)
    # uploaded_file = st.file_uploader("Upload Teen Mental Health Dataset(CSV or Excel)", type=["csv", "xlsx"])

    # if uploaded_file:
    #     new_df = load_data(uploaded_file)
    #     if new_df is not None:
    #         st.session_state.df = new_df
    #         st.success(f"File '{uploaded_file.name}' uploaded successfully — {len(new_df):,} rows loaded.")
        # else:
        #     st.error("Could not read that file. Please check the format and try again.")

    active_df = st.session_state.df if st.session_state.df is not None else load_data(None)

    if active_df is None:
        st.info("No dataset available yet — upload a CSV or Excel file above to get started.")
    else:
        if st.session_state.df is None:
            st.info("Showing the bundled sample dataset (`t.csv`). "
                    "Upload your own file above to replace it.")

        df = active_df
        n_rows_total = len(df)
        n_cols_total = df.shape[1]
        n_duplicates = int(df.duplicated().sum())
        n_missing = int(df.isna().sum().sum())

        st.markdown('<div class="section-heading-sm">📋 Dataset Summary</div>', unsafe_allow_html=True)
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_rows_total:,}</div>'
                        f'<div class="kpi-label">Rows</div></div>', unsafe_allow_html=True)
        with k2:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_cols_total}</div>'
                        f'<div class="kpi-label">Columns</div></div>', unsafe_allow_html=True)
        with k3:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_duplicates:,}</div>'
                        f'<div class="kpi-label">Duplicate Rows</div></div>', unsafe_allow_html=True)
        with k4:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_missing:,}</div>'
                        f'<div class="kpi-label">Missing Values</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-heading-sm">📄 Dataset</div>', unsafe_allow_html=True)

        slider_max = max(n_rows_total, 1)
        default_rows = min(20, slider_max)
        n_rows = st.slider("Rows to preview", min_value=1, max_value=slider_max, value=default_rows)

        tab1, tab2, tab3 = st.tabs(["🔍 Preview", "🧬 Column Info", "🔢 Value Counts"])

        with tab1:
            st.dataframe(df.head(n_rows), width="stretch")
            st.image("image 4.jpeg",use_column_width=True)

        with tab2:
            col_info = pd.DataFrame({
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str).values,
                "Non-Null Count": df.notna().sum().values,
                "Null Count": df.isna().sum().values,
                "Unique Values": [df[c].nunique() for c in df.columns],
            })
            st.dataframe(col_info, width="stretch", hide_index=True)

        with tab3:
            default_col = "Platform" if "Platform" in df.columns else df.columns[0]
            vc_col = st.selectbox("Choose a column", options=df.columns.tolist(),
                                   index=df.columns.tolist().index(default_col))
            vc = df[vc_col].value_counts().reset_index()
            vc.columns = [vc_col, "Count"]
            st.dataframe(vc, width="stretch", hide_index=True)
            

            if df[vc_col].nunique() <= 40:
                vc_chart = vc.head(20).sort_values("Count")
                fig_vc = go.Figure(go.Bar(x=vc_chart["Count"], y=vc_chart[vc_col].astype(str), orientation="h"))
                fig_vc.update_xaxes(title_text="Count")
                fig_vc.update_yaxes(title_text="")
                st.plotly_chart(style_fig(fig_vc, f"Value Counts — {vc_col}", height=min(500, 100 + 28 * len(vc_chart))), width="stretch")
            else:
                st.caption(f"'{vc_col}' has {df[vc_col].nunique():,} unique values — too many to chart, showing the table above instead.")
                
elif opt=="📊Visualization":
    
    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
        Teen Mental Health &<br>
        Social Media Usage
        
        
    </h1>
    """, unsafe_allow_html=True)
    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Teenagers</div>
        <div class="metric-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📱 Avg Usage</div>
        <div class="metric-value">{df['daily_social_media_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">😴 Sleep</div>
        <div class="metric-value">{df['sleep_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏃 Activity</div>
        <div class="metric-value">{df['physical_activity'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)
     
     
    # col1.metric("👥 Total Teenagers",len(df))
    # col2.metric("📱 Avg Social Media Hours",round(df["daily_social_media_hours"].mean(),2))
    # col3.metric("😴 Avg Sleep Hours",round(df["sleep_hours"].mean(),2))
    # col4.metric("🏃 Avg Physical Activity",round(df["physical_activity"].mean(),2))
    t1,t2,t3,t4,t5,t6=st.tabs(["📊Histogram","📈Line chart","📌Scatter Plot", "💡Bar Chart","🧩Pie Chart","Graphs"])
    st.markdown("---")
    
    with t1:
        st.subheader("📊 Age Distribution")

        fig = px.histogram(
          df,
         x="age",
         nbins=15,
         color_discrete_sequence=px.colors.sequential.Viridis
         )

        st.plotly_chart(fig, use_container_width=True)
        

        
    with t2:
       st.subheader("📉 Average Stress by Age")

       avg = df.groupby("age")["stress_level"].mean().reset_index()

       fig = px.line(
        avg,
         x="age",
         y="stress_level",
         markers=True,
         color_discrete_sequence=["#00CC96"]
        )

       st.plotly_chart(fig, use_container_width=True)
    with t3:
      
       st.subheader("📍 Sleep Hours vs Stress Level")

       fig = px.scatter(
             df,
             x="sleep_hours",
             y="stress_level",
             color="gender",
             hover_data=["age", "platform_usage"],
             template="plotly_white",
             color_discrete_sequence=px.colors.qualitative.Bold,
             title="Sleep Hours vs Stress Level"
             )

       st.plotly_chart(fig, use_container_width=True)
    
    with t4:
    #   st.subheader("Gender Distribution
        st.subheader("📈 Gender Distribution")

        gender = df["gender"].value_counts().reset_index()
        gender.columns = ["gender","count"]

        fig = px.bar(
               gender,
             x="gender",
             y="count",
             color="gender",
             color_discrete_sequence=px.colors.qualitative.Set2
             )

        st.plotly_chart(fig, use_container_width=True)
      
        st.subheader("Charts")
        st.subheader("Stress Level Distribution ")
        fig,ax=plt.subplots()
        df["stress_level"].value_counts().plot(kind="bar",ax=ax)

        ax.set_xlabel("stress level")
        ax.set_ylabel("count")
        st.pyplot(fig)
    
    with t5:
      st.subheader("🥧 Gender Distribution")

      fig = px.pie(
         df,
          names="gender",
         color_discrete_sequence=px.colors.qualitative.Pastel
         )

      st.plotly_chart(fig, use_container_width=True)
      
    with t6:
       st.subheader("🔥 Correlation Heatmap")

       corr = df.corr(numeric_only=True)

       fig = px.imshow(
          corr,
         text_auto=True,
         color_continuous_scale="RdBu_r"
        )     

       st.plotly_chart(fig, use_container_width=True)
       

       
       st.subheader("🌞 Sunburst Chart")

       fig = px.sunburst(
         df,
          path=["gender","stress_level"],
         color="stress_level",
         color_continuous_scale="Turbo"
         )

       st.plotly_chart(fig, use_container_width=True)
elif opt=="💡Insights":
    
    set_background("black.png")   # Your background image
    url = "https://assets3.lottiefiles.com/packages/lf20_kkflmtur.json"

    animation = requests.get(url).json()

    st_lottie(animation, height=300)
    st.title("📌 Key Insights")

    st.success("✔ Teenagers spend an average of {:.2f} hours per day on social media.".format(df["daily_social_media_hours"].mean()))

    st.success("✔ Average sleep hours: {:.2f}".format(df["sleep_hours"].mean()))

    st.success("✔ Average physical activity: {:.2f} hours".format(df["physical_activity"].mean()))

    st.info("📱 Most used social media platform:")

    st.write(df["platform_usage"].value_counts())
   
    

     
    st.subheader("💡 Key Insights")
    st.subheader("📱 Social Media Usage")
    st.write("""Average daily social media usage is X hours.
        Most teenagers spend a significant portion of their day on social media.
        Most popular platform: Instagram/YouTube/TikTok""")
    st.subheader("😴 Sleep Patterns")
    st.write(""" Teenagers with higher social media usage tend to have fewer sleep hours.
        Maintaining healthy sleep habits is important for physical and mental well-being.""")
    st.subheader("   🏃 Physical Activity")
    st.write("""Physical activity levels vary among teenagers.
        Regular exercise may help support better mental health.""")
    st.subheader(" 👥 Gender Comparison")
    st.write(""" Compare average social media usage by gender.
        Highlight any noticeable differences in sleep or activity levels, if present.""")
    st.subheader("  🧠 Mental Health")
    st.write("""Observe how social media usage relates to the mental health labels in the dataset.
        Emphasize that the dashboard shows patterns and associations, not proof that one factor causes another.""")
    st.subheader(" 📊 Correlation Highlights")
    st.write(""" Mention any strong positive or negative correlations found in the heatmap.
        Explain them in simple language.""")
        

    st.subheader("Example:")

    st.write("""    A negative correlation between sleep hours and social media usage suggests that teenagers who spend more time on social media often report less sleep.

        📌 Main Findings
        Most teenagers use social media every day.
        Sleep duration may decrease as social media usage increases.
        Physical activity differs across individuals.
        Different platforms have different usage patterns.
        The dashboard helps identify trends that may support awareness and further research.
        💬 Recommendations
        Limit excessive daily screen time.
        Maintain a consistent sleep schedule.
        Balance online activities with outdoor exercise.
        Take regular breaks from social media.
        Encourage open conversations about mental health.""")

    st.subheader("🎯 Final Conclusion")

    st.write("""
    -This dashboard provides an interactive analysis of teen social media usage and its relationship with lifestyle and mental health indicators. The findings suggest that balanced social media use, healthy sleep habits, and regular physical activity are important for overall well-being. These insights can help students, parents, educators, and researchers better understand behavioral trends and encourage healthier digital habits.
    """)   
    from streamlit_lottie import st_lottie
    import requests

    url="https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json"

    animation=requests.get(url).json()

    st_lottie(animation,height=250)
elif opt=="📌About":
    
    set_background("background.png")   # Your background image
    st.title("")
    url = "https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json"

    animation = requests.get(url).json()

    st_lottie(animation, height=280)
    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
    📌 About This Project
    </h1>
    """, unsafe_allow_html=True)
    st.write("""
### Project Objective

This dashboard analyzes how social media usage affects teenagers'
mental health.

### Tools Used

- Python
- Streamlit
- Pandas
- Seaborn
- Plotly

### Dataset

Teen Mental Health & Social Media Usage Dataset

### Developed By

Amit
""")
    """

🌱 "Mental health is not a destination, but a journey."

Made with ❤️ using Streamlit
""",

   
st.markdown("---")

st.markdown(
"""
""",
unsafe_allow_html=True
)
