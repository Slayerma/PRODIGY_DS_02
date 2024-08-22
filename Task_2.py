import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TitanicEDA:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
    
    def explore_data(self):
        self.visualize_survival_rate(self.data)
        self._explore_relationships(self.data)
    
    def visualize_survival_rate(self, data: pd.DataFrame) -> None:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='PassengerId', y='Survived', data=data)
        plt.title('Survival Rate')
        plt.show()
    
    def _explore_relationships(self, data: pd.DataFrame) -> None:
        corr_matrix = data.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        plt.show()

        sns.pairplot(data, hue='Survived', palette='husl')
        plt.title('Pairplot')
        plt.show()
        
        sns.countplot(x='PassengerId', hue='Survived', data=data)
        plt.title('Number of Survived vs PassengerId')
        plt.xlabel('PassengerId')
        plt.ylabel('Number of Survived')
        plt.show()

# Usage
titanic_eda = TitanicEDA('gender_submission.csv')
titanic_eda.explore_data()

