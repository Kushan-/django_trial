linux_installer(){
	pip3 --version
	if [ $? -eq 127 ]; then
		echo "Installing pip"
		sudo easy_install pip
	elif
	virtualenv .
	if [ $? -eq 127]; then
		echo "Insalling virtualenv"
		sudo pip3 install virtualenv 
		sudo apt install python3-django
	elif
	virtual .
	echo "setting up virtualenv"
	echo "activating virtualenv"
	source bin/activate
	pip3 install django==2.1.5

	sudo apt install python-django-common
	which django
}

sudo apt install docker-compose
