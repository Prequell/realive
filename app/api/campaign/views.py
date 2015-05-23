from flask import render_template, session, redirect, url_for, request, jsonify
from . import campaignAPI

@campaignAPI.route('/all', methods=['GET'])
def get_all_campaign():
	return jsonify({'campaign' : 'all' })