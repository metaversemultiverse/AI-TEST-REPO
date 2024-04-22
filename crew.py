class Crew:

    def __init__(self, agents):
        self.agents = agents

    def kickoff(self, inputs):
        """ Sequentially executes tasks assigned to each agent based on the provided inputs. """
        results = {}
        for agent in self.agents:
            for input_detail in inputs:  # Assuming inputs might be a list of tasks or a single task.
                result = agent.perform_task(input_detail)
                results[agent.role] = result
                if agent.verbose:
                    print(f"Result for agent {agent.role}: {result}")

        return results

    def get_crew_memory(self):
        """ Compiles and returns memories from all agents in the crew. """
        crew_memory = {}
        for agent in self.agents:
            crew_memory[agent.role] = agent.recall_memory()
        return crew_memory

    def reset_crew_memory(self):
        """ Resets the memories of all agents in the crew. """
