from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy 
from sorting_alg.merge_sort import MergeSort
from sorting_alg.quick_sort import QuickSort
from sorting_alg.selection_sort import SelectionSort
from sorting_alg.bubble_sort import BubbleSort
from sorting_alg.insertion_sort import InsertionSort

app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# class User(db.Model):
#     id = db.Column(db.Integer)
#     username = db.Column(db.String(20)) 

def convert_array(value):
    array = []
    i = 0
    num = ""
    last_comma = 0
    while i < len(value):
      if value[i] == ",":
        array.append(int(num))
        last_comma = i
        num = ""
      else:
          num += value[i]
      i += 1 
    array.append(int(value[last_comma+1:]))
    return array

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        value = request.form["numbers"]
        select = request.form["sorting"]
        array = convert_array(value)

        if select == "merge_sort":
            alg = MergeSort()
            alg.mergeSort(array.copy(), 0, len(array)-1)
            array_str = str(alg.sorting_steps)
            return render_template('index.html', sorting= "Merge Sort", original=value, arr=array_str)
        
        elif select == "bubble_sort":
            alg = BubbleSort()
            alg.bubbleSort(array.copy())
            array_str = str(alg.sorting_steps)
            return render_template('index.html', sorting= "Bubble Sort", original=value, arr=array_str)

        elif select == "selection_sort":
            alg = SelectionSort()
            alg.selectionSort(array.copy())
            array_str = str(alg.sorting_steps)
            return render_template('index.html', sorting= "Selection Sort", original=value, arr=array_str)

        elif select == "insertion_sort":
            alg = InsertionSort()
            alg.insertionSort(array.copy())
            array_str = str(alg.sorting_steps)
            return render_template('index.html', sorting= "Insertion Sort", original=value, arr=array_str)

        elif select == "quick_sort":
            alg = QuickSort()
            alg.quickSort(array.copy(), 0, len(array)-1)
            array_str = str(alg.sorting_steps)
            return render_template('index.html', sorting= "Quick Sort", original=value, arr=array_str)

        else:
            return render_template('index.html', sorting= "No Sorting Algorithm", original=value, arr=[])

    else:
        return render_template('index.html')
        