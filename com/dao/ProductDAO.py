from project.com.dao import con


class ProductDAO:

    def insertProduct(self,ProductVO):

            connection = con()
            cursor1 = connection.cursor()
            cursor1.execute("INSERT INTO productmaster(productCategory,productSubategory,productName,productPrice,expDate,mfgDate)VALUES('"+ProductVO.productCategory+"','"+ProductVO.productSubategory+"','"+ProductVO.productName+"','"+ProductVO.productPrice+"','"+ProductVO.mfgDate+"','"+ProductVO.expDate+"')")
            connection.commit()
            cursor1.close()
            connection.close()