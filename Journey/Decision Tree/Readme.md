# 🎵 Music Genre Prediction 🎵  
*Unlocking the rhythm of your favorite tunes using Machine Learning!*

---

## 🌟 Project Overview  

This project demonstrates how to predict a person's favorite music genre based on their **age** and **gender** using a **Decision Tree Classifier** from the `scikit-learn` library. It's an educational project showcasing the fundamentals of machine learning with Python.  

---

## 💂️ Dataset Details  

The dataset, `music.csv`, consists of the following columns:  

| **Column** | **Description**                  |  
|------------|----------------------------------|  
| `age`      | The age of the individual.       |  
| `gender`   | The gender (0 = male, 1 = female). |  
| `genre`    | The favorite music genre.        |  

---

## 🚀 Features  

- **Simple and Beginner-Friendly:** Understand machine learning concepts step by step.  
- **Decision Tree Classifier:** A powerful yet easy-to-use algorithm for classification tasks.  
- **Predict Music Preferences:** Input new data and predict genres in seconds.  

---

## 📦 Installation  

To get started, ensure you have Python installed and run the following commands to set up the environment:  

```bash
# Clone the repository
git clone https://github.com/your-username/music-genre-prediction.git  

# Navigate to the project folder
cd music-genre-prediction  

# Install required dependencies
pip install pandas scikit-learn matplotlib  
```

---

## 📖 How It Works  

1. **Load Data:** Read the dataset using Pandas.  
   ```python
   data = pd.read_csv("music.csv")
   ```  

2. **Prepare Features and Labels:** Separate the features (`age`, `gender`) and labels (`genre`).  
   ```python
   X = data.drop(columns=["genre"])
   y = data["genre"]
   ```  

3. **Train the Model:** Train a Decision Tree Classifier on the data.  
   ```python
   from sklearn.tree import DecisionTreeClassifier
   model = DecisionTreeClassifier()
   model.fit(X, y)
   ```  

4. **Make Predictions:** Use the trained model to predict genres for new inputs.  
   ```python
   input_data = pd.DataFrame([[21, 1], [33, 0]], columns=X.columns)
   prediction = model.predict(input_data)
   print(prediction)
   ```  

5. **Output Example:**  
   For input `[21, 1]` (21-year-old female) and `[33, 0]` (33-year-old male):
   ```bash
   ['HipHop', 'Classical']
   ```

---

## 🌐 Visualization (Optional)  

You can visualize the decision tree using `matplotlib`:
```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plot_tree(model, feature_names=X.columns, class_names=model.classes_, filled=True)
plt.show()
```

---

## 🔧 Future Improvements  

- Expand the dataset for more diverse genres and better predictions.
- Implement other classifiers to compare performance.
- Build a user-friendly interface for live predictions.

---

## 📚 Contributing  

Feel free to fork the repo and submit pull requests to improve the project. Contributions are always welcome!  

---

## 🔗 Connect  

If you have any questions or feedback, feel free to reach out or open an issue in the repository.

