from flask import render_template, session, redirect, url_for, request, jsonify
from . import api

@api.route('/', methods=['GET'])
def test_api():
	return jsonify({'test': 'success'})
