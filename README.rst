
# Packaging

The program can be packaged into a single file using `pyinstaller`, but it's not a one-command deal.  First you'll need
to generate the spec file using `pyi-makespec`:

# Linux version:

    pyi-makespec --onefile -n Optimine2Dat --add-data optimine2dat/export.ui:./optimine2dat optimine2dat/export.py

# Windows version:

    pyi-makespec --onefile -n Optimine2Dat --add-data optimine2dat/export.ui;.\optimine2dat optimine2dat/export.py



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
