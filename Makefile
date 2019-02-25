VENV=venv

install:
	$(VENV)/bin/pip3 install .

venv:
	python3 -m venv $(VENV)

clean:
	rm -rf $(VENV)