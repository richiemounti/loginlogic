from flask import request, make_response, jsonify, abort


class Dashboard(object):
        
    @staticmethod
    def get_data():
        data = request.get_json()
        if data is not request.get_json:
            data = request.get_json(force=True)
        return data