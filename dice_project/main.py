import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import numpy as np

st.title('Roll the Die!')
st.divider()

with st.container():
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        def load_lottiefile(filepath: str):
            with open(filepath, 'r') as f:
                return json.load(f)
                    
        lottie_coading = load_lottiefile('resourse/dice_animation_1.json')
        st_lottie(lottie_coading, speed=1, reverse=False,loop=False, quality='high', height=None, width=None)

    with c3:
        def dice():
            choice = np.random.randint(1,7)
            return st.header(choice)
            
        if st.button('Click to Roll'):
            dice()
st.divider()
