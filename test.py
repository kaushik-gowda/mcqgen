import json
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from mcqgenrator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from mcqgenrator.MCQGenrator import generate_evaluate_chain

#loading json file
with open('C:\Users\Kaushik\mcqgen\experiment\response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

