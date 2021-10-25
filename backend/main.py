from flask import Flask
from flask_cors import CORS
from views.routes import pd_bp

app = Flask(__name__, template_folder='templates/')
CORS(app)
app.register_blueprint(pd_bp)
app.run(debug=True)
