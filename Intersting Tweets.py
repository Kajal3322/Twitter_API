import pandas as pd

# Read the CSV file into a DataFrame
data_frame = pd.read_csv("elonmusk_tweets.csv")


print("The Top 10 Favrite Tweets")

# Sort the DataFrame by Favorite Count in descending order and select the top 10 tweets
top_10_favorites = data_frame.sort_values(by="Favorite Count", ascending=False).head(10)

# Print the relevant information for each tweet in the top 10
for index, tweet in top_10_favorites.iterrows():
    print(f"Creation Date: {tweet['Creation Date']}\nText: {tweet['Text']}\nFavorite Count: {tweet['Favorite Count']}\nRetweet Count: {tweet['Retweet Count']}\n")


print("The Top 10 Least Favrite Tweets")

# Sort the DataFrame by Favorite Count in ascending order and select the top 10 tweets
top_10_least_favorites = data_frame.sort_values(by="Favorite Count").head(10)

# Print the relevant information for each tweet in the top 10
for index, tweet in top_10_least_favorites.iterrows():
    print(f"Creation Date: {tweet['Creation Date']}\nText: {tweet['Text']}\nFavorite Count: {tweet['Favorite Count']}\nRetweet Count: {tweet['Retweet Count']}\n")

print("The Top 10 Most Retweeted Tweets")

# Sort the DataFrame by Retweet Count in descending order and select the top 10 tweets
top_10_most_retweeted = data_frame.sort_values(by="Retweet Count", ascending=False).head(10)

# Print the relevant information for each tweet in the top 10
for index, tweet in top_10_most_retweeted.iterrows():
    print(f"Creation Date: {tweet['Creation Date']}\nText: {tweet['Text']}\nFavorite Count: {tweet['Favorite Count']}\nRetweet Count: {tweet['Retweet Count']}\n")
