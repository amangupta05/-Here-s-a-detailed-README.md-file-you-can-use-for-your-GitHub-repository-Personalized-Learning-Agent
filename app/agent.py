from fetchai.uagents import Agent
from config.config import config

class LearningAgent(Agent):
    def __init__(self):
        super().__init__(private_key=config.UAGENT_PRIVATE_KEY)

    async def handle_message(self, sender, message):
        # Process incoming messages
        user_input = message.get("content")
        # Implement a workflow
        response = await self.process_user_input(user_input)
        await self.send_message(sender, {"content": response})

    async def process_user_input(self, user_input):
        # Call GPT-4 API
        prompt = f"Provide personalized learning guidance for: {user_input}"
        return query_gpt4(prompt)