
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv(".env.ok")

client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Basic test
version = "1.0.0"                                           # Optional specific version
# Load flow configuration

input_dict = {"recipe" :"pasta", "style":"italian"}                               # Prepare test input
if version:
    flow_name = f"two-seven/recipe-maker/{version}"
else:
    flow_name = "two-seven/recipe-maker"

result = client.flow.execute(flow_name, input_dict)         # Execute flow
print(result)

