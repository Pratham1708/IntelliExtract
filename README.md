# IntelliExtract: Named Entity Recognition Tool

IntelliExtract is a web-based Named Entity Recognition (NER) tool built using Flask and spaCy. It allows users to extract entities such as names, locations, dates, and organizations from the given text.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- Web-based UI for easy text input
- Extracts named entities using **spaCy**
- Displays extracted entities in a table
- Saves extracted entities as a CSV file
- User-friendly interface built with Flask

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/IntelliExtract.git
   cd IntelliExtract
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Download the spaCy English Model**
   ```sh
   python -m spacy download en_core_web_sm
   ```

## Usage
### Running the Application
To start the Flask app, run:
```sh
python app.py
```
This will start the server, and you can access it in your browser at:
```
http://127.0.0.1:5000/
```

### How to Use
1. Enter or paste text into the input box.
2. Click the **Extract Entities** button.
3. View the extracted entities categorized by type.
4. Optionally, download the extracted data as a CSV file.

## Project Structure
```
IntelliExtract/
│── static/            # CSS and JS files
│── templates/         # HTML templates
│── app.py            # Main Flask application
│── requirements.txt   # List of dependencies
│── README.md          # Project documentation
```

## Technologies Used
- **Flask** (Backend framework)
- **spaCy** (NER engine)
- **pandas** (Data handling and exporting to CSV)
- **HTML/CSS** (Frontend UI)

## Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

## Contact
For any inquiries, feel free to reach out via GitHub or email at `jindalpratham68@gmail.com`.

