import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data (user-item interaction matrix)
data = {
    'User1': [5, 4, 0, 0, 0],
    'User2': [0, 0, 3, 4, 0],
    'User3': [1, 0, 0, 0, 2],
    'User4': [0, 2, 4, 5, 0],
    'User5': [0, 0, 0, 0, 3]
}

# Convert to DataFrame
df = pd.DataFrame(data, index=['Item1', 'Item2', 'Item3', 'Item4', 'Item5'])

# Calculate cosine similarity between users
user_similarity = cosine_similarity(df)

# Target user index (for example, User1)
target_user_index = 0  # corresponds to 'User1'

# Find similar users (excluding self)
similar_users = sorted(list(enumerate(user_similarity[target_user_index])), key=lambda x: x[1], reverse=True)
similar_users = [user_index for user_index, similarity in similar_users if user_index != target_user_index]

# Recommendation for target user based on similar users
recommended_items = []
for user in similar_users:
    for item in df.index:
        if df.loc[item, f'User{user + 1}'] > 0 and df.loc[item, f'User{target_user_index + 1}'] == 0:
            recommended_items.append(item)

# Print recommended items
print("Recommended items:")
for item in recommended_items:
    print(item)
