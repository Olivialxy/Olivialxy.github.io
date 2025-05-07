import streamlit as st
import pandas as pd
import altair as alt

# -- Title --
st.title("Private Credit & Bank Risk Across Countries")
st.subheader("Author: Olivia Lai")

# -- Intro Paragraphs --
st.markdown("""
This interactive app lets you explore financial development and risk in over 200 countries using data from the World Bank's Global Financial Development Database.  
Our main focus is on two indicators:
- **Private credit by deposit money banks to GDP (%)**  
- **Non-performing loans to total gross loans (%)**

Use the controls below to compare countries across different years and see long-term trends.
""")

# -- Load Data --
df = pd.read_csv("GFDDData.csv")

# Filter indicators
indicator_codes = {
    "Private credit to GDP (%)": "GFDD.DI.01",
    "Non-performing loans (%)": "GFDD.SI.01"
}
df = df[df['Indicator Code'].isin(indicator_codes.values())]
years = [str(y) for y in range(2000, 2021)]
df_long = df.melt(
    id_vars=["Country Name", "Indicator Code"],
    value_vars=years,
    var_name="Year",
    value_name="Value"
).dropna()

# Pivot so indicators are columns
df_wide = df_long.pivot_table(
    index=["Country Name", "Year"],
    columns="Indicator Code",
    values="Value"
).reset_index()

df_wide.columns.name = None
df_wide = df_wide.rename(columns={
    "GFDD.DI.01": "Private Credit (% of GDP)",
    "GFDD.SI.01": "Non-performing Loans (%)"
})
df_wide["Year"] = df_wide["Year"].astype(int)

# -- Year Dropdown --
year_selected = st.selectbox("Choose a Year to Explore:", sorted(df_wide["Year"].unique()), index=15)
df_selected = df_wide[df_wide["Year"] == year_selected]

# -- Main Plot (Interactive Scatter) --
st.markdown("### Main Visualization: Credit vs. Risk")
scatter = alt.Chart(df_selected).mark_circle(size=80).encode(
    x="Private Credit (% of GDP)",
    y="Non-performing Loans (%)",
    tooltip=["Country Name", "Private Credit (% of GDP)", "Non-performing Loans (%)"]
).interactive().properties(
    width=700,
    height=400
)
st.altair_chart(scatter)

# -- Country Selector for Trend Line --
st.markdown("### Explore Credit Trends Over Time")
country_list = sorted(df_wide["Country Name"].unique())
selected_country = st.selectbox("Choose a Country:", country_list)

df_country = df_wide[df_wide["Country Name"] == selected_country]

line = alt.Chart(df_country).mark_line().encode(
    x="Year",
    y="Private Credit (% of GDP)",
    tooltip=["Year", "Private Credit (% of GDP)"]
).properties(width=700, height=300)

st.altair_chart(line)

# -- Contextual Visualizations --
st.markdown("### Contextual Visualizations")
st.image("context_chart1.png", caption="Source: World Bank — Bank Capital to Assets Ratio by Income Group (GFDD.SI.07)")
st.image("context_chart2.png", caption="Source: World Bank — Domestic Credit to Private Sector by Banks (% of GDP) (FS.AST.PRVT.GD.ZS)")


# -- Data Sources & Notebook --
st.markdown("### Data Sources")
st.markdown("""
- **Primary Dataset**: Global Financial Development Database  
  https://datacatalog.worldbank.org/dataset/global-financial-development

- **Context Chart 1**: Bank Capital to Assets Ratio (GFDD.SI.07)  
  https://databank.worldbank.org/source/global-financial-development/Series/GFDD.SI.07

- **Context Chart 2**: Domestic Credit to Private Sector by Banks (% of GDP) (FS.AST.PRVT.GD.ZS)  
  https://databank.worldbank.org/source/jobs/Series/FS.AST.PRVT.GD.ZS

""")


st.markdown("[View the Jupyter notebook used for analysis](notebook_link.txt)")
