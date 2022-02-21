# Title

## Installation

You will need to install dependencies

```shell
pip install -r requirements.txt
```

### PyQT ui generation

```shell
# Example
pyuic5 ./reports_app/ui/designer_files/main_window.ui > ./reports_app/ui/main_window_ui.py
```

## Run

```shell
python main.py
```


## Test

```shell
pytest
#OR
python -m unittest discover

# Coverage:
coverage run -m pytest
# OR
coverage run -m unittest discover

# Coverage report
coverage report
```