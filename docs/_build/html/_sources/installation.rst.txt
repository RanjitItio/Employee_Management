Installation Guide
===================

This installation guide provides step-by-step instructions for setting up and running a Django application locally. It covers environment setup, software requirements, database setup (using PostgreSQL), project configuration, and running the application on a local server.

Environment Setup
------------------

1. Ensure you have a compatible operating system such as Windows, Linux, or MacOS.
2. Install Python from the official website (https://www.python.org/downloads/) above Python 3.

Software Required
------------------

1. **Python**: Python Programming Language
2. **Django**: Web Framework for building web applications

Project Configuration
----------------------

1. **Create Virtual Environment**:
   - Open a terminal or command prompt.
   - Run the following command to create a virtual environment named `virtual_env`:

     ::
        
        python -m venv virtual_env

2. **Activate Virtual Environment**:
   - Navigate to the virtual environment directory:

     ::
        
        cd virtual_env

   - Activate the virtual environment:
     - On Windows:

       ::
       
           Scripts\activate

     - On MacOS and Linux:

       ::
       
           source bin/activate

3. **Clone the Git Repository**:
   - Run the following command to clone the Git repository:

     ::
        
        git clone https://github.com/RanjitItio/Employee_Management.git

4. **Install Required Packages**:
   - Navigate to the cloned project directory:

     ::
        
        cd Employee_Management

   - Install the required Python packages listed in the `requirements.txt` file:

     ::
        
        pip install -r requirements.txt

5. **Run the Local Development Server**:
   - Start the local development server by running the following command:

     ::
        
        python manage.py runserver

6. **Access the Application**:
   - Open a web browser and enter the following URL:

     ::
        
        http://127.0.0.1:8000/
