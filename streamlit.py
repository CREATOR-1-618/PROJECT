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
                               ["Streets with the highest congestion", "The average car density of the city", "Average time needed", "Mouhamadou", "Anicette", "Megane"],
                               icons=['signpost', 'car-front', 'alarm', 'person', 'person', 'person'
                                      ], menu_icon="cast")

    st.title("Welcome to Beijing Traffic Analysis ")


    if selected == "Streets with the highest congestion":
        file = pd.read_feather('dataf.csv')
        st.title('Streets with the highest congestion')
        highest_congestion(file)

    if selected == "The average car density of the city":
        file = pd.read_feather('dataf.csv')
        st.title("The average car density of the city")
        car_density(file)









