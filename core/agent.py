class Agent:
    def __init__(self, name, task_type, handler):
        self.name = name
        self.task_type = task_type
        self.handler = handler

    async def run(self, input_data, model):
        return await self.handler(input_data, model)
