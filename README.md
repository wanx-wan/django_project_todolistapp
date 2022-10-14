# First Steps

    conda create -n webenv python=3.10
    conda install -c conda-forge django

# Create New Web Project

    django-admin startproject myweb .

# Create New Web Project

    python manage.py startapp myapp

# Activate to env

    conda activate webenv

# Migrate

    python manage.py makemigrations
    python manage.py migrate

# createsuperuser

    python manage.py createsuperuser
    user, password : admin




