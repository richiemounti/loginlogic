import uuid
import app
from app import db


from flask import (
    Blueprint, request,  render_template, make_response, abort, g, session
)

bp = Blueprint('dashboard', __name__)

from app.dashboard import Dashboard


@bp.route('/')
@bp.route('/index')
def index():

    return render_template('dashboard/index.html',
                            title='Main',
                            )