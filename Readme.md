# Money Planner App
Implementasi belum 100% selesai

## How to run app locally
Clone repo ini
```bash
git clone https://github.com/venedictchen/Money-Planner.git money-planner
```

CD ke dir app
```bash
cd ./money-planner
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

Buka html di browser
