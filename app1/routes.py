from flask import render_template, url_for, flash, redirect
from app1 import app, db
from app1.forms import RegistrationForm
from app1.models import User
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split  # Importing the necessary libraries
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

db.create_all()


@app.route("/covid", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # user = User(oxygen_concentration=form.oxygen_concentration.data, dry_cough=form.dry_cough.data,
        #  septic_shock=form.septic_shock.data, age=form.age.data, breathe_rate=form.breathe_rate.data,
        # prior_disease=form.prior_disease.data)

        dataset = pd.read_csv('C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\Covid19_Final_dataset.csv')
        # Reading the covid-19 dataset using pandas
        # print(dataset.head())
        dataset = dataset.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
        # Cleaning the dataset to increase the performance
        septic_shock = LabelEncoder()
        dry_cough = LabelEncoder()  # Labelling the string data as integers
        prior_disease = LabelEncoder()
        dataset['Septic_Shock'] = septic_shock.fit_transform(dataset['Septic Shock'])
        dataset['Dry_Cough'] = dry_cough.fit_transform(dataset['Dry Cough'])  # Creating new columns of labelled data
        dataset['Prior_Disease'] = prior_disease.fit_transform(dataset['Prior Respiratory Disease'])
        x = np.array(dataset.drop(['Septic Shock', 'Dry Cough', 'Prior Respiratory Disease', 'Severity Status'],axis='columns'))
        # Creating a feature data
        y = np.array(dataset['Severity Status'])  # creating the target data
        reg = KNeighborsClassifier(n_neighbors=1)  # training the model using K nearest neighbour algorithm
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
        # splitting the data into training and testing data. 30% of the data is for testing
        reg.fit(x_train, y_train)
        reg.fit(x_train, y_train)  # training the model
        # print(x_train)
        # print('The model gives you information about COVID-19 status based on your visible symptoms')
        # print('Enter 0 if your answer is No, if answer is Yes, enter 1')
        breadth_rate = form.breathe_rate.data
        oxygen_concentration = form.oxygen_concentration.data
        age = form.age.data
        septic_shock = form.septic_shock.data
        dry_cough = form.dry_cough.data
        prior_disease = form.prior_disease.data

        classified = reg.predict([[breadth_rate, oxygen_concentration, age, septic_shock, dry_cough, prior_disease]])
        # classify the input features or symptoms.
        if classified == 0 or classified == 1:
            temp = 'The symptoms do not promise COVID-19. Stay alert and take every possible precaution.\n'
            if dry_cough == 1:
                temp += 'At-home treatments"\n"A cough that results from a virus can’t be treated with antibiotics. ' \
                        'You can, however, soothe it in the following ways:\n1. Keep hydrated by drinking plenty of ' \
                        'water.\n2. Elevate your head with extra pillows when sleeping.\n3. Use cough drops to ' \
                        'soothe your throat.\n4. Gargle with warm salt water regularly to remove mucus and soothe ' \
                        'your throat.\n5. Avoid irritants, including smoke and dust.\n6. Add honey or ginger to hot ' \
                        'tea to relieve your cough and clear your airway.\n7. Use decongestant sprays to unblock ' \
                        'your nose and ease breathing.\n'
            string = User(string1=temp)
            db.session.add(string)
        elif classified == 2:
            string = User(string1='The symptoms direct to a moderate case.')  # telling the user, the condition
            db.session.add(string)
        else:
            string = User(string1='The symptoms correspond to a critical case.')
            db.session.add(string)
        db.session.commit()
        # db.session.add(user)
        # db.session.commit()
        return redirect(url_for('details'))
    return render_template('Covid-19.html', form=form)


@app.route('/details')
def details():
    details_of_user = User.query.all()
    return render_template('Details.html', details_of_user=str(details_of_user[-1]), coordinates=coordinates)
