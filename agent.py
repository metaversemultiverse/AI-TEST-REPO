class Agent:

    def __init__(self, role, goal, tools, verbose=False, memory=None):
        self.role = role
        self.goal = goal
        self.tools = tools
        self.verbose = verbose
        self.memory = memory if memory is not None else []

    def perform_task(self, input_data):
        """ Process the input data using the assigned tool and store the interaction in memory. """
        if self.verbose:
            print(
                f"Agent {self.role} performing task with input: {input_data}")

        tool_response = self.tools[0].run(input_data, self.memory)
        self.memory.append(
            (input_data,
             tool_response))  # Storing both input and output for context

        if self.verbose:
            print(f"Task completed with output: {tool_response}")

        return tool_response

    def recall_memory(self):
        """ Return the memory of this agent which includes past interactions. """
        return self.memory

    def reset_memory(self):
        """ Reset the memory of this agent. """

        self.memory = []
        return self.memory

    def save_memory(self, filename):
        """ Save the memory of this agent to a file. """
        with open(filename, 'w') as file:
            for input_data, output in self.memory:
                file.write(f"Input: {input_data}\n")
                file.write(f"Output: {output}\n")

    def load_memory(self, filename):
        """ Load the memory of this agent from a file. """
        self.memory = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("Input:"):
                    input_data = line.split("Input: ")[1]
                elif line.startswith("Output:") and input_data:
                    output = line.split("Output: ")[1]
                    self.memory.append((input_data, output))
                    input_data = None  # Reset input_data for the next interaction


class Task:

    def __init__(self, name, description, tools):
        self.name = name
        self.description = description
        self.tools = tools

    def run(self, input_data):
        """ Process the input data using the assigned tool and return the output. """
        if self.tools:
            tool_response = self.tools[0].run(input_data)
            return tool_response
        else:
            return "No tools available for this task."


class Crew:

    def __init__(self, name, description, agents, verbose=False):
        self.name = name
        self.description = description
        self.agents = agents
        self.verbose = verbose

    def perform_task(self, input_data):
        """ Process the input data using the assigned agent and return the output. """
        if self.verbose:
            print(f"Crew {self.name} performing task with input: {input_data}")
        agent_response = self.agents[0].perform_task(input_data)
        if self.verbose:
            print(f"Task completed with output: {agent_response}")
        return agent_response

    def recall_memory(self):
        """ Return the memory of this crew which includes past interactions. """
        memory = []
        for agent in self.agents:
            memory.extend(agent.recall_memory())
        return memory

    def reset_memory(self):
        """ Reset the memory of this crew. """
        for agent in self.agents:
            agent.reset_memory()
        return self.recall_memory()

    def save_memory(self, filename):
        """ Save the memory of this crew to a file. """

        for agent in self.agents:
            agent.save_memory(filename)

    def load_memory(self, filename):
        """ Load the memory of this crew from a file. """
        for agent in self.agents:
            agent.load_memory(filename)
