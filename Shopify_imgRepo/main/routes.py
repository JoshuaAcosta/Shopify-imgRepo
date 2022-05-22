from flask import render_template
from flask_login import login_required, current_user
from . import main_bp


@main_bp.route('/', methods=['GET'])
def mainpage():
    """Renders main page asking to registe or log in """
    return render_template('mainpage.html')

@main_bp.route('/galeria', methods=['GET'])
@login_required
def galeria():
    """Renders page to view your gallery of images """
    return render_template('galeria.html', name=current_user.first_name)