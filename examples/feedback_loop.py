import un1ty

# Collect user feedback and improve future outputs
def collect_feedback(output, user_rating):
    un1ty.feedback.learn(
        output=output,
        rating=user_rating
    )
    return "Feedback recorded. Thank you!"

# Example usage
feedback = collect_feedback("Sample output from Hybr1d.", user_rating=4.5)
print(feedback)