# 200 OK
# 201 Created
# 400 Bad Request
# 401 Unautorized
# 404 Not Found
# 500 Server Error

from flask import Flask, request, jsonify, redirect, url_for, render_template, flash, session
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
# users = [
#     {"id": 1, "name": "Alice", "role": "student"},
#     {"id": 2, "name": "Bob", "role": "teacher"}
# ]
# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify(users)
# @app.route('/users', methods=['POST'])
# def create_user():
#     new_user = request.json
#     new_user["id"] = len(users) + 1
#     users.append(new_user)
#     return jsonify(new_user), 201
# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.json
#     for user in users:
#         if user["id"] == user_id:
#             user.update(data)
#             return jsonify(user), 200
#     return jsonify({"error": "User not found"}), 404
# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     for user in users:
#         if user["id"] == user_id:
#             users.remove(user)
#             return jsonify({"message": "User deleted"}), 200
#     return jsonify({"error": "User not found"}), 404
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask,request,jsonify
# import base64
# app=Flask(__name__)
# products=[]
# @app.route("/register/product",methods=['POST'])
# def register_product():
#     data=request.get_json()
#     required_fields=[
#         "Cat_id","Sub_id","Product_name","Price","GST","offer","image"
#     ]
#     for field in required_fields:
#         if field not in data:
#             return jsonify({
#                 "error": f"{field} is required"
#             }), 400
#     try:
#         image_bytes = base64.b64decode(data["image"])
#         data["image"] = image_bytes
#     except Exception:
#         return jsonify({
#             "error": "Invalid image format"
#         }), 400
#     products.append(data)
#     return jsonify({
#         "message": "Product registered successfully",
#         "product": data
#     }), 201
# @app.route("/products",methods=['GET'])
# def get_products():
#     return jsonify(products), 200

# if __name__ == "__main__":
#     app.run(port=3000, debug=True)


# from flask import Flask,request,jsonify
# app=Flask(__name__)
# accounts=[]
# @app.route("/accounts/<int:acc_no>",methods=["GET"])
# def get_account(acc_no):
#     try:
#         for acc in accounts:
#             if acc["account_no"]==acc_no:
#                 return jsonify(acc),200
#         return jsonify({"error":"account not found"}),404
#     except Exception as e:
#         return jsonify({"error":str(e)}),500
#     finally:
#         print("GET Account called")
# @app.route("/accounts",methods=["POST"])
# def create_account():
#     try:
#         data=request.get_json()
#         accounts.append(data)
#         return jsonify({"message":"Account Created","account":data}),201
#     except Exception as e:
#         return jsonify({"error":str(e)}),400
#     finally:
#         print("POST account called")
# @app.route("/accounts/<int:acc_no>",methods=["PUT"])
# def update_account(acc_no):
#     try:
#         data=request.get_json()
#         for acc in accounts:
#             if acc["account_no"]==acc_no:
#                 acc.update(data)
#                 return jsonify(acc),200
#         return jsonify({"error":"account not found"}),404
#     except Exception as e:
#         return jsonify({"error":str(e)}),400
#     finally:
#         print("PUT account called")
# @app.route("/accounts/<int:acc_no>",methods=["DELETE"])
# def close_account(acc_no):
#     try:
#         for acc in accounts:
#             if acc["account_no"]==acc_no:
#                 accounts.remove(acc)
#                 return jsonify({"message":f"account {acc_no} closed"}),200
#         return jsonify({"error":"account not found"}),404
#     except Exception as e:
#         return jsonify({"error":str(e)}),400
# if __name__=="__main__":
#     app.run(port=3000,debug=True)


# app=Flask(__name__)
# @app.route('/')
# def Hello():
#     return 'Hello'
# if __name__=="__main__":
#     app.run(debug=True)


# app=Flask(__name__)
# def hello():
#     return 'hello world'
# app.add_url_rule('/','hello',hello)
# if __name__=="__main__":
#     app.run(debug=True)


# app = Flask(__name__)
# @app.route('/hello/<name>')
# def hello(name):
#     return 'Hello %s!' % name
# if __name__ == "__main__":
#     app.run(debug=True)


# app = Flask(__name__)
# @app.route('/blog/<int:postID>')
# def show(postID):
#     return 'Blog Number %d' % postID
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number %f' % revNo
# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route('/')
# def hello_admin():
#     return "Hello Admin"
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return "Hello %s!" % guest
# @app.route('/user/<name>')
# def hello(name):
#     if name=='admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest',guest=name))
# if __name__=="__main__":
#     app.run(debug=True)


# @app.route('/upload')
# def upload():
#     return render_template('upload.html')
# @app.route('/uploader',methods=['GET','POST'])
# def upload_file():
#     if request.method=='POST':
#         f=request.files['file']
#         f.save(secure_filename(f.filename))
#         return "file uploaded successfully"
# if __name__=="__main__":
#     app.run(debug=True)


# @app.route('/')
# def student():
#     return render_template('student.html')
# @app.route('/result',methods=['GET','POST'])
# def result():
#     if request.method=='POST':
#         result=request.form
#         return render_template("result.html",result=result)
# if __name__=="__main__":
#     app.run(debug=True)


# app.secret_key="secret"
# @app.route('/index')
# def index():
#     return render_template('index.html')
# @app.route('/login',methods=['GET','POST'])
# def login():
#     error=None
#     if request.method=='POST':
#         if request.form['username']!='admin' or \
#             request.form['password']!='admin':
#                 error='Invlid username or password. Please try again !'
#         else:
#             flash("you were logged in successfully")
#             return redirect(url_for('index'))
#     return render_template('login.html',error=error)
# if __name__=="__main__":
#     app.run(debug=True)


# students_data={
#     1: {"name": "anu","dept": "CSE", "year": 3},
#     2: {"name": "karthi","dept": "ECE", "year": 2},
#     3: {"name": "priya","dept": "IT", "year": 4}
# }
# @app.route('/students',methods=['GET'])
# def get_all_students():
#     try:
#         return jsonify(students_data)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         print("GET All students called")
# @app.route('/students/<int:student_id>',methods=['GET'])
# def get_student_by_ID(student_id):
#     try:
#         if student_id not in students_data:
#             return jsonify({"error": "Student data not found"}), 404
#         return jsonify({
#             "student_id": student_id,
#             "details": students_data[student_id]
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         print("GET student by ID called")
# if __name__=="__main__":
#     app.run(port=3000,debug=True)
    
    
# staff_data = {
#     101: {"name": "ramesh", "subject": "maths"},
#     102: {"name": "suresh", "subject": "physics"},
#     103: {"name": "meena", "subject": "computer science"}
# }
# @app.route('/staff', methods=['GET'])
# def get_all_staff():
#     try:
#         return jsonify(staff_data)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         print("GET All staff called")
# @app.route('/staff/<int:staff_id>', methods=['GET'])
# def get_staff_by_ID(staff_id):
#     try:
#         if staff_id not in staff_data:
#             return jsonify({"error": "Staff data not found"}), 404

#         return jsonify({
#             "staff_id": staff_id,
#             "details": staff_data[staff_id]
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         print("GET staff by ID called")
# if __name__=="__main__":
#     app.run(port=3000,debug=True)
