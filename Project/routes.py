# app/routes.py
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from Project import db, bcrypt, app, summarizer
from Project.models import User, Email
from Project.forms import RegistrationForm, LoginForm, UpdateAccountForm, ComposeEmailForm, RequestResetForm, ResetPasswordForm
from flask_login import login_user, current_user, logout_user, login_required
from PIL import Image
import os
import secrets
from datetime import datetime, timedelta

# LOGIC FOR SAVING PROFILE PICTURE
def save_picture(form_picture, old_picture):
    # Delete the old profile picture if it exists and is not the default image
    if old_picture != 'default.png':
        old_picture_path = os.path.join(app.root_path, 'static/profile_pics', old_picture)
        if os.path.exists(old_picture_path):
            os.remove(old_picture_path)
    # Ensure the directory exists
    picture_dir = os.path.join(app.root_path, 'static/profile_pics')
    if not os.path.exists(picture_dir):
        os.makedirs(picture_dir)
    # Save the new profile picture
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(picture_dir, picture_fn)
    # Resize the image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)  # Save the uploaded file
    return picture_fn

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    title = data.get('title', '')
    body = data.get('body', '')
    input_text = title + ' ' + body
    input_length = len(input_text.split())
    max_length = min(130, input_length // 2)  # Adjust max_length based on input length
    summary = summarizer(input_text, max_length=max_length, min_length=30, do_sample=False)
    return jsonify(summary=summary[0]['summary_text'])

# Home
@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('inbox'))
    return render_template('home.html', datetime=datetime, timedelta=timedelta, Email=Email)

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('inbox'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # Transaction
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, datetime=datetime, timedelta=timedelta, Email=Email)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inbox'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('inbox'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    return render_template('login.html', form=form, datetime=datetime, timedelta=timedelta, Email=Email)

# Account
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data, current_user.image_file)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, datetime=datetime, timedelta=timedelta, Email=Email)

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('inbox'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            return redirect(url_for('reset_password_form', email=form.email.data))
        else:
            flash('No account found with that email.', 'warning')
            return redirect(url_for('reset_request'))
    return render_template('reset_request.html', title='Reset Password', form=form, datetime=datetime, timedelta=timedelta, Email=Email)

@app.route('/reset_password_form/<email>', methods=['GET', 'POST'])
def reset_password_form(email):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('login'))
    return render_template('reset_password.html', title='Reset Password', form=form, email=email, datetime=datetime, timedelta=timedelta, Email=Email)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been reset.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_password.html', title='Reset Password', form=form, datetime=datetime, timedelta=timedelta, Email=Email)

# Inbox
@app.route("/inbox")
@login_required
def inbox():
    emails = Email.query.filter_by(recipient=current_user.email).all()
    return render_template('inbox.html', emails=emails, datetime=datetime, timedelta=timedelta, Email=Email)

# Sent
@app.route("/sent")
@login_required
def sent():
    sent_emails = Email.query.filter_by(sender_id=current_user.id).all()
    return render_template('sent.html', sent_emails=sent_emails, datetime=datetime, timedelta=timedelta, Email=Email)


@app.route("/email/<int:email_id>")
@login_required
def view_email(email_id):
    email = Email.query.get_or_404(email_id)
    if email.sender_id != current_user.id and email.recipient != current_user.email:
        abort(403)
    return render_template('view_email.html', email=email, datetime=datetime, timedelta=timedelta, Email=Email)

# Delete
@app.route("/email/<int:email_id>/delete", methods=['POST'])
@login_required
def delete_email(email_id):
    email = Email.query.get_or_404(email_id)
    # Ensure the current user is either the sender or the recipient
    if email.sender_id != current_user.id and email.recipient != current_user.email:
        abort(403)
    db.session.delete(email)
    db.session.commit()
    flash('Email has been deleted!', 'success')
    return redirect(url_for('inbox'))

# Compose
@app.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    form = ComposeEmailForm()
    if form.validate_on_submit():
        recipient = form.recipient.data
        user = User.query.filter_by(email=recipient).first()
        if user:
            subject = form.subject.data
            body = form.body.data
            category = form.category.data
            email = Email(sender=current_user.email, recipient=recipient, subject=subject, body=body, sender_id=current_user.id, category=category)
            db.session.add(email)
            db.session.commit()
            flash('Your email has been sent!', 'success')
            # Create a new form instance to clear the fields
            form = ComposeEmailForm()
            return redirect(url_for('compose'))
        else:
            flash('The recipient email does not exist.', 'danger')
            return redirect(url_for('compose'))
    return render_template('compose.html', form=form, datetime=datetime, timedelta=timedelta, Email=Email)

@app.route("/inbox/<category>")
@login_required
def inbox_category(category):
    emails = Email.query.filter_by(recipient=current_user.email, category=category).all()
    return render_template('inbox.html', emails=emails, selected_category=category, datetime=datetime, timedelta=timedelta, Email=Email)

@app.route("/sent/<category>")
@login_required
def sent_category(category):
    sent_emails = Email.query.filter_by(sender_id=current_user.id, category=category).all()
    return render_template('sent.html', sent_emails=sent_emails, selected_category=category, datetime=datetime, timedelta=timedelta, Email=Email)

# About
@app.route('/about')
def about():
    return render_template('about.html', title='About', datetime=datetime, timedelta=timedelta, Email=Email)
