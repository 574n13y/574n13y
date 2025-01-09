import matplotlib.pyplot as plt

# Total contributions per year
years = ['2023', '2024', '2025']
contributions = [617, 904, 46]

plt.figure(figsize=(10, 6))
plt.bar(years, contributions, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Total Contributions')
plt.title('Total Contributions per Year')
plt.savefig('total_contributions.png')

# Storage used in GitHub
storage = 11111101001  # in bytes

plt.figure(figsize=(10, 6))
plt.bar(['Storage Used'], [storage], color='green')
plt.xlabel('Category')
plt.ylabel('Storage (Bytes)')
plt.title('Storage Used in GitHub')
plt.savefig('storage_used.png')

# Number of public and private repositories
repos = ['Public', 'Private']
counts = [45, 7]

plt.figure(figsize=(10, 6))
plt.bar(repos, counts, color='purple')
plt.xlabel('Repository Type')
plt.ylabel('Count')
plt.title('Number of Public and Private Repositories')
plt.savefig('repo_count.png')

# Most productive day of the week
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
productive_days = [1, 1, 1, 1, 1, 1, 1]  # Assuming equal productivity for simplicity

plt.figure(figsize=(10, 6))
plt.bar(days, productive_days, color='orange')
plt.xlabel('Day of the Week')
plt.ylabel('Productivity')
plt.title('Most Productive Day of the Week')
plt.savefig('productive_days.png')

# Number of commits per day
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
commits = [2, 5, 7, 10, 3]

plt.figure(figsize=(10, 6))
plt.plot(days, commits, marker='o', color='red')
plt.xlabel('Days')
plt.ylabel('Number of Commits')
plt.title('Number of Commits per Day')
plt.savefig('commits_per_day.png')