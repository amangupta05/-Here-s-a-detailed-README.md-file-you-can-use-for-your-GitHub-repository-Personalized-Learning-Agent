from app.database import Session, User, LearningHistory
from app.gpt4_integration import query_gpt4

def personalize_and_store(user_id, user_input):
    session = Session()
    
    # Fetch user preferences or set defaults
    user = session.query(User).filter_by(user_id=user_id).first()
    preferences = user.preferences if user else {"default": "preferences"}
    
    # Generate personalized content
    prompt = f"User prefers {preferences}. Content: {user_input}"
    response = query_gpt4(prompt)
    
    # Log response in learning history
    if user:
        learning_record = LearningHistory(user_id=user_id, content=response)
        session.add(learning_record)
        session.commit()

    return response