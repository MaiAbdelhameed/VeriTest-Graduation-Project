import os
import shutil
from flask import Flask, request, jsonify, send_file
import tempfile
import zipfile
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)


@app.route('/upload_files', methods=['POST'])
def upload_files():
    # Get Mode_Number field from form data
    mode_number = request.form.get('Mode_Number')
    if mode_number == '1':
        try:
            v_file = request.files['vFile']
            py_file = request.files['pyFile']
            # Save or process the uploaded files here
            v_file.save('uploaded_files/' + v_file.filename)
            py_file.save('uploaded_files/' + py_file.filename)

            arguments = []
            arguments.append(os.path.abspath(
                f"uploaded_files/{v_file.filename}"))
            arguments.append(os.path.abspath(
                f"uploaded_files/{py_file.filename}"))

            # Run the Bash script with command-line arguments
            HOME = os.environ.get('VERITEST_HOME')
            subprocess.run(
                ['bash', f"{HOME}/mode_selection.bash"] + arguments, check=True)

            ################################

            directory_to_zip = f'{HOME}/web_portal/backend/results'

            # Create a temporary file to store the ZIP archive
            zip_fd, zip_path = tempfile.mkstemp()
            os.close(zip_fd)

            # Create a ZIP archive of the directory
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(directory_to_zip):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(
                            file_path, directory_to_zip))
            #########################
            # Delete the individual uploaded files
            os.remove('uploaded_files/' + v_file.filename)
            os.remove('uploaded_files/' + py_file.filename)

            # Return the zip file for download

            return send_file(zip_path, as_attachment=True)
        except Exception as e:
            print("EXCEPTION")
            print(e)
            return jsonify(success=False, error=str(e)), 400
###############################################################################
    elif (mode_number == '2'):
        try:
            v_file = request.files['vFile']
            jsonfile = request.files['jsonFile']
            # Save or process the uploaded files here
            v_file.save('uploaded_files/' + v_file.filename)
            jsonfile.save('uploaded_files/' + jsonfile.filename)

            arguments = []
            arguments.append(os.path.abspath(
                f"uploaded_files/{v_file.filename}"))
            arguments.append(os.path.abspath(
                f"uploaded_files/{jsonfile.filename}"))

            # Run the Bash script with command-line arguments
            HOME = os.environ.get('VERITEST_HOME')
            subprocess.run(
                ['bash', f"{HOME}/mode_selection.bash"] + arguments, check=True)

            ################################

            directory_to_zip = f'{HOME}/web_portal/backend/results'

            # Create a temporary file to store the ZIP archive
            zip_fd, zip_path = tempfile.mkstemp()
            os.close(zip_fd)

            # Create a ZIP archive of the directory
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(directory_to_zip):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(
                            file_path, directory_to_zip))
            #########################
            # Delete the individual uploaded files
            os.remove('uploaded_files/' + v_file.filename)
            os.remove('uploaded_files/' + jsonfile.filename)

            # Return the zip file for download

            return send_file(zip_path, as_attachment=True)
        except Exception as e:
            print("EXCEPTION")
            print(e)
            return jsonify(success=False, error=str(e)), 400
###############################################################################
    elif (mode_number == '3'):
        v_file = request.files['vFile']
        v_file.save('uploaded_files/' + v_file.filename)
        arguments = []
        arguments.append(os.path.abspath(
            f"uploaded_files/{v_file.filename}"))
        HOME = os.environ.get('VERITEST_HOME')
        subprocess.run(
            ['bash', f"{HOME}/Mode_3/entry_point.bash"] + arguments, check=True)
        predicted_json = {}
        with open(f"uploaded_files/predicted.json", "r") as json_file:
            data = json.load(json_file)
        os.remove('uploaded_files/' + v_file.filename)
        os.remove('uploaded_files/predicted.json')
        return jsonify(data), 200
    else:
        return jsonify(success=False, error="Invalid Mode_Number"), 400

#########################################################


@app.route('/submit_prediction', methods=['POST'])
def submit_prediction():
    try:
        json_data = request.form.get('json')
        if json_data:
            circuit_dict = json.loads(json_data)

        # Get the file
        v_file = request.files['vFile']
        # save V file
        v_file.save('uploaded_files/' + v_file.filename)
        # save JSON to file
        json_filename = f'uploaded_files/{v_file.filename.split(".")[0]}.json'
        with open(json_filename, "w") as json_file:
            json.dump(circuit_dict, json_file)

        #####################################################
        # script arguments
        arguments = []
        arguments.append(os.path.abspath(f"uploaded_files/{v_file.filename}"))
        arguments.append(os.path.abspath(
            f'uploaded_files/{v_file.filename.split(".")[0]}.json'))
        print(arguments)
        # Run the Bash script with command-line arguments
        HOME = os.environ.get('VERITEST_HOME')
        subprocess.run(
            ['bash', f"{HOME}/mode_selection.bash"] + arguments, check=True)

        ##################################################
        directory_to_zip = f'{HOME}/web_portal/backend/results'

        # Create a temporary file to store the ZIP archive
        zip_fd, zip_path = tempfile.mkstemp()
        os.close(zip_fd)

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory_to_zip):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(
                        file_path, directory_to_zip))
        #########################
        # Delete the individual uploaded files
        os.remove('uploaded_files/' + v_file.filename)
        os.remove(f'uploaded_files/{v_file.filename.split(".")[0]}.json')

        # delete results
        directory_to_delete = "results"
        shutil.rmtree(directory_to_delete)

        # Return the zip file for download
        return send_file(zip_path, as_attachment=True)

    except Exception as e:
        print("EXCEPTION")
        print(e)
        return jsonify(success=False, error=str(e)), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
