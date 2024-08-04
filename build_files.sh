
echo "BUILD START"
Python3.10 -m pip install requirement.txt
Python3.10 manage.py collectstatic --noinput --clear

echo " BUILD START"