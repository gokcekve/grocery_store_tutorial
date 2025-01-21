""" 
* 3 parts included: 
  - frontend: web UI (html, css, js)
  - backend: python, flask
  - db: mysql workbench 

* to view the page: 
    - connect db 
    - run server.py file 
    - go index.html and open in browser
    - done your shopping operations and check db, orders will be viewed on db tables
    
Rules:
        When you create a new x_dao.py;
            - import it into server.py
            - connect it with sql in __main__ :     # connection = get_sql_connection()
            - in each function you create in a dao file;
                * you need a cursor first     :     # cursor = connection.cursor()
                * write your query            :     # query = (" ... ")
                * execute cursor              :     # cursor.execute(query)
                * after these steps, in case:
                    - 1. when you want to list all x's (get_all_x function):
                        you will need a list to store x as dicts :     # response = []
                        use for loop to reach each dict (x information) and add them to response
                    - 2. when you want to manipulate data (adding, deleting, inserting etc.):
                        you have to commit the change to see in db them :   #  connection.commit()
                * return response(for 1.case) or cursor(for 2.case)

-> for each function in dao file; connect the service in server.py file. (exception: order_dao / get_order_details())

Exercises will be done: 
1. IDE error: no conenction with db ( + solved)
2. Products: In products page that lists current products, add an edit button next to delete button that allows to edit current product
3. Products: Implement a new form that allows you to add new UOM in the application. For example you want to add Cubic Meter as a new UOM as the grocery store decided to start selling wood as well. This requies changing backend (python server) and front end (UI) both.
4. Orders: When you place an order it doesn't have any validation. For example one can enter an order with empty customer name. You need to add validation for customer name and invalid item name or not specifying a quantity etc. This is only front end UI work.
5. Orders: In new order page there is a bug. When you manually change total price of an item it doesn't change the grand total. You need to fix this issue.
6. Orders: In the grid where orders are listed, add a view button in the last column. On clicking this button it should show you order details where individual items in that order are listed along with their price/quantity etc.


"""
