
# Packaging

The program can be packaged into a single file using `pyinstaller`, but it's not a one-command deal.  First you'll need
to generate the spec file using `pyi-makespec`:

## Linux version:

    pyi-makespec --onefile -n Optimine2Dat --add-data optimine2dat/export.ui:. optimine2dat/export.py

## Windows version:

If packaging with python 3.5+ on Windows 10 you will need to install the Windows 10 SDK from
https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk

See notes:
  PyInstaller issue: https://github.com/pyinstaller/pyinstaller/issues/1566
  StackOverflow: https://stackoverflow.com/questions/46416221/pyinstaller-distributing-opencv-from-windows-10-to-windows-10-missing-ucrt-dll

    pyi-makespec --onefile -n Optimine2Dat --add-binaries C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64;. \
         --add-data optimine2dat/export.ui;. optimine2dat/export.py


Then, you'll need to add the following after the 'Analasys()....' call to the generated .spec file:


```
def get_pandas_path():
    import pandas
    pandas_path = pandas.__path__[0]
    return pandas_path


dict_tree = Tree(get_pandas_path(), prefix='pandas', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'pandas' not in x[0], a.binaries)
```

NOW you can run `pyinstaller --one-file Optimine2Dat.spec`
