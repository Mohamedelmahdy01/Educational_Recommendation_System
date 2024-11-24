# Career Recommendation System 🧑‍💼🎓

An **AI-powered Career Recommendation System** designed to analyze users' skills and interests to suggest the most suitable specialization. The system uses the **Random Forest Classifier** algorithm to process user answers and provide personalized recommendations.

---

## 📖 Table of Contents

- About the Project
- Features
- Dataset
- Technologies Used 
- Setup and Run  
- Future Improvements  
- How to Contribute
- License
---

## 🔍 About the Project

This project targets computer science students and anyone passionate about developing their technical skills and discovering the best career path. The system analyzes 20 user responses to skill-related questions and provides recommendations using a machine learning model.

---

## ✨ Features

- **Balanced Data Handling**: Ensures fair representation across different career fields.  
- **Robust Machine Learning Model**: Utilizes the Random Forest algorithm for accurate predictions.  
- **User-Friendly in Arabic**: Clear and straightforward questions to ensure accessibility.  

---

## 📊 Dataset

- **Source**: Represents real or simulated survey responses.  
- **Processing**: Data balancing is achieved using oversampling techniques.  
- **Splitting**: Data is divided into training and testing sets for model evaluation.  

---

## 🛠️ Technologies Used

- **Python**: The primary language for development.  
- **Flask**: For creating the API backend.  
- **Pandas & NumPy**: For data processing and analysis.  
- **scikit-learn**: For building and training the machine learning model.  

---

## 🚀 Setup and Run

### Prerequisites

- Python 3.8+  
- Required libraries listed in `requirements.txt`  

### Steps

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/YourUsername/Career-Recommendation-System.git
   cd Career-Recommendation-System
   ```

2. **Create a virtual environment (optional)**:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**:  
   ```bash
   python app.py
   ```

5. **Access the API**:  
   The application is now accessible at `http://127.0.0.1:5000`.

---

## 🔮 Future Improvements

- Add more questions to enhance recommendation accuracy.  
- Integrate additional machine learning models for comparison.  
- Develop a user-friendly frontend interface.  
- Support multiple languages to reach a broader audience.  

---

## 🤝 How to Contribute

We welcome contributions to improve the project!  
1. **Fork the repository**:  
   ```bash
   git clone https://github.com/YourUsername/Career-Recommendation-System.git
   ```
2. **Create a new branch**:  
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes**:  
   ```bash
   git commit -m "Add some feature"
   ```
4. **Push the branch**:  
   ```bash
   git push origin feature-name
   ```
5. **Open a Pull Request**.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

