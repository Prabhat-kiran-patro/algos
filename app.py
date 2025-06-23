from flask import Flask, render_template, request

from algorithms.algorithms import Sorting

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<algorithm_name>', methods=['GET', 'POST'])
def algorithm(algorithm_name):
    result = None
    time_taken = None
    formatted_time = None
    valid = None
    user_input = None
    if request.method == 'POST':
        # getting user input from form
        user_input = request.form.get('user_input').strip() # the param is name of the input tag

        # applying algorithms
        try:
            if not user_input:
                valid = 0
            else:
                valid = 1
            if algorithm_name == 'bblsrt':
                ulist = user_input.split()
                for i in range(len(ulist)):
                    ulist[i] = int(ulist[i])
                time_taken = Sorting.bubble_sort(ulist)
                result = ulist
            elif algorithm_name == 'selecsrt':
                ulist = user_input.split()
                for i in range(len(ulist)):
                    ulist[i] = int(ulist[i])
                time_taken = Sorting.selection_sort(ulist)
                result = ulist
            elif algorithm_name == 'insersrt':
                ulist = user_input.split()
                for i in range(len(ulist)):
                    ulist[i] = int(ulist[i])
                time_taken = Sorting.insertion_sort(ulist)
                result = ulist
            elif algorithm_name == 'mergesrt':
                ulist = user_input.split()
                for i in range(len(ulist)):
                    ulist[i] = int(ulist[i])
                time_taken = Sorting.merge_sort(ulist)
                result = ulist
            

            
            if time_taken:
                time_taken_ms = time_taken / 1000  # converting to milliseconds
                formatted_time = f"{time_taken_ms:.5f} ms"

        except ValueError:
            valid = 0
        
        
    return render_template(
        'algorithm.html',
        active_algorithm=algorithm_name,
        result=result,
        time_taken=formatted_time,
        uinput=user_input,
        ipvalidity=valid
    )


if __name__=="__main__":
    app.run(debug=True)