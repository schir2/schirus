source venv/bin/activate
git pull
python manage.py collectstatic
sudo systemctl reload nginx