from flask import Blueprint, request, jsonify, render_template


projects_bp = Blueprint('projects', __name__)


@projects_bp.route("/", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")


