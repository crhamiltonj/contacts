from flask import Blueprint, render_template


contact_bp = Blueprint('contact_bp', __name__, template_folder='templates', static_folder='static', static_url_path='/contact')


@contact_bp.route('/')
def contact_dashboard():
    return render_template('index.html')