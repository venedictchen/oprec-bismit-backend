# To Do List App
## How to run app locally
Clone repo ini
```bash
git clone https://github.com/venedictchen/oprec-bismit-backend.git
```

CD ke dir app
```bash
cd /oprec-bismit-backend
```

Buat virtual enviroment
```
python -m venv env
```

Start virtual enviroment
```
./env/Script/activate
```

Install dependency python
```bash
pip install -r ./requirements.txt
```

Start backend
```bash
python main.py
uvicorn main:app --reload
```
Replace the database url at database.py with your own url database connection


