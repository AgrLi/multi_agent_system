import asyncio

class ClaudeModel:
    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.1)
        return f"[Claude] {prompt}"
