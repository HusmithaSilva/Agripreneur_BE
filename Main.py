from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "testing12#"


# from Agripreneur_App.Routes.Agri_App import create_user
# from extensions import mongo, db
import Agripreneur_App.Routes.User
import Agripreneur_App.Auth.Token
import Agripreneur_App.Routes.Leaderboard
import Agripreneur_App.Routes.Gamification




if __name__ == "__main__":
    app.run(port=5000, debug=True)
