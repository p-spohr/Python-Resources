from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, 
                     SelectField, TextAreaField, SubmitField, validators)
from markupsafe import escape

import logging

app = Flask(__name__)

# set up as env variable later
# app.config['SECRET_KEY'] = 'mysecretkey'
app.secret_key = 'mysecretkey' # same as above

class InfoForm(FlaskForm):
    owner = StringField(label= 'Owner name?', validators= [validators.DataRequired()])
    name = StringField(label= 'Dog name?', validators= [validators.DataRequired()])
    breed = StringField(label= 'Which breed?', validators= [validators.DataRequired()])
    neutered = BooleanField(label= 'Is neutered?')
    mood = RadioField(label= 'Please choose mood.', choices= [(-1, 'unhappy',), (0, 'ok'), (1, 'happy')])
    food = SelectField(label= u'Pick favorite food.', 
                       choices= [('chicken', 'Chicken'), ('beef', 'Beef'), ('fish', 'Fish')]) # u'' for unicode string
    feedback = TextAreaField(label= 'Feedback')
    submit = SubmitField(label= 'Submit')

class ClickMeForm(FlaskForm):
    submit = SubmitField(label= 'Click me!')


@app.route('/', methods= ['GET'])
def index():
    return '<h1>Welcome!</h1>'


@app.route('/click_me', methods= ['GET', 'POST'])
def click_me():
    form = ClickMeForm()
    # check if count is in session and set to zero
    if not session.get('count'):
        session['count'] = 0
    if form.validate_on_submit():
        session['count'] += 1
        app.logger.log(logging.INFO, f'Count: {session['count']}')
        flash(f'You just clicked the button {session['count']} times!')
        # flash('You just clicked the button!')
        return redirect(url_for('click_me'))
    return render_template('click_me.html', form= form)
    

@app.route('/form', methods= ['GET', 'POST'])
def form():
    form = InfoForm()
    if form.validate_on_submit():
        for label, data in form.data.items():
            session[label] = data
        # app.logger.info(session)
        # https://docs.python.org/3/library/logging.html#logging-levels
        # check out logging levels for more logging options
        app.logger.log(logging.INFO, session)
        return redirect(url_for('thank_you'))
    # make sure index.html is in templates directory!
    return render_template('form.html', form=form)


@app.route('/thank_you', methods= ['GET'])
def thank_you():
    # Inside templates you also have access to the config, request, session and g objects 
    # as well as the url_for() and get_flashed_messages() functions.
    # this passing of session to the template is not necessary
    # return render_template('thank_you.html', owner= session['owner'], name= session['name'], breed = session['breed'])        
    return render_template('thank_you.html')        


@app.route("/hello", methods= ['GET'])
def hello():
    name = request.args.get("name")
    return f"<h1>Hello, {escape(name)}!</h1>"


# variable sections to a URL: function receives the <variable_name> as a keyword argument.
@app.route('/user/<username>', methods= ['GET'])
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


# <converter:variable_name> to make type conversion
@app.route('/post/<int:post_id>', methods= ['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>', methods= ['GET'])
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# POST vs. GET: POST is also more secure than GET, because you aren't sticking information into a URL.
# POST has no size restrictions for transmitted data, 
# GET is limited to 2048 characters.
@app.route('/input', methods= ['GET'])
def input():
    username = request.args.get('username')
    html = f'''
        <form>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"> <br>
        <input type="submit" value="Submit">
        </form>
        <h1> {username if username else 'Please input username.'} </h1>
        '''
    return html
        
if __name__ == '__main__':
    app.run(debug= True)