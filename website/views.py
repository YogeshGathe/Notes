from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note, User
import json



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')


    return render_template("home.html", user=current_user)

@views.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_note(id):
    note=Note.query.get(id)
    db.session.delete(note)
    db.session.commit()
    flash('Note Deleted!', category='success')
    return redirect(url_for('views.home'))


@views.route('/update', methods=['POST', 'GET'])
@login_required
def update_page():
        return render_template("update.html", user=current_user)
    
@views.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update_note(id):
    note=Note.query.get_or_404(id)
    if request.method=='POST':
        note.data = request.form.get('note')
        print(note.data)
        # db.session.delete(note)
        db.session.commit()
        flash('Note Updated!', category='success')
        return redirect(url_for('views.home'))
    

@views.route('/search', methods=['POST'])
@login_required
def search_note():
        key=request.form.get('key')
        notes_q=Note.query
        # user=current_user
        searched=notes_q.filter(Note.data.like('%'+key+'%'), Note.user_id == current_user.id).all()
        if searched:
             return render_template("search.html", user=current_user, searched=searched)
        else:
             flash("No Notes Found!", category= "error")
             return redirect(url_for('views.home'))

            

    