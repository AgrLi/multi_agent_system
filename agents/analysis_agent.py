async def analysis_handler(input_data, model):
    prompt = f"Analyze: {input_data['text']}"
    return await model.generate(prompt)
