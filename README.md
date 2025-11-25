ML Password Security API 🔐 (Machine Learning Powered Password Strength Prediction)

A lightweight, production-ready API that uses Machine Learning + Rule-Based Features to analyze password strength.
Built with FastAPI, scikit-learn, and deployed on Render.

This project predicts whether a password is Weak, Medium, or Strong using a trained RandomForest model based on entropy, length, and rule-based scoring.

-------------------------------------------------------------------------------------

🚀 Live API

BASE URL:
https://ml-password-security-api.onrender.com

Interactive Docs (Swagger):
https://ml-password-security-api.onrender.com/docs

-------------------------------------------------------------------------------------

📌 Features
✔ Machine Learning Model

Trained RandomForest classifier

Feature engineering based on entropy, length, and character rules

✔ FastAPI Backend

Fast, async Python backend

Clean and modular folder structure

✔ Ready for Production

Deployed on Render

CORS ready

Auto-generated API docs

-------------------------------------------------------------------------------------

📂 Project Structure
Ml-Password-Security-Api/
│
├── api/
│   └── main.py               # FastAPI app
│
├── ml/
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── model.pkl             # Trained model
│
├── requirements.txt
├── README.md
└── .gitignore

-------------------------------------------------------------------------------------

🧠 How the ML Model Works

The model uses:

1. Length

Longer passwords are usually stronger.

2. Entropy

Higher randomness → stronger password.

3. Rule-Based Score

Checks for:

Uppercase

Lowercase

Numbers

Special characters

The ML model learns patterns from data to classify strength.

-------------------------------------------------------------------------------------

▶ API Endpoints
1. Predict Password Strength

POST /predict

Request Body:
{
  "password": "YourPassword123@"
}

Response:
{
  "strength": "Strong",
  "score": 0.92
}

-------------------------------------------------------------------------------------

🛠 Local Setup
Clone the repository
git clone https://github.com/your-username/Ml-Password-Security-Api.git
cd Ml-Password-Security-Api

Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run server
uvicorn api.main:app --reload

🎯 Training the Model (Optional)

If you modify the dataset:

python -m ml.train_model


This regenerates:

ml/model.pkl

☁ Deploying to Render
1. Push your code to GitHub
2. Create new Web Service
3. Choose:

Runtime → Python

4. Set build command:
pip install -r requirements.txt

5. Set start command:
uvicorn api.main:app --host 0.0.0.0 --port $PORT


Done. Render auto-deploys on every commit.

🧩 Tech Stack

Python

FastAPI

scikit-learn

Pandas

Render

Uvicorn

🤝 Contributing

Pull requests are welcome.
For major changes, open an issue first to discuss.

📜 License
Free for personal and commercial use.
