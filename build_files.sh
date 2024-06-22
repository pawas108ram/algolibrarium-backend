python3.9 -m venv venv
source venv/bin/Activate.ps1
pip install -r requirements.txt
python manage.py collectstatic --noinput

