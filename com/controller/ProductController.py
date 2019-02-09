from flask import render_template,request
from project import app
from project.com.dao.ProductDAO import ProductDAO
from project.com.vo.ProductVO import ProductVO

@app.route('/addProduct')
def addProduct():

   return render_template("admin/addProduct.html")

@app.route('/insertProduct',methods=["POST"])
def insertProduct():


    productVO = ProductVO()
    productDAO = ProductDAO()

    productCategory = request.form['productCategory']
    productSubategory = request.form['productSubategory']
    productName = request.form['productName']
    productPrice = request.form['productPrice']
    expDate = request.form['expDate']
    mfgDate = request.form['mfgDate']

    productVO.productCategory =  productCategory
    productVO.productSubategory= productSubategory
    productVO.productName = productName
    productVO.productPrice = productPrice
    productVO.expDate = expDate
    productVO.mfgDate = mfgDate

    productDAO.insertProduct(productVO)

    return render_template('admin/addProduct.html')