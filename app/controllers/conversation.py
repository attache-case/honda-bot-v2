from app.models.honda import honda


async def process_message(message):
    await honda.process_message(message)
