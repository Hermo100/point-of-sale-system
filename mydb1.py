import psycopg2

connect=psycopg2.connect(
    dbname='muduka_db',
    user='postgres', 
    host='localhost',
    password='12345',
    port=5433)

cur=connect.cursor()


def conf_email_password(email,password):
    query="select id,name from users WHERE email=%s AND password=%s"
    cur.execute(query,(email,password))
    result=cur.fetchone()
    if result is not None:
        id=result[0]
        name=result[1]
        return id,name
    else:
        return None



def sale_info():
    cur= connect.cursor()
    sales_info="""SELECT products.name,SUM(sales.quantity) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	GROUP BY products.name;"""
    cur.execute(sales_info)
    info=cur.fetchall()
  
    return info


def sales_date():
    cur= connect.cursor()
    saless_date="""SELECT DATE(sales.created_at) SaleDate,SUM(sales.quantity * products.sellimg_price) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	GROUP BY SaleDate
	order by SaleDate;"""
    cur.execute(saless_date)
    info1=cur.fetchall()
   
    return info1


def totalsales():
    cur= connect.cursor()
    total_saless="""SELECT SUM(sales.quantity * products.sellimg_price) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	order by total_sales"""
    cur.execute(total_saless)
    info2=cur.fetchall()
    print(info2)
    return info2


def bestproduct():
    cur= connect.cursor()
    best="""SELECT products.name,SUM(sales.quantity * products.sellimg_price) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	GROUP BY products.name
	order by total_sales desc
	limit 1;"""
    cur.execute(best)
    info3=cur.fetchall()
    print(info3)
    return info3


def bestdate():
    cur= connect.cursor()
    
    bestday="""SELECT DATE(sales.created_at) SaleDate,SUM(sales.quantity * products.sellimg_price) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	GROUP BY SaleDate
	order by total_sales desc
	limit 1;"""
    cur.execute(bestday)
    info4=cur.fetchall()
    print(info4)
    return info4
    

def sales1():
    cur= connect.cursor()
    
    sale2="""SELECT products.name,sales.created_at,SUM(sales.quantity * products.sellimg_price) AS total_sales
	FROM sales
	JOIN products ON products.id=sales.pid
	GROUP BY products.name,sales.created_at;"""
    cur.execute(sale2)
    info5=cur.fetchall()
    print(info5)
    return info5


def prods1():
     cur.execute('select * from products')
     prods=cur.fetchall()
     return prods 
    
    
def profit1():
    cur= connect.cursor()
    profit2="""SELECT DATE(created_at) AS mydate,
    SUM((sellimg_price - buying_price) * sales.quantity) AS profit 
    FROM sales 
    JOIN products ON products.id = sales.pid 
    GROUP BY mydate 
    ORDER BY mydate"""
    cur.execute(profit2)
    info6=cur.fetchall()
    print(info6)
    return info6
# cur= connect.cursor()
# total_saless="""SELECT SUM(sales.quantity * products.sellimg_price) AS total_sales
# 	FROM sales
# 	JOIN products ON products.id=sales.pid
# 	order by total_sales"""
# cur.execute(total_saless)
# info2=cur.fetchall()
# print(info2)

# cur= connect.cursor()
    
# best="""SELECT products.name,SUM(sales.quantity * products.sellimg_price) AS total_sales
# 	FROM sales
# 	JOIN products ON products.id=sales.pid
# 	GROUP BY products.name
# 	order by total_sales desc;"""
# cur.execute(best)
# info3=cur.fetchall()
# print(info3)
