from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, config_list_from_json


# Load LLM configuration
config_list = config_list_from_json(env_or_file="../OAI_CONFIG_LIST.json")

# Create an AI assistant agent that generates Python code
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

# Create a debugging agent to check for errors
debugger = ConversableAgent("debugger")

# Create an optimization agent to improve the code
optimizer = ConversableAgent("optimizer")

# Create a user proxy agent that can execute Python code
user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding", "use_docker": False}
)

# Function for debugging code
def debug_code(message, sender):
    if "def" in message and "return" in message:
        return f"✅ Code looks syntactically correct, but let's test it: {message}"
    else:
        return "❌ There's an error in the generated code. Please fix it."

# Function for optimizing code
def optimize_code(message, sender):
    optimized_code = message.replace("*", "**2")  # Example optimization
    return f"✅ Optimized code:\n{optimized_code}"

# Register debug and optimize functions
debugger.register_reply(debug_code)
optimizer.register_reply(optimize_code)

# Step 1: Assistant generates Python function
user_proxy.initiate_chat(
    assistant,
    message="Write a Python function that takes a number as input and returns its square."
)

# Step 2: Debugger checks the code
user_proxy.initiate_chat(
    debugger,
    message="Here is the function the assistant provided. Please check for errors."
)

# Step 3: Optimizer refines the function
user_proxy.initiate_chat(
    optimizer,
    message="Please optimize this function to make it more efficient."
)

