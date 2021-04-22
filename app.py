import streamlit as st
from multiapp import MultiApp
from apps import home, syllabus, orientation, workshop # importing app modules

app = MultiApp()

# all applications for navigation
app.add_app("Home", home.app)
app.add_app("Syllabus", syllabus.app)
app.add_app("Orientation", orientation.app)
app.add_app("Workshop", workshop.app)

# The main app
app.run()
