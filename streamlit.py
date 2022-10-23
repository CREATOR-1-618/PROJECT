import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import matplotlib

# Functions
def highest_congestion(data):
    cong = data.groupby(["adresse"]).agg({"Id_x": 'count'})
    cong10 = cong.sort_values(by=['Id_x'], ascending=False).head(10)
    fig = px.bar(cong10)
    st.plotly_chart(fig)

def car_density(data):
    densi = data.groupby(["adresse"]).agg({"Id_x": lambda x: x.nunique()})
    densi10 = densi.sort_values(by=['Id_x'], ascending=False).head(10)
    fig = px.bar(densi10)
    st.plotly_chart(fig)

if __name__ == "__main__":

    with st.sidebar:
        selected = option_menu("Trafic Analysis",
                               ["Traffic analysis"],
                               icons=['signpost'], menu_icon="cast", default_index=1)

    st.title("Welcome to Beijing Traffic Analysis ")


    if selected == "Traffic Analysis":
        file = pd.read_feather('dataf.csv')

        st.title("The average car density of the city")
        car_density(file)









