from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv(".env.ok")

client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Basic test
version = "1.0.0"                                           # Optional specific version
# Load flow configuration

input_dict = {"recipe" :"pasta", "style":"italian"} 
# Basic test
flow = Flow(source="recipe.yaml")                    # Load flow configuration
                            # Prepare test input
response = client.flow.test(flow, input_dict)               # Test flow
print(response)