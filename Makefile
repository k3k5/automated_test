version:
	python3 --version && pip3 --version

install:
	python3 -m pip install -r requirements.txt

run:
	python3 -m unittest discover