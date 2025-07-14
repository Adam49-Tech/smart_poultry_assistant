def calculate_feed(bird_type, age_days, num_birds, feed_type):
    try:
        age_days = int(age_days)
        num_birds = int(num_birds)
    except (ValueError, TypeError):
        return "Invalid input. Age and number of birds must be numbers."
    if age_days <= 0 or num_birds <= 0:
        return "Please enter positive values."
    # Feed consumption estimates (grams/day) by feed type
    feed_chart = {
        'super starter': lambda age: 15 + (age * 1.5),
        'starter': lambda age: 35 + (age * 2.5),
        'finisher': lambda age: 70 + (age * 3.5),
    }
    # Decide feed type based on selection or age
    feed_type = feed_type.lower()
    if feed_type not in feed_chart:
        if age_days <= 14:
            feed_type = 'super starter'
        elif age_days <= 28:
            feed_type = 'starter'
        else:
            feed_type = 'finisher'
    daily_feed_per_bird = feed_chart[feed_type](age_days)
    total_feed_kg = (daily_feed_per_bird * num_birds) / 1000
    return f"{round(total_feed_kg, 2)} kg of {feed_type} feed per day"