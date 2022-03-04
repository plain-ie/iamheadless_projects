# iamheadless_projects

App to manage project/tenant/user hierarchy. This app is decoupled from Django native permission model. Users use their email as username.

## Installation

1. install package
2. add `iamheadless_projects` to `INSTALLED_APPS` in `settings.py`
3. add `AUTH_USER_MODEL = 'iamheadless_projects.User'` in `settings.py`
4. run migrations `python manage.py migrate`
