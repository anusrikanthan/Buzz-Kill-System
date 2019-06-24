# Buzz-Kill-System
A novel driver alterness detection system.

# Hardware Used :
  Intel UP squared development board
  Neurosky Mindwave mobile 2 (Brain Computing Interface)
  Logitech Web Cam
  
# Procedure for connecting Neurosky (Windows 8 and above):
    1. Download thinkgear connector from this site http://developer.neurosky.com/docs/doku.php?id=thinkgear_connector_tgc
    2. Use AAA batteries to power on the Neuro Sky.
    3. Install necessary drivers from the thinkgear website. 
    4. Switch on bluetooth in your machine and pair the device .
    5. Figure out the port the device is connected to using device manager.
    6. Create a twilio account from https://www.twilio.com/login?      g=%2Fconsole%3F&t=2b1c98334b25c1a785ef15b6556396290e3c704a9b57fc40687cbccd79c46a8c
    7. Update twilio account details in script "our_test.py" and update port also.
    8. Then run script "our_test.py" from the repository.
    
# Procedure for running EAR code:
The libraries required for running the python code can be installed using the following commands in linux

sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

pip install numpy
pip install scipy
pip install scikit-image
pip install dlib

After installing all the necessary packages, download the contents of the folder from the link and enter the following command from that directory to run the python code.
https://drive.google.com/drive/folders/1ZNAGtaiK2uS3Zrf_vIHX4DnETJNSYl9o

python alert_driver.py --shape-predictor shape_predictor_68_face_landmarks.dat

A working demo of the code is shown in https://drive.google.com/file/d/1Q2lg-M9moV7kJNqH3UfVZFPPfUTl4DTF/view?usp=sharing
