# Flask Web Application
This is a Flask-based web application with Docker support.

## Installation Requirements

### 1. Local Setup

#### Prerequisites
- **Python 3.9**
- **pip** (Python package installer)

#### Steps
1. **Clone the repository**:  
   `git clone git@github.com:rafogasparyan/web_application_flask.git && cd web_application_flask`
2. **Install dependencies**:  
   `pip install -r requirements.txt`
3. **Run the application**:  
   `python run.py`

The application will start on `http://0.0.0.0:5001` with debug mode enabled.

### 2. Docker Setup

#### Prerequisites
- **Docker** (with Docker Compose)

#### Steps
1. **Build and run the application**:  
   `docker-compose up --build`
2. **Access the application**:  
   Visit `http://localhost:5001` in your browser.
