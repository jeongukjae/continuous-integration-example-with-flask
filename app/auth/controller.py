from flask import Blueprint, render_template, request, url_for, redirect

from .forms import SignInForm

auth_page = Blueprint('auth_page', __name__)

@auth_page.route('/signin', methods=['GET', 'POST'])
def signin(): 
    form = SignInForm(request.form)

    if form.validate_on_submit():
        return redirect(url_for('.success', email=form.email.data, name=form.name.data))

    return render_template('auth/signin.html', form=form)

@auth_page.route('/success', methods=['GET'])
def success():
    email = request.args.get('email')
    name = request.args.get('name')

    if email and name:
        return render_template('auth/success.html', data={
            'email': email,
            'name' : name
        })
    else:
        return "bad request"