from flask import render_template,request
from project import app
from project.com.dao.SubcategoryDAO import SubcategoryDAO
from project.com.vo.SubcategoryVO import SubcategoryVO

@app.route('/addSubcategory')
def addSubcategory():

   return render_template("admin/addSubcategory.html")
@app.route('/insertSubcategory',methods=["POST"])
def insertSubcategory():

    subcategoryVO = SubcategoryVO()
    subcategoryDAO = SubcategoryDAO()

    CategoryId = request.form['CategoryId']
    subcategoryName  = request.form['subcategoryName']
    subcategoryDescription = request.form['subcategoryDescription']

    SubcategoryVO.CategoryId = CategoryId
    SubcategoryVO.subcategoryName = subcategoryName
    SubcategoryVO.subcategoryDescription = subcategoryDescription

    subcategoryDAO.insertSubcategory(subcategoryVO)

    return render_template('admin/addSubcategory.html')