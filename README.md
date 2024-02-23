# PFE_2023-2024_Laverie_Habitat-Humanisme
Final project of my engineering school 
During this project I had to create a system for a private laundry where users can select a laundry machine and than pay for what the consume ( only the electrical cosumption is colected)

## Installation

1. **Install Python:**

   If you haven't already installed Python

*** Install on linux ***
   Update 
```sh
$ sudo apt update 
```
Install 
```sh
$ sudo apt install python3
```
*** Install on windows ***

Download the latest version of the Python executable installer for Windows x86-64 from the Python.org downloads page.

Run the Python installer executable file that you downloaded in the previous step. Select the following options in the Python installer window to configure the installation steps for the EB command-line interface that follow:

Choose to add Python executable to your path.

Choose Install Now.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_project.git
   ```

3. **Navigate into the project directory:**

   ```bash
   cd your_project
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

Now the project is ready to use! You can proceed with the usage instructions below.

# Usage
Run the development server:
```bash
   python manage.py runserver
   ```
The project will be accessible at http://127.0.0.1:8000/

