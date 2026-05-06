from core.registry import AgentRegistry
from core.router import TaskRouter
from core.selector import ModelSelector
from agents.analysis_agent import analysis_handler
from agents.coding_agent import coding_handler
from core.agent import Agent

class MultiAgentSystem:
    def __init__(self):
        self.registry = AgentRegistry()
        self.selector = ModelSelector()
        self.router = TaskRouter(self.registry, self.selector)

    def setup(self):
        self.registry.register(Agent("analysis_agent", "analysis", analysis_handler))
        self.registry.register(Agent("coding_agent", "coding", coding_handler))

    async def run_tasks(self, tasks):
        results = []
        for task in tasks:
            result = await self.router.route(task)
            results.append(result)
        return results
