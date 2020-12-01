from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('PRODUCT', 'PRODUCT'), ('IDEA', 'IDEA'), ('Business', 'Business')],
                           validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    """
    Class to create a wtf form for creating a pitch
    """
    opinion = TextAreaField('WRITE YOUR COMMENT',validators=[Required()])
    submit = SubmitField('SUBMIT')

class Vote(FlaskForm):
    submit = SelectField('Like')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])
    submit = SubmitField('Post')