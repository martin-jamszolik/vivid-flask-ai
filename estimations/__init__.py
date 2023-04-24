from flask import Blueprint
from flask_restful import Api
from .views import *


def init_estimations(app):
    estimations_bp = Blueprint('estimations', __name__, url_prefix='/api/estimations')
    api = Api(estimations_bp)
    api.add_resource(ProposalList, '/proposals')
    api.add_resource(ProposalDetail, '/proposals/<int:id>')
    app.register_blueprint(estimations_bp)
    

