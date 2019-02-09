from flask import render_template,request
from project import app
from  project.com.dao.CategoryDAO import CategoryDAO
from  project.com.vo.CategoryVO import CategoryVO

@app.route('/')
def loadIndex():
    return render_template('admin/index.html')


@app.route('/addCategory')
def addCategory():

   return render_template("admin/addCategory.html")


@app.route('/insertCategory',methods=["POST"])
def insertCategory():

    categoryVO = CategoryVO()
    categoryDAO = CategoryDAO()


    categoryName  = request.form['categoryName']
    categoryDescription = request.form['categoryDescription']

    categoryVO.categoryName = categoryName
    categoryVO.categoryDescription = categoryDescription

    categoryDAO.insertCategory(categoryVO)

    return render_template('admin/addCategory.html')