from flask import Flask,render_template,redirect,request,flash,session,url_for
import psycopg2
from mydb1 import conf_email_password,sale_info,sales_date,totalsales,bestproduct,bestdate,sales1,prods1,profit1

connect=psycopg2.connect(
    dbname='muduka_db',
    user='postgres', 
    host='localhost',
    password='12345',
    port=5433)

cur= connect.cursor()
app= Flask(__name__)
app.secret_key='dont tell anyone'


@app.route("/")
def hello():
    prods2=prods1()
    salee=sales1()
    datebest=bestdate()
    bestprod=bestproduct()
    sum_sales=totalsales()
    sale_date=[]
    day_sales=[]
    for j in sales_date():
      sale_date.append(str(j[0]))
      day_sales.append(str(j[1]))
    return render_template('index.html',sum_sales=sum_sales,sale_date=sale_date,day_sales=day_sales,bestprod=bestprod,datebest=datebest,salee=salee,prods2=prods2)
    

@app.route("/products")
def products():
    if "user_id" not in session:
       return redirect("/login")
    cur.execute('select * from products')
    prods=cur.fetchall()
    return render_template('products.html',product=prods)
    # return "products"
# pr=products()
# print(pr)


@app.route("/sales")
def sales():
    if "user_id" not in session:
       return redirect("/login")
    cur.execute('select * from sales')
    sals=cur.fetchall()

    cur.execute('select * from products')
    prods=cur.fetchall()
    return render_template('sales.html',sale=sals,product=prods)


@app.route("/add products", methods=["post"])
def addproducts():
 product_name=request.form['name']
 buying_price=request.form['buying price']
 selling_price=request.form['selling price']
 stock_quantity=request.form['stock quantity']
 values=(product_name,buying_price,selling_price,stock_quantity)
 insert_querry="""INSERT INTO products(
	 name, buying_price, sellimg_price, stock_quantity)
	VALUES (%s,%s,%s,%s);"""
 cur.execute(insert_querry,values)
 connect.commit()
 return redirect("/products")


@app.route("/add sales", methods=["post"])
def addsales():
    pid=request.form['pid']
    quantity=request.form['quantity']
    value=(pid,quantity)
    insert_sale="""INSERT INTO sales(
	 pid, quantity, created_at)
	VALUES ( %s, %s,now());"""
    cur.execute(insert_sale,value)
    connect.commit()
    flash("seccesful")
    return redirect("/sales")



# @app.route("/register")
# def users():
    
#     cur.execute('select * from users')
#     user0=cur.fetchall()
#     return render_template('register.html',user1=user0)


@app.route("/register",methods=['POST','GET'])
def addusers():
    if request.method=='POST':
     name=request.form['name']
     email=request.form['email']
     password=request.form['password']
     values=(name,email,password)
     insert="""INSERT INTO users(
	 name, email, password)
	 VALUES (%s, %s, %s);"""
     cur.execute(insert,values)
     connect.commit()
    return render_template("login.html")


@app.route("/login",methods=["POST",'GET'])
def login():
    
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        users=conf_email_password(email,password)
        # session["user"]=user
        if users:
           user_id,full_name=users
           session['user_id']=user_id
           session['user_name']=full_name
           return redirect (url_for('dasboard'))
              
        else:
           return redirect('/register')
    
    return render_template('login.html')
    
# @app.route("/user")
# def user():
#    if "user" in session:
#       user=session["user"]
#       return f"{user}"
#    else:
#       return redirect('/login')
   
@app.route('/dashboard')
def dasboard():
   if "user_id" not in session:
      return redirect ("/login")
   profit=profit1()
   saleee=sales()
   sum_sales=totalsales()
   productss=[]
   total_sales=[]
   sale_date=[]
   day_sales=[]
   for i in sale_info():
      productss.append(str(i[0]))
      total_sales.append(i[1])
   for j in sales_date():
      sale_date.append(str(j[0]))
      day_sales.append(str(j[1]))
    
   return render_template('dashboard.html',productss=productss,total_sales=total_sales,sale_date=sale_date,day_sales=day_sales,sum_sales=sum_sales,saleee=saleee,profit=profit)
connect.commit()


# @app.route("/dashboard")
# def totsale():
#     cur.execute("""SELECT SUM(sales.quantity * products.sellimg_price) AS total_sales
# 	FROM sales
# 	JOIN products ON products.id=sales.pid
# 	order by total_sales""")
#     tots=cur.fetchall()
#     print(tots)
#     return render_template('products.html',tots=tots)

# @app.route('/totalsales')
# def total():
#    totall=[]
#    for i in totalsales():
#       totall.append(i[0])
#    return render_template('index.html',totall=totall)
# connect.commit()





@app.route("/logout")
def logout():
    if 'user_id' in session:
        user_id=session['user_id']
        user_name=session["user_name"]
        session.pop("user_id",None)
        session.pop("user_name",None)
    return redirect(url_for('index.html'))


# @app.route("/single")
# def single():
#     return render_template ('single.html')

app.run(debug=True)
# @app.route('/dashboard')
# def dasboard():
#    productss=[]
#    total_sales=[]
#    for i in sale_info():
#       productss.append(str (i[0]))
#       total_sales.append(i[1])
#    return render_template('dashboard.html',productss=productss,total_sales=total_sales)
# connect.commit()
