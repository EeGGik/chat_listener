from flask.views import MethodView
from flask import jsonify, request
from http import HTTPStatus
from business.checker import checker


class HeathCheck(MethodView):
    def get(self):
        """This is a health check
        """
        return jsonify({"status": "ok"}), HTTPStatus.OK


class MessageChecker(MethodView):
    def post(self):
        return checker(request)
