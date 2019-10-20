from flask import Blueprint, render_template

landing_bp = Blueprint('landing_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/landing')

@landing_bp.route("/")
def index():
    return render_template('index.html')

@landing_bp.route('/about')
def about():
    return render_template('about.html')

@landing_bp.route('/contact')
def contact():
    return render_template('contact')

