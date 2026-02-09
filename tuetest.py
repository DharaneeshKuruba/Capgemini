# from flask import Flask, request, jsonify, redirect, url_for, render_template, flash, session
# from werkzeug.utils import secure_filename
# import os
# app = Flask(__name__)
# app.secret_key="secret"
# users={}
# accounts={}
# @app.route("/",methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         username=request.form["username"]
#         password=request.form["password"]
#         if username in users and users[username]["password"]==password:
#             session["user"]=username
#             return redirect(url_for("dashboard"))
#         return "Invalid login"
#     return render_template("login.html")
# @app.route("/dashboard")
# def dashboard():
#     if "user" in session:
#         return f"Welcome {session['user']}"
#     return redirect(url_for("login"))
# @app.route("/users",methods=["POST"])
# def create_user():
#     data=request.json
#     username=data["username"]
#     if username in users:
#         return jsonify({"error":"User already exists"}),400
#     users[username]={"password":data["password"]}
#     return jsonify({"message":"User created"})
# @app.route("/users/<username>",methods=["GET"])
# def get_user(username):
#     if username not in users:
#         return jsonify({"error":"User not found"}),404
#     return jsonify(users[username])
# @app.route("/users/<username>",methods=["PUT"])
# def update_user(username):
#     if username not in users:
#         return jsonify({"error":"User not found"}),404
#     users[username]["password"]=request.json["password"]
#     return jsonify({"message":"User updated"})
# @app.route("/users/<username>",methods=["DELETE"])
# def delete_user(username):
#     if username not in users:
#         return jsonify({"error":"User not found"}),404
#     users.pop(username)
#     return jsonify({"message":"User deleted"})
# @app.route("/account",methods=["POST"])
# def create_account():
#     data=request.json
#     username=data["username"]
#     if username not in users:
#         return jsonify({"error":"User not found"}),404
#     accounts[username]={
#         "accno":data["accno"],
#         "name":data["name"],
#         "balance":data["balance"],
#         "updatedamount":data["updatedamount"],
#         "phone":data["phone"],
#         "aadhaar":data["aadhaar"],
#         "account_type":data["account_type"]
#     }
#     return jsonify({"message":"Account created"})
# @app.route("/account/<username>",methods=["GET"])
# def get_account(username):
#     if username not in accounts:
#         return jsonify({"error":"Account not found"}),404
#     return jsonify(accounts[username])
# @app.route("/account/<username>",methods=["PUT"])
# def update_account(username):
#     if username not in accounts:
#         return jsonify({"error":"Account not found"}),404
#     accounts[username]["balance"]=request.json["balance"]
#     accounts[username]["updatedamount"]=request.json["updatedamount"]
#     return jsonify({"message":"Account updated"})
# @app.route("/account/<username>",methods=["DELETE"])
# def delete_account(username):
#     if username not in accounts:
#         return jsonify({"error":"Account not found"}),404
#     accounts.pop(username)
#     return jsonify({"message":"Account deleted"})
# @app.route("/loan/<username>",methods=["GET"])
# def loan_eligibility(username):
#     if username not in accounts:
#         return jsonify({"error":"Account not found"}),404
#     if accounts[username]["balance"]>30000:
#         return jsonify({"username":username,"eligible":True,"loan_amount":50000})
#     return jsonify({"username":username,"eligible":False,"loan_amount":0})
# if __name__=="__main__":
#     app.run(debug=True)