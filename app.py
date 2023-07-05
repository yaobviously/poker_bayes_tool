# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:23:42 2023

@author: yaobv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from scipy.stats import beta, binom
from update_func import update_poker_beliefs


def main():

    st.title("Poker Belief Updater")

    # creating a sidebar and its sliders
    with st.sidebar:
        st.subheader("Input Parameters")
        hands = st.slider('Sample of Hands', min_value=1, max_value=100, value=15, help="Number of hands")
        raises = st.slider('Aggressive Actions', min_value=1, max_value=hands, value=4, help="Number of aggressive actions")
        value_perc = st.slider('Value Hands', min_value=0.01, max_value=0.3, step=0.01, value=0.15, help="Percentage of value hands")
        prior = st.selectbox('Prior', ['beta_1', 'beta_2', 'beta_3', 'uniform'], help="Prior distribution")

    # calling the function 
    plot = update_poker_beliefs(hands, raises, value_perc, prior)

    # display plot
    st.pyplot(plot)


if __name__ == '__main__':
    main()