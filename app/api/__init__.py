from flask import Blueprint
from campaign import campaignAPI

api = Blueprint('api', __name__)

from . import views