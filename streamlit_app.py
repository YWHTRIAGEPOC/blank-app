import streamlit as st
import streamlit.components.v1 as components

with open("test.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=600, scrolling=True)
