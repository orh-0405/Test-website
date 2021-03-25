from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home/')
@app.route('/')
def website():
    return render_template('Prototype 2.html')

@app.route('/about/')
def about():
    return render_template("About.html")

@app.route('/start/')
def start():
    return render_template('1_start page.html')

@app.route('/survey/')
def survey():
    return render_template('2_survey.html')

@app.route('/personality/')
def personality():
    interaction = request.args["interaction"]
    prac = request.args["prac"]
    data = request.args["data"]
    arts = request.args["arts"]
    if interaction == "yes":
        personality = "Social"
        img = "social_car.jpeg"
        desc = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis labore, ratione deserunt perferendis aspernatur praesentium nisi, accusantium suscipit quisquam quos laborum vel quas saepe, ab dolorum reprehenderit quaerat asperiores. Porro!"
    elif prac == "yes":
        personality = "Practical"
        img = "practical_car.png"
        desc = "You enjoy working with machines, mechanisms and tools, and you might be interested in physical or biological processes, as well as building and modelling! Let’s take a look at the possible jobs you may be interested in that are in this category!"
    elif data == "yes":
        personality = "Data"
        img = "data_car.jpeg"
        desc = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis labore, ratione deserunt perferendis aspernatur praesentium nisi, accusantium suscipit quisquam quos laborum vel quas saepe, ab dolorum reprehenderit quaerat asperiores. Porro!"
    elif arts == "yes":
        personality = "Creative"
        img = "creative_car.jpeg"
        desc = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis labore, ratione deserunt perferendis aspernatur praesentium nisi, accusantium suscipit quisquam quos laborum vel quas saepe, ab dolorum reprehenderit quaerat asperiores. Porro!"

    elif interaction == "yes" and prac == "yes" and data == "yes" and arts == "yes":
        personality = "All-rounder"
        img = "creative_car.jpeg"
        desc = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis labore, ratione deserunt perferendis aspernatur praesentium nisi, accusantium suscipit quisquam quos laborum vel quas saepe, ab dolorum reprehenderit quaerat asperiores. Porro!"

    elif interaction == "no" and prac == "no" and data == "no" and arts == "no":
        personality = "None"
        img = ""
        desc = "its ok..."
    
    img = "../static/" + img

    return render_template('3_personality.html', personality=personality, img=img, desc=desc)

@app.route('/job_options/')
def jobs():
    return render_template('4_job_options.html')

@app.route('/job-desc/')
def doctor():
    return render_template('5_job_desc.html')

@app.route('/courses/')
def courses():
    return render_template('6_course.html')

if __name__ == '__main__':
    app.run(debug=True)