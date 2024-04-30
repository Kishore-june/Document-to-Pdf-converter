from flask import Flask, render_template, request, redirect, url_for, send_file
from docx2pdf import convert
import os

app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def upload_file():
    """
    Handle file upload and conversion to PDF
    """
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return redirect(request.url)

        # Get the file extension and create a new filename for the PDF
        filename, file_extension = os.path.splitext(file.filename)
        pdf_filename = f"{filename}.pdf"

        # Save the uploaded file
        upload_folder='upload'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        converted_file = os.path.join(upload_folder,filename + file_extension)
        file.save(converted_file)

        # Convert the file to PDF
        pdf_file = os.path.join(upload_folder, pdf_filename)
        convert(converted_file, pdf_file)

        # Return a success message or redirect to a success page
        print("File uploaded and converted successfully!", 200)
        return redirect(url_for("uploaded_file", filename=pdf_filename)) 

    return render_template("upload.html")

@app.route("/uploads/<filename>")

def uploaded_file(filename):
    upload_folder = 'upload'
    file_path = os.path.join(upload_folder, filename)
    return send_file(file_path, as_attachment = True)

    # return render_template("download.html", filename=filename, as_attachment = True)

if __name__ == "__main__":
    app.run(debug=True)