VENV = .venv
PYTHON = $(VENV)/bin/python

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

ex%: $(VENV)/bin/activate
	$(PYTHON) src/$@.py

fclean:
	rm -rf $(VENV)

.PHONY: fclean
