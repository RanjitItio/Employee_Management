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

   - **ERROR**:
      - 1: Permission issues or missing dependencies

   - **ERROR HANDLING:**
      - 1: Ensure Python is installed correctly.
      - 2: Write permission in the working directory.
      - 3: Verify the virtual environment module is available.


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
   
   - **ERROR:**
      - 1: Command not Found
      - 2: Activation script is not running

   - **ERROR HANDLING:**
      - 1: Recheck the path to the activation Script, Ensuring the compatibility with the user's operating system.
      - 2: Troubleshooting any environment variable conflicts.


3. **Clone the Git Repository**:
   - Run the following command to clone the Git repository:

     ::
        
        git clone https://github.com/RanjitItio/Employee_Management.git

   - **ERROR:**
      - 1: Network connectivity issue
      - 2: Authentication Failure

   - **ERROR HANDLING:**
      - 1: Check network connectivity
      - 2: Verify repository permission, Ensure correct repository URL is used


4. **Install Required Packages**:
   - Navigate to the cloned project directory:

     ::
        
        cd Employee_Management

   - Install the required Python packages listed in the `requirements.txt` file:

     ::
        
        pip install -r requirements.txt


   - **ERROR:**
      - 1: Dependency Conflict
      - 2: Package installation Failure

   - **ERROR HANDLING:**
      - 1: Use virtual environment to isolate the dependencies.
      - 2: Updating 'pip' and 'setuptools' to the latest version 


5. **Run the Local Development Server**:
   - Start the local development server by running the following command:

     ::
        
        python manage.py runserver

   - **ERROR:**
      - 1: Port conflict
      - 2: Django Configuration Issue

   - **ERROR HANDLING:**
      - 1: Specify exact port number mentioned on the shell
      - 2: Review Django settings for any misconfigurations 


6. **Access the Application**:
   - Open a web browser and enter the following URL:

     ::
        
        http://127.0.0.1:8000/
