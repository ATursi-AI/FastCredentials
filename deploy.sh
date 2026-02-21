#!/bin/bash

# 1. Activate environment
source venv/bin/activate

# 2. Pull latest changes (if using Git)
# git pull origin main

# 3. Install/Update requirements
pip install -r requirements.txt

# 4. Run Migrations
python3 manage.py migrate

# 5. Collect Static Files (CSS/Images)
python3 manage.py collectstatic --noinput

# 6. Restart Services (Adjust based on your server setup, e.g., Gunicorn/Nginx)
# sudo systemctl restart gunicorn
# sudo systemctl restart nginx

echo "Deployment Successful!"
