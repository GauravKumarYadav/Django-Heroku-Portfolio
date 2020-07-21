# Django-Heroku-Portfolio
<h2>Portfolio Website</h2>
<p> This repo contains a pdf converter , converting pdf to Image and PDF to Text and serving them as downloadable (.zip)files , along with a beautiful profile template  </p>

<h2>Installation<h2>
<p>
  <h3><strong>Activating conda Environment:</strong></h3>
  <ul>
    <li><i>conda create --name envName python=3.6</i></li>
    <li><i>conda activate envName</i></li>
  </ul>
  <h3><strong>Installing on local machine</strong></h3>
  <p> comment the line <i>import django_heroku</i> and <i>django_heroku.settings(locals())</i> in pdfconverter/settings.py file and remove <i>django_heroku package</i> from requirements.txt file</p>
  <ul>
    <li><i>pip install -r requirements.txt</i></li>
  </ul>
  <h3><strong>Deploying on Heroku server</strong></h3>
  <p><a href="https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html">Here</a> are simple steps to deploy it on Heroku </p>
</p>
<h2> Run </h2>
<ul>
<li><p> <i>python manage.py runserver</i>  on local machine</p></li>
<li><p> simply visite the website on browser </p></li>
</ul>
