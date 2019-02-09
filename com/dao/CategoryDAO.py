from project.com.dao import con


class CategoryDAO:

    def insertCategory(self,CategoryVO):

            connection = con()
            cursor1 = connection.cursor()
            cursor1.execute("INSERT INTO categorymaster(categoryName,categoryDescription)VALUES('"+CategoryVO.categoryName+"','"+CategoryVO.categoryDescription+"')")
            connection.commit()
            cursor1.close()
            connection.close()