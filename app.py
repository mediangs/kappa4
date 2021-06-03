import streamlit as st
from multiapp import MultiApp
import st_chart_anatomy, st_chart_g20_shaping, st_chart_g19 # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Canal Shaping", st_chart_g20_shaping.app)
app.add_app("G19", st_chart_g19.app)
app.add_app("Canal Anatomy", st_chart_anatomy.app)

# The main app
app.run()
