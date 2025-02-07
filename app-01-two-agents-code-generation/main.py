from autogen import AssistantAgent, UserProxyAgent, config_list_from_json


# Load the LLM configuration (ensure you have API keys configured)
config_list = config_list_from_json(env_or_file="../OAI_CONFIG_LIST.json")

# Create an AI assistant agent
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

# Create a user proxy agent that can execute Python code
user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# Start a conversation where the user asks for Python code
user_proxy.initiate_chat(
    assistant,
    human_input_mode="NEVER",
    message="Write a Python function that takes a number as input and returns its square."
)

