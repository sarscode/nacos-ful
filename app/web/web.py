
from flask import (
    Blueprint,  render_template
)

blueprint = Blueprint('web', __name__, url_prefix='/',
                      template_folder='templates', static_folder='static')


@blueprint.route('/')
def home():
    """ Home page """
    return render_template('home.html')
