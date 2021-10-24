from flask import Flask
from views.routes import pd_bp

app = Flask(__name__, template_folder='templates/')
app.register_blueprint(pd_bp)
app.run(debug=True)
