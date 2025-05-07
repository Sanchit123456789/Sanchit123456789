import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot with 'Species' as hue (color category)
sns.scatterplot(data=df, x='PetalLengthCm', y='SepalLengthCm', hue='Species')

# Add title and show plot
plt.title('Petal Length vs Sepal Length by Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()

