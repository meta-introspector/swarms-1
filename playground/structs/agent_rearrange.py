from swarms import Agent, AgentRearrange, rearrange, Anthropic


# Initialize the director agent

director = Agent(
    agent_name="Director",
    system_prompt="Directs the tasks for the workers",
    llm=Anthropic(),
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="<DONE>",
    state_save_file_type="json",
    saved_state_path="director.json",
)


# Initialize worker 1

worker1 = Agent(
    agent_name="Worker1",
    system_prompt="Generates a transcript for a youtube video on what swarms are",
    llm=Anthropic(),
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="<DONE>",
    state_save_file_type="json",
    saved_state_path="worker1.json",
)


# Initialize worker 2
worker2 = Agent(
    agent_name="Worker2",
    system_prompt="Summarizes the transcript generated by Worker1",
    llm=Anthropic(),
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="<DONE>",
    state_save_file_type="json",
    saved_state_path="worker2.json",
)


# Create a list of agents
agents = [director, worker1, worker2]

# Define the flow pattern
flow = "Director -> Worker1 -> Worker2"

# Using AgentRearrange class
agent_system = AgentRearrange(agents=agents, flow=flow)
output = agent_system.run(
    "Create a format to express and communicate swarms of llms in a structured manner for youtube"
)
print(output)


# Using rearrange function
output = rearrange(
    agents,
    flow,
    "Create a format to express and communicate swarms of llms in a structured manner for youtube",
)

print(output)
