class Task:

    def __init__(self, description, agent):
        self.description = description
        self.agent = agent

    def execute(self, input_data):
        """ Execute the task by delegating the input data to the agent's perform_task method. """
        print(f"Executing task: {self.description}")
        return self.agent.perform_task(input_data)


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
