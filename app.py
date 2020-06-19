#!/usr/bin/env python3


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def init_recorder():
    return render_template('./index2.html')

@app.route('/get_canvas_images', methods=['POST', 'GET'])
def get_canvas_images():

    if request.method == 'POST':

        raw_images = request.get_data()

        symptoms = request.files["_symptoms"].read()
        symptom_image = open("canvas_images/symptoms.png", "wb")
        symptom_image.write(symptoms)
        symptom_image.close()

        diagnosis = request.files["_diagnosis"].read()
        diagnosis_image = open("canvas_images/diagnosis.png", "wb")
        diagnosis_image.write(diagnosis)
        diagnosis_image.close()

        treatment = request.files["_treatment"].read()
        treatment_image = open("canvas_images/treatment.png", "wb")
        treatment_image.write(treatment)
        treatment_image.close()

        tests = request.files["_tests"].read()
        tests_image = open("canvas_images/tests.png", "wb")
        tests_image.write(tests)
        tests_image.close()

        others = request.files["_others"].read()
        others_image = open("canvas_images/others.png", "wb")
        others_image.write(others)
        others_image.close()

        flag_file = open("canvas_images/flag.txt", "w+")
        flag_file.write("1")
        flag_file.close()

    return "CANVASES SAVED!!!"



if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=True)