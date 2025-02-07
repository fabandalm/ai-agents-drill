import autogen

config_list = autogen.config_list_from_json(
    env_or_file="../OAI_CONFIG_LIST.json"
)

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config={
        "config_list": config_list
    }
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change using yahoo finance api.")


