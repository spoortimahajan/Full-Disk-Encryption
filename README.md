# Full-Disk-Encryption
# Introduction
Full Disk Encryption (FDE) is a security technique that encrypts all data stored on a disk drive to prevent unauthorized access. It ensures that even if a device is lost or stolen, the data remains protected. Popular tools like BitLocker and VeraCrypt implement FDE at the system level.
In this project, we simulate FDE using:
- A login-based disk unlock system
- A simple encryption & decryption algorithm (Caesar Cipher)
- A web interface similar to BitLocker

# Objective
- To protect sensitive data from unauthorized access
- To simulate disk encryption and authentication
- To understand how encryption works in real systems
- To demonstrate secure login before accessing system

# Key Features
- Password-based authentication
- Data encryption & decryption simulation
- Limited login attempts (security feature)
- Pre-boot authentication simulation
- Web-based UI(Bitlocker like screen)
- User-friendly interface

# Technologies Used
- Python → Core logic (encryption, authentication)
- Flask → Backend server
- HTML → Structure of web page
- CSS → Styling (BitLocker UI simulation)
- JavaScript → Handling user interaction & API calls

#  Project Structure
- static/ --CSS files
- templates/--HTML files
- app.py--main python(Flask)file
- Screenshots/--images
- README.md--project description
  
# Installation and Setup
- Step 1: Install Python
  Download and install Python 
- Step 2: Install Flask
  pip install flask
- Step 3: Project Setup
  Place files in correct folders (templates, static)
  Save Flask code as app.py
- Step 4: Run the Application
  python app.py
- Step 5: Open Browser
  Go to: http://127.0.0.1:5000/

# Working Procedure
- Users enters password in web page
- Java script sends it to flask backend
- Flask verifies the password
- Result is shown on screen
- If correct--system unlocks
- If wrong--error message shown
  
# sample log output
- The system displays a login screen and shows success or error message based on password verification

# Applications
- Data protection in laptops and computers 
- Prevent unauthorized disk access
- Educational purpose for encryption concepts
- Simulation of real tools like BitLocker

# Limitations
- Uses simple Caesar Cipher (not strong security)
- Password is hardcoded
- No real disk encryption (only simulation)
- No database for storing users
- Limited error handling

# Future Enhancement
- Implement strong encryption (AES)
- Add database for password storage
- Multi-user authentication system
- Real file/disk encryption integration
- GUI desktop application
- Biometric authentication

# Author
- Sonal Bhangle
- Spoorti Mahajan








