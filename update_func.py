# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:30:28 2023

@author: yaobv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import beta, binom

def update_poker_beliefs(hands: int, raises: int, value_perc: float, prior: str) -> None:
    
    possible_bluff_freq = np.linspace(0.00, 1.0, 101)
    
    prior_dict = {
        'beta_1' : beta.pdf(possible_bluff_freq, 1, 3),
        'beta_2' : beta.pdf(possible_bluff_freq, 2, 5),
        'beta_3' : beta.pdf(possible_bluff_freq, 4, 10),
        'uniform' : np.full(len(possible_bluff_freq), 1)
    }
    prior = prior_dict[prior]
    prior = prior / prior.sum()
    
    val_bet_probs = []
    
    bluff_df = pd.DataFrame()
    
    for val in np.arange(0, raises + 1):
        
        prob_val_ = binom.pmf(val, hands, value_perc)
        prob_bluffs_ = pd.Series(binom.pmf(raises-val, hands-val, possible_bluff_freq))
        prob_bluffs_.name = f'{raises - val}_bluffs'        
        
        val_bet_probs.append(prob_val_)
        bluff_df = pd.concat([bluff_df, prob_bluffs_], axis=1)
        
    # normalizing the value bet probabilities
    # these are the probabilities of value bets given value bet %
    # and they're used to weight the bluffing frequencies
    val_bet_probs = np.array(val_bet_probs)
    val_bet_probs = val_bet_probs / val_bet_probs.sum()
    
    # multiplying each bluff count by its probability of occurring
    bluff_df = bluff_df * val_bet_probs
    
    # getting the total weighted likelihood for each bluff frequency
    bluff_df['total_prob'] = bluff_df.sum(axis=1)
    
    # getting the unnormed posterior and normalizing it
    unnormed = bluff_df['total_prob'] * prior
    posterior = unnormed / unnormed.sum()
    
    # creating the plot object
    fig, ax = plt.subplots(figsize=(5, 3))
    plt.title(f"Update After {raises} XR in {hands} hands")
    plt.plot(possible_bluff_freq, posterior, label="posterior")
    plt.plot(possible_bluff_freq, prior, label="prior")
    plt.xlabel("Opponent's Bluffing Frequency")
    plt.legend()

    # returning it for streamlit
    return fig