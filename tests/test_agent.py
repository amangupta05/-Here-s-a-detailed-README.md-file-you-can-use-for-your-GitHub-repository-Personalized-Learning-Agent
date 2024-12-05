import unittest
from app.agent import LearningAgent

class TestAgent(unittest.TestCase):
    def test_agent_initialization(self):
        agent = LearningAgent()
        self.assertIsNotNone(agent, "Agent should be initialized correctly.")

    def test_process_user_input(self):
        agent = LearningAgent()
        response = agent.process_user_input("Test input")
        self.assertTrue(response, "Agent should return a valid response.")