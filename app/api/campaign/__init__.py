from flask import Blueprint

campaignAPI = Blueprint('campaign', __name__)

from . import views