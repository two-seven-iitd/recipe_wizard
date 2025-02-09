from flask import Flask, render_template, request
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os
import markdown  # Import the markdown library

# Load environment variables
load_dotenv(".env.ok")

# Initialize Flask app
app = Flask(__name__)

# Initialize MiraClient
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-recipe", methods=["POST"])
def generate_recipe():
    # Get user input from the form
    recipe = request.form.get("recipe")
    style = request.form.get("style")

    # Prepare input for Mira API
    input_dict = {"recipe": recipe, "style": style}

    # Execute the flow
    flow_name = "two-seven/recipe-maker"
    result = client.flow.execute(flow_name, input_dict)

    # Convert Markdown to HTML
    recipe_html = markdown.markdown(result["result"])

    # Return the HTML
    return recipe_html

if __name__ == "__main__":
    app.run(debug=True)
