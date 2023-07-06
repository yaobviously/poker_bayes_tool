# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:23:42 2023

@author: yaobv
"""


import streamlit as st

from update_func import update_poker_beliefs


def main():

    st.title("Poker Belief Updater")

    # creating a sidebar and its sliders
    with st.sidebar:
        st.subheader("Input Parameters")
        hands = st.slider('Sample of Hands', min_value=1, max_value=100, value=15, help="Number of hands")
        raises = st.slider('Aggressive Actions', min_value=1, max_value=hands, help="Number of aggressive actions")
        value_perc = st.slider('Value Percentage', min_value=0.01, max_value=0.3, step=0.01, value=0.15, help="Percentage of natural (non-bluff) aggressive actions in opponent's range")
        prior = st.selectbox('Prior', ['beta_1', 'beta_2', 'beta_3', 'uniform'], help="Prior distribution")

    # calling the function 
    plot = update_poker_beliefs(hands, raises, value_perc, prior)

    # display plot
    st.pyplot(plot)
    
    # foter
    st.write("---")
    st.markdown("Created by [Jason Young](mailto:yaobviously@gmail.com)")
    st.markdown("Inspiration taken from [Think Bayes 2](https://allendowney.github.io/ThinkBayes2/) by Allen Downey")


if __name__ == '__main__':
    main()