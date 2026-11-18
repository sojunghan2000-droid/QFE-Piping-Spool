"""Streamlit entry point for the QFE Piping Spool dashboard.

The dashboard is a self-contained HTML page. Uploaded workbooks are parsed by
JavaScript in the viewer's browser and are never sent to the Streamlit server.
"""

from pathlib import Path

import streamlit as st

DASHBOARD = Path(__file__).with_name("QFE_dashboard_prototype.html")

st.set_page_config(
    page_title="QFE Piping Spool Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      header[data-testid="stHeader"] { display: none; }
      [data-testid="stMain"] { overflow: hidden; }
      [data-testid="stMainBlockContainer"] { padding: 0; max-width: 100%; }
      [data-testid="stVerticalBlock"] { gap: 0; }
      [data-testid="stElementContainer"]:has(style) { display: none; }
      iframe { display: block; height: 100vh !important; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.iframe(DASHBOARD, height=900, alt="QFE Piping Spool Dashboard")
