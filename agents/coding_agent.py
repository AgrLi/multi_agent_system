async def coding_handler(input_data, model):
    prompt = f"Code: {input_data['requirement']}"
    return await model.generate(prompt)
