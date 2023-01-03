from flask import Flask, escape ,request,render_template
import pickle
gs = pickle.load(open('Churn_model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        credit_score=int(request.form['credit_score'])
        country=request.form['country']
        age=int(request.form['age'])
        estimated_salary=float(request.form['estimated_salary'])
        balance=float(request.form['balance'])
        credit_card=int(request.form['credit_card'])
        gender=request.form['gender']
       
        # gender
        if gender=="Male":
            gender_Male = 1
            gender_Other = 0
        elif gender=="Other":
            gender_Male=0
            gender_Other=1
        else:
            gender_Male=0
            gender_Other=0
       
        # Credit card
        if credit_card == 'yes':
            credit_card_yes = 1
            credit_card_no = 0
        if credit_card == 'No':
            credit_card_no = 0
            credit_card_yes = 1
        else:
            credit_card_yes=0
            credit_card_no=0

        return render_template("prediction.html", prediction_text="Is churn {}".format(prediction))        

    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)
    