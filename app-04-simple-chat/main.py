# 1. Import our agent class
import os
from autogen import ConversableAgent


# 2. Define our LLM configuration for OpenAI's GPT-4o mini
#    Provider defaults to OpenAI and uses the OPENAI_API_KEY environment variable
llm_config = {
    "config_list": [
        {
            "api_type": "openai",
            "model": "gpt-4o-mini",
            "api_key": os.environ["OPENAI_API_KEY"]
        }
    ],
}

# 3. Create our agent
my_agent = ConversableAgent(
    name="helpful_agent",
    llm_config=llm_config,
    system_message="You are a poetic AI assistant, respond in rhyme.",
)

# 4. Create an agent to represent you
human_agent = ConversableAgent(
    name="user",
    human_input_mode="ALWAYS",
)

# 5. Chat with our agent
human_agent.initiate_chat(
    recipient=my_agent,
    message="In one sentence, what's the big deal about AI?"
)
