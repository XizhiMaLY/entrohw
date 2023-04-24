import streamlit as st
import pandas as pd
from io import StringIO

from google.cloud import storage
import pandas as pd

# Set the name of your GCS bucket and the name of the CSV file
BUCKET_NAME = 'entrop_hw_resume'
CSV_FILE_NAME = 'linkedin-jobs-usa.csv'

# Create a client instance
client = storage.Client()

# Get the bucket containing your file
bucket = client.get_bucket(BUCKET_NAME)

# Get the blob (file) object for your CSV file
blob = bucket.get_blob(CSV_FILE_NAME)

# Download the contents of the blob as a string
csv_contents = blob.download_as_string().decode('utf-8')

# Parse the string contents into a Pandas DataFrame
df = pd.read_csv(pd.compat.StringIO(csv_contents))



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # To read file as string:
    string_data = stringio.read()
    
    # ML code here

    st.write(output)

