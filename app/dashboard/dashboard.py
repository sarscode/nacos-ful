""" Dashboard """
from flask import (
    Blueprint, render_template
)


blueprint = Blueprint('dashboard', __name__, url_prefix='/dashboard',
                      template_folder='templates', static_folder='static')


@blueprint.route('/', methods=['GET'])
def dashboard():
    """ Dashboard """
    return render_template('dashboard.html')
