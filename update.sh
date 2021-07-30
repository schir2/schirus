source venv/bin/activate
git pull
python manage.py collectstatic
sudo systemctl restart nginx
sudo systemctl reload nginx