# Recipe Wizard 🧙‍♂️🍳

Welcome to **Recipe Wizard**, a web application that generates delicious recipes based on your input! Whether you're craving a chocolate cake or a vegan curry, Recipe Wizard has got you covered. Simply tell us what you want to cook and the cuisine style, and we'll provide you with a detailed recipe.

![Recipe Wizard Screenshot](![image](https://github.com/user-attachments/assets/acbf5e37-864f-455f-8354-96e6cc7e17ff)
)  


---

## Features ✨

- **Recipe Generation**: Input a dish name and cuisine style, and get a detailed recipe.
- **Dark Theme**: A sleek, modern dark theme for an enjoyable user experience.
- **Interactive UI**: Smooth animations and responsive design.
- **Customizable**: Easily modify the app to suit your needs.

---

## Technologies Used 🛠️

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **API**: Mira API (for recipe generation)
- **Deployment**: pending

---

## How to Use 🚀

1. **Visit the Website**:  
   Go to the hosted website (if deployed) or run the app locally.

2. **Input Your Preferences**:  
   - Enter the dish you want to cook (e.g., "chocolate cake").
   - Specify the cuisine or style (e.g., "French" or "vegan").

3. **Generate Recipe**:  
   Click the "Generate Recipe" button, and voilà! Your recipe will appear.

---

## Installation and Setup 🛠️

### Prerequisites
- Python 3.x
- Flask
- Mira API key (sign up at [Mira](https://mira.ai/) to get one)

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/recipe-wizard.git
   cd recipe-wizard

    Set Up a Virtual Environment (Optional but recommended):
    bash
    Copy

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install Dependencies:
    bash
    Copy

    pip install -r requirements.txt

    Set Up Environment Variables:

        Create a .env.ok file in the root directory.

        Add your Mira API key:
        plaintext
        Copy

        MIRA_API_KEY=your_mira_api_key_here

    Run the Application:
    bash
    Copy

    python app.py

    Access the App:
    Open your browser and go to http://127.0.0.1:5000/.
