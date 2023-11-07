# dynamic_report

Behold My Awesome Project!

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ DJANGO_SETTINGS_MODULE="config.settings.local" python manage.py createsuperuser
        for local run
      $ DJANGO_SETTINGS_MODULE="config.settings.production" python manage.py createsuperuser
        for production run

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Development setup project

The following details how to deploy this application.
sudo docker-compose development-docker-compose.yml up
