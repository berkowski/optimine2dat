# Optimine JSON to DAT file converter

Provides a GUI and converter for translating Optimine JSON data files to older DAT format for use with
existing tooling to create Pressure Test Certificates.


# Packaging

The program can be packaged into a single file using `pyinstaller`.  Appveyor has been setup to do this
for you, but here's how to do it manually.

NOTE:  When packaging, use PyQt5 and PyQtChart version 5.9.2 (5.10 isn't supported well by pyinstaller)

## Environment

Create a new virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Then install the requried dependencies

    pip install -r packaging_requirements.txt


## Packaging

NOW you can run `pyinstaller --one-file .appveyor/optimine2dat_win7.spec`

## Windows 10 Notes:

If packaging with python 3.5+ on Windows 10 you will need to install the Windows 10 SDK from
https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk

See notes:
  - PyInstaller issue: https://github.com/pyinstaller/pyinstaller/issues/1566
  - StackOverflow: https://stackoverflow.com/questions/46416221/pyinstaller-distributing-opencv-from-windows-10-to-windows-10-missing-ucrt-dll


You'll need to add some extra flags:

    pyinstaller --add-binary "C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64;." \
         --path "C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64".appveyor/optimine2dat_win7.spec`

