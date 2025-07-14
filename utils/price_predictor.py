def estimate_price(bird_type, age_weeks):
    try:
        bird_type = str(bird_type).strip().lower()
        age = int(age_weeks)
        base_prices = {
            "broiler": 300,
            "cockerel": 200,
            "layer": 250
        }
        growth_multipliers = {
            "broiler": 1.15,
            "cockerel": 1.10,
            "layer": 1.12
        }
        if bird_type not in base_prices:
            return "Unknown bird type"
        base_price = base_prices[bird_type]
        multiplier = growth_multipliers[bird_type]
        price = base_price * (multiplier ** age)
        return round(price)
    except ValueError:
        return "Please enter a valid age in weeks"