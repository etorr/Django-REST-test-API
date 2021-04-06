# Django REST Framework with Unit TEST

<h2>Installation</h2>
<b>unzip contents of package</b>
<pre>
</pre>
<b>open terminal and move into folder that was extracted</b>
<pre>
cd {yourpath}/djangorest/
</pre>
<b>create a virtualenv named env</b>
<pre>
python3 -m venv env
</pre>
<b>activate env</b>
<pre>
source env/bin/activate
</pre>
<b>Verify that virtualenv is working. (at the beginning of the command request (env))</b>
<pre>
(env) ~$ pip install --upgrade pip
</pre>
<b>then install requirements.txt</b>
<pre>
(env) ~$ pip3 install -r requirements.txt
</pre>
<h2>Usage</h2>
<b>Create the Database</b>

<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h2>Unit Tests</h2>
<b>Run automated tests</b>
<pre>
python manage.py test
</pre>
<b>To test with Postman</b>
<pre>
python manage.py createsuperuser
python manage.py runserver
</pre>
<b>use login details of created user to obtain JWT token pair in Postman</b>