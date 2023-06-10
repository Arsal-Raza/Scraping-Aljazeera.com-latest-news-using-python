import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data into a DataFrame
df = pd.read_csv('today_News.csv')

# Step 2: Count the occurrences of each category and topic
category_counts = df['Tag 1'].value_counts()
topic_counts = df['Tag 2'].value_counts()

# Step 3: Visualize the category and topic distributions
plt.figure(figsize=(9, 5))
category_counts.plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.title('Category Distribution')
plt.show()

plt.figure(figsize=(8, 4))
topic_counts.plot(kind='bar')
plt.xlabel('Topics')
plt.ylabel('Frequency')
plt.title('Topic Distribution')
plt.show()

# Step 4: Analyze relationships between categories and topics
category_topic_counts = pd.crosstab(df['Tag 1'], df['Tag 2'])
print(category_topic_counts)
