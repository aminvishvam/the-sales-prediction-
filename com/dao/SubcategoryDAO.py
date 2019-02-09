from project.com.dao import con


class SubcategoryDAO:

    def insertSubcategory(self,SubcategoryVO):

            connection = con()
            cursor1 = connection.cursor()
            cursor1.execute("INSERT INTO subcategorymaster(CategoryId,subcategoryName,subcategoryDescription)VALUES('"+SubcategoryVO.CategoryId+"','"+SubcategoryVO.subcategoryName+"','"+SubcategoryVO.subcategoryDescription +"')")
            connection.commit()
            cursor1.close()
            connection.close()