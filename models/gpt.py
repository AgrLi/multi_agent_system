import asyncio

class GPTModel:
    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.1)
        return f"[GPT] {prompt}"
