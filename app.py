from flask import Flask, render_template, request
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

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

    # Parse the result and convert it to HTML
    recipe_html = format_recipe(result["result"])

    # Return the HTML
    return recipe_html
def format_recipe(recipe_text):
    """
    Convert the raw recipe text into HTML format.
    """
    # Split the recipe into sections
    sections = recipe_text.split("## ")

    html = ""
    for section in sections:
        if not section.strip():
            continue

        title = section.split("\n")[0].strip()
        content = "\n".join(section.split("\n")[1:]).strip()

        # Format sections
        if title == "Ingredients":
            html += f'<div class="section"><h2>{title}</h2><ul>'
            for line in content.split("\n"):
                if line.strip().startswith("-"):
                    html += f'<li>{line.strip()[1:].strip()}</li>'
            html += '</ul></div>'

        elif title == "Instructions":
            html += f'<div class="section"><h2>{title}</h2><ol>'
            for line in content.split("\n"):
                if line.strip().startswith("-"):
                    html += f'<li>{line.strip()[1:].strip()}</li>'
            html += '</ol></div>'

        elif title == "Tips and Variations":
            html += f'<div class="section"><h2>{title}</h2><ul class="tips">'
            for line in content.split("\n"):
                if line.strip().startswith("-"):
                    html += f'<li>🌟 {line.strip()[1:].strip()}</li>'
            html += '</ul></div>'

        else:
            html += f'<div class="section"><h2>{title}</h2><p>{content}</p></div>'

    return html
if __name__ == "__main__":
    app.run(debug=True)