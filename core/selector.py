from models.gpt import GPTModel
from models.claude import ClaudeModel

class ModelSelector:
    def __init__(self):
        self.models = {
            "gpt": GPTModel(),
            "claude": ClaudeModel()
        }

    def select(self, task_type):
        if task_type in ["analysis", "coding"]:
            return self.models["gpt"]
        return self.models["claude"]
