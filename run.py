from app import app
from app.agent import LearningAgent
import threading

def run_agent():
    agent = LearningAgent()
    print("uAgent is running...")
    agent.run()

if __name__ == "__main__":
    # Run the uAgent in a separate thread
    agent_thread = threading.Thread(target=run_agent)
    agent_thread.start()

    # Run the Flask app
    print("Flask app is running...")
    app.run(host="0.0.0.0", port=5000)