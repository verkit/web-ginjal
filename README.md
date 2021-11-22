## WEB SKRIPSI
___
Website skripsi klasifikasi penyakit ginjal

Build with python (Flask) - 
[sumber referensi](https://code.visualstudio.com/docs/python/tutorial-flask)

### Prasyarat instalasi
- Install [ekstensi python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Install python3

### Membuat environment
```
py -3 -m venv .venv
.venv\scripts\activate
```

Pastikan status bar di pojok kiri bawah vscode menjadi seperti ini 
![status-bar](https://code.visualstudio.com/assets/docs/python/shared/environment-in-status-bar.png)

Apabila belum silahkan cek [tutorial](https://code.visualstudio.com/docs/python/tutorial-flask#_create-a-project-environment-for-the-flask-tutorial) ini

Setelah status bar sesuai jalankan
```
python -m pip install --upgrade pip
python -m pip install flask
```

Kemudian jalan kan webnya
```
python -m flask run
```