import streamlit as st
import pandas as pd
from io import StringIO

import pandas as pd


file = pd.read_csv('linkedin-jobs-usa.csv')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # To read file as string:
    string_data = stringio.read()
    
    # ML code here

    st.write(output)

