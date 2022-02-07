echo 'Activating Python Environment'
source venv/bin/activate
echo 'Pulling from GitHub'
git pull
python manage.py collectstatic
echo 'Restarting NGINX'
sudo systemctl restart nginx
echo 'Reloading NGINX'
sudo systemctl reload nginx