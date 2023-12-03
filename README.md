# inventory
# Example installation steps
git clone https://github.com/bash02/inventory.git
cd inventory
pipenv install
create new db "inventory"
type out your mysql password in setting module in root of the ptoject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
