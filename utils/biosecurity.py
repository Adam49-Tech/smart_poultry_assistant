# utils/biosecurity_advice.py
def get_biosecurity_tips(selected_challenges):
    tips = []
    if "dirty water" in selected_challenges:
        tips.append("💧 Provide clean, treated water daily.")
    if "bad ventilation" in selected_challenges:
        tips.append("💨 Improve airflow with cross-ventilation or fans.")
    if "rodents" in selected_challenges:
        tips.append("🐭 Seal holes, set traps, and store feed properly.")
    if "wet litter" in selected_challenges:
        tips.append("🧹 Replace wet bedding and fix roof leaks.")
    if "overcrowding" in selected_challenges:
        tips.append("📏 Space birds properly to reduce stress and disease.")
    if "mixing old and new birds" in selected_challenges:
        tips.append("🚫 Quarantine new birds before mixing.")
    if not tips:
        tips.append("⚠️ Select at least one farm challenge to get tips.")
    return tips
