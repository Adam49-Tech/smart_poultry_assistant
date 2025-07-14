# utils/biosecurity_advice.py
def get_biosecurity_tip(challenge):
    tips = {
        "Frequent disease outbreak": "Disinfect the pen regularly, isolate sick birds, and improve ventilation.",
        "Wet litter": "Reduce water spillage, use absorbent bedding, and replace wet areas promptly.",
        "High mortality": "Check feed quality, ensure proper brooding, and vaccinate as scheduled.",
        "Slow growth": "Provide balanced feed, deworm regularly, and reduce overcrowding.",
        "Smelly environment": "Clean droppings frequently, improve airflow, and remove leftover feed.",
        "Fly infestation": "Use fly traps, maintain cleanliness, and apply natural repellents.",
        "Mixed age birds": "Separate birds by age group to reduce disease transmission and competition."
    }
    return tips.get(challenge, "No specific advice available.")
