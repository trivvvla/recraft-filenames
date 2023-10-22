from flask import Flask, render_template, request
import dearpygui.dearpygui as dpg

app = Flask(__name__)

@app.route('/')
def index():
    # Clear any previous DPG data
    dpg.cleanup()
    
    # Create Dear PyGui items
    with dpg.handler_registry():
        with dpg.window(label="Music Organizer"):
            dpg.add_text("Welcome to the Music Organizer!")
            dpg.add_button(label="Select Directory", callback=select_directory)
            dpg.add_button(label="Run Features", callback=run_features)
    
    # Render Dear PyGui to HTML
    rendered_html = dpg.render_dearpygui_frame()

    return rendered_html

def select_directory(sender, app_data):
    # Your logic to select directory here
    pass

def run_features(sender, app_data):
    # Your logic to run features here
    pass

if __name__ == '__main__':
    app.run(debug=True)
