python3.9 -m venv venv
source venv/Scripts/activate.ps1/
pip install -r requirements.txt
python manage.py collectstatic --noinput

