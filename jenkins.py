import os 
os.system("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add - ")
os.system("sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
os.system("sudo apt update")
os.system("sudo apt install jenkins")
os.system("sudo systemctl start jenkins")
print("Your Jenkins Setup is Ready Now ")
print(" ***** THANKU ***** ")
