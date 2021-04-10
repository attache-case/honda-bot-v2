from app.models.honda import honda


async def initial_message(ch):
    await honda.initial_famous_saying(ch)

async def process_message(message):
    await honda.process_message(message)
