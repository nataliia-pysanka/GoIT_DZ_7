# Clean_folder

This is a package to make your folder clear and structured. 
You just need to install this package with command:
```
https://test.pypi.org/project/clean-folder-superb/0.0.1/
```
or from folder with setup.py file:
```
python setup.py install
```

And then run it with one argument:
```
clean_folder <source>
```

All files from source folder will be sorted by their extensions to the next folders created inside source folder:
- images ('JPEG', 'PNG', 'JPG', 'SVG');
- video ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- audio ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');
- other

All filenames will be normalized: cyrillic symbols are transliterated and symbols except latin alphabet and  numbers are change by symbol '_'.
