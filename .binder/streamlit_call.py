from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('data_analysis_trading/')
    Popen(["streamlit", "run", "trading.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
