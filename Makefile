all: dist

dist:
	python setup.py sdist

install:
	pip install --upgrade .

clean:
	rm -vrf \
		zabbix_template_converter.egg-info \
		build \
		dist

upload:
	python setup.py sdist upload

.PHONY: all dist install clean upload
