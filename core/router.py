class TaskRouter:
    def __init__(self, registry, selector):
        self.registry = registry
        self.selector = selector

    async def route(self, task):
        agent = self.registry.get(task["agent"])
        model = self.selector.select(agent.task_type)
        return await agent.run(task["input"], model)
