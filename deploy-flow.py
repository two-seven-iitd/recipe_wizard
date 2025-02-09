
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
     # Initialize Mira Client
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv(".env.ok")
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})
# Basic test
flow = Flow(source="recipe.yaml")                    # Load flow configuration

try:
    client.flow.deploy(flow)                                # Deploy to platform
except FlowError as e:
    print(f"Error occurred: {str(e)}") 
