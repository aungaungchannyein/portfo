from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:pagename>')
def my_page(pagename):
	return render_template(pagename)

def write_to_file(data):
	with open('database.txt',mode='a')as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a')as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(database2,delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method=='POST':
  	try:
	  	data=request.form.to_dict()
	  	write_to_csv(data)
  		return redirect('/thankyou.html')
  	except:
  		return 'did not save to database'
  else:
  	return'something went wrong'

       
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    

# @app.route('/work.html')
# def my_work():
# 	return render_template('work.html')

# @app.route('/works.html')
# def my_works():
# 	return render_template('works.html')

# @app.route('/about.html')
# def my_about():
# 	return render_template('about.html')

# @app.route('/components.html')
# def my_components():
# 	return render_template('components.html')

# @app.route('/contact.html')
# def my_contact():
# 	return render_template('contact.html')

