# hdl300 - Modbus Readout for HDL300

This repository contains Python 3 application that reads HDL300 Pressure Transmitter over RS-485/Modbus RTU.


## Requirements

* Python 3


## Download

> It is recommended to use `pyenv` + `venv` (`venv` is part of the standard Python distribution) to manage your Python environment.

Clone this repository:

    $ git clone https://github.com/hardwario/hdl300.git

Switch to the Git repository:

    $ cd hdl300

Make sure the Python version matches the `.python-version` file:

    $ pyenv local

Create (just once) the virtual environment:

    $ python -m venv .venv

Activate the virtual environment:

    $ source .venv/bin/activate

Install all required dependencies:

    $ pip install -r requirements.txt


## Usage

The tool can be run using this command:

    $ python app.py --device <DEVICE>


## Authors

* [**Pavel Hübner**](https://github.com/hubpav) - Initial work


## License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT/) - see the [**LICENSE**](https://github.com/hardwario/hdl300/blob/master/LICENSE) file for details.
