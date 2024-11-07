# Document-to-Pdf-converter
# DOCX to PDF Converter Flask App

This Flask application allows users to upload DOCX files and converts them to PDF for download.

## Libraries Used:

- **Flask**: Framework for building the web application.
- **render_template**: Renders HTML templates for the user interface.
- **request**: Handles user requests (e.g., file uploads).
- **redirect**: Redirects users to different routes within the app.
- **url_for**: Generates URLs for specific routes in the application.
- **send_file**: Sends converted PDF files for download.
- **docx2pdf**: Library for converting DOCX files to PDF.
- **os**: Provides functionalities for interacting with the operating system (e.g., creating directories).

## Flask App:

- **app = Flask(__name__, static_folder='static')**: 
  - Initializes the Flask application.
  - `__name__`: Refers to the current Python module.
  - `static_folder='static'`: Specifies the folder for static files (e.g., HTML templates).

## Routes:

- `@app.route("/", methods=["GET", "POST"])`: 
  - Defines the route for the root URL `/`.
  - Handles both GET (displaying the upload form) and POST (processing file uploads).
  - Calls the `upload_file()` function.

- `@app.route("/uploads/<filename>")`: 
  - Defines the route for downloading converted PDFs.
  - Accepts the filename parameter in the URL.
  - Calls the `uploaded_file()` function.

## Functions:

- **upload_file()**: 
  - Handles file uploads and DOCX-to-PDF conversion.
  - Checks for uploaded files in the POST request.
  - Saves the uploaded DOCX file.
  - Converts the DOCX file to PDF using `docx2pdf`.
  - Redirects to a success page or displays a success message.

- **uploaded_file(filename)**: 
  - Handles the downloading of converted PDFs.
  - Sends the converted PDF to the user as an attachment using `send_file()`.

## Running the App:

- `if __name__ == "__main__":`: 
  - Ensures the script runs directly (not imported as a module).
  - `app.run(debug=True)`: Runs the Flask development server in debug mode for easier testing.

