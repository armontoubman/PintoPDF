## Synopsis

PintoPDF is a GUI tool for 1) extracting pages from PDF files and 2) merging PDF files.

## Motivation

I needed this, and I wanted to use Python 3 and tkinter.

## Installation

Requires Python 3.
Install dependencies (PyPDF2): `pip install -r requirements.txt`.
The tkinter (8.6) library may or may not already come with your Python 3 distribution.

Clone the repository, and use `python3 pintopdf.py` to start.

### Building executables

#### Using py2exe/py2app:

On Windows, use `python setup.py py2exe` to build an executable.

On OS X, use `python setup.py py2app` to build an app bundle.

#### Using PyInstaller: 

`pyinstaller --onefile --windowed pintopdf.py`

## Screenshots

Windows 7

![PintoPDF on Windows 7 (1)](https://www.armontoubman.com/files/pintopdf/pintopdf_windows7_1.png)

![PintoPDF on Windows 7 (2)](https://www.armontoubman.com/files/pintopdf/pintopdf_windows7_2.png)

Ubuntu 16.04

![PintoPDF on Ubuntu 16.04 (1)](https://www.armontoubman.com/files/pintopdf/pintopdf_ubuntu_1.png)

![PintoPDF on Ubuntu 16.04 (2)](https://www.armontoubman.com/files/pintopdf/pintopdf_ubuntu_2.png)

OS X

![PintoPDF on macOS (1)](https://www.armontoubman.com/files/pintopdf/pintopdf_osx_1.png)

![PintoPDF on macOS (2)](https://www.armontoubman.com/files/pintopdf/pintopdf_osx_2.png)

## License

PintoPDF is licensed under the GPLv3:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

