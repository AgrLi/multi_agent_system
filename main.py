import asyncio
from core.system import MultiAgentSystem

async def main():
    system = MultiAgentSystem()
    system.setup()

    tasks = [
        {"agent": "analysis_agent", "input": {"text": "AI market trends"}},
        {"agent": "coding_agent", "input": {"requirement": "build a FastAPI service"}}
    ]

    results = await system.run_tasks(tasks)

    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
