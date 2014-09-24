from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()
app = Flask(__name__)      
app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'alfie.2012@gmail.com'
app.config["MAIL_PASSWORD"] = 'masquerader'
 
mail.init_app(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')
 
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm(request.form)
 
  if request.method == 'POST' and form.validate():
    msg = Message(form.subject.data, sender='alfie.2012@gmail.com', recipients=['alfie.2012@gmail.com'])
    msg.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)

    return render_template('contact.html', success=True)
  else:
    print form.data
    return render_template('contact.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)
