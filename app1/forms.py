from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    oxygen_concentration = IntegerField('Oxygen Concentration in Blood(in percentage)', validators=[DataRequired()])
    dry_cough = IntegerField('Dry Cough', render_kw={"placeholder": 'Enter 1 for Yes and 0 for No'})
    septic_shock = IntegerField('Septic Shock', render_kw={"placeholder": 'Enter 1 for Yes and 0 for No'})
    age = IntegerField('Age', validators=[DataRequired()])
    breathe_rate = IntegerField('Breathe Rate(per minute)', validators=[DataRequired(), NumberRange(min=1, max=130)])
    prior_disease = IntegerField('Prior Respiratory Diseases', render_kw={"placeholder": 'Enter 1 for Yes and 0 for No'})
    submit = SubmitField('Get Details')