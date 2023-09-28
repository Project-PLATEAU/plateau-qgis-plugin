PACKAGE_NAME = plateau_plugin

# Use this tag for packaging
VERSION = HEAD

# Windows (OSGeo4W)
ifeq ($(OS),Windows_NT)
QGIS_PYTHON = C:\OSGeo4W\bin\python-qgis-ltr.bat
QGIS_USER = $(APPDATA)\QGIS\QGIS3\profiles\default
QGIS_DLL = C:\OSGeo4W\bin
export QGIS_PREFIX_PATH = C:\OSGeo4W\apps\qgis-ltr
else
# macOS
ifeq ($(shell uname),Darwin)
QGIS_PYTHON = /Applications/QGIS.app/Contents/MacOS/bin/python3
QGIS_USER = ~/Library/Application\ Support/QGIS/QGIS3/profiles/default
QGIS_STD_PLUGINS = /Applications/QGIS.app/Contents/Resources/python/plugins
export QGIS_PREFIX_PATH = /Applications/QGIS.app/Contents/MacOS
export DYLD_LIBRARY_PATH = /Applications/QGIS.app/Contents/MacOS/lib
export PROJ_LIB = /Applications/QGIS.app/Contents/Resources/proj
else
# TODO: Linux
endif
endif


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

init:  ## Startup project
ifeq ($(OS),Windows_NT)
	$(QGIS_PYTHON) -m pip install poetry
	$(QGIS_PYTHON) -m poetry config --local virtualenvs.in-project true
	$(QGIS_PYTHON) -m poetry install
	$(QGIS_PYTHON) -c "import pathlib;import qgis;open('.venv/Lib/site-packages/qgis.pth', 'w').write(str((pathlib.Path(qgis.__file__)/'../..').resolve()) + '\n' + str((pathlib.Path(qgis.__file__)/'../../plugins').resolve()))"
else
	poetry env use $(QGIS_PYTHON)
	poetry install
	echo $(QGIS_STD_PLUGINS) > .venv/lib/python3.9/site-packages/qgis_std_plugins.pth
endif

deploy:  ## Deploy to QGIS
ifeq ($(OS),Windows_NT)
	robocopy /mir ${PACKAGE_NAME} $(QGIS_USER)/python/plugins/${PACKAGE_NAME}
else
	rsync -av --delete ${PACKAGE_NAME} $(QGIS_USER)/python/plugins/
endif

package:  ## Build zip package
	mkdir -p dist
	git archive -o dist/artifact-${VERSION}.zip ${VERSION} ${PACKAGE_NAME}

test:  ## Test
ifeq ($(OS),Windows_NT)
	$(QGIS_PYTHON) -m poetry run python -c "import os; os.add_dll_directory(r'${QGIS_DLL}'); import pytest; pytest.main('-v --cov --cov-report=term'.split())"
else
	poetry run pytest -v --cov --cov-report=term
endif

update_dependencies:  ## Update PLATEAU library
	pip download plateau-py --no-dependencies
	wheel3 unpack plateau_py-*-py3-none-any.whl
	rsync -r --delete plateau_py-*/plateau ${PACKAGE_NAME}/
	cp plateau_py-*/plateau_py-*.dist-info/LICENSE.txt ${PACKAGE_NAME}/plateau/
	rm -rf plateau_py-*/
	rm -rf plateau_py-*.whl
