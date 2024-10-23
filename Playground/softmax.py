import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit as st

# Softmax function
def my_softmax(z):
    return np.exp(z) / np.sum(np.exp(z), axis=0)

# Streamlit app

st.markdown('<h1 style="text-align: center; " >Softmax Visualization</h1>   ', unsafe_allow_html=True)
st.write('\n')
st.image('https://miro.medium.com/v2/resize:fit:1400/1*de5BTgQXIV2uLckxrkN85Q.png', use_column_width=True)


st.info("####  *Change the values of z from the sidebar and see the output*")
st.sidebar.header("Z values")

# Inputs
z0 = st.sidebar.slider("z0", 0, 10, 1)
z1 = st.sidebar.slider("z1", 0, 10, 5)
z2 = st.sidebar.slider("z2", 0, 10, 2)
z3 = st.sidebar.slider("z3", 0, 10, 1)

# Input array
z_values = np.array([z0, z1, z2, z3])

# Softmax output
a_values = my_softmax(z_values)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# Bar chart for z inputs
z_names = ['z0', 'z1', 'z2', 'z3']
ax[0].barh(z_names, z_values, color='blue')
ax[0].set_xlim([0, 10])
ax[0].set_title("z input to softmax")

# Bar chart for softmax output
a_names = ['a0', 'a1', 'a2', 'a3']
ax[1].barh(a_names, a_values, color='red')
ax[1].set_xlim([0, 1])
ax[1].set_title("softmax(z)")

# Display the plot in Streamlit
st.pyplot(fig)


