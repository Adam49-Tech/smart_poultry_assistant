from utils.feed_calculator import get_feed_recommendation, load_feed_data
age = 20
feed = get_feed_recommendation(age)
print(f"Feed for age {age} days: {feed}")
df = load_feed_data("my data/feed_nutrients.csv")
print(df[df["Feed Type"] == feed])
