# PEAssignment
PharmEasy Interview Assignment

Python version: 3.6.1

Setup Instructions
1. Create environment variables
2. Run: pip install -r requirements.txt in project root
3. Migrate db: python manage.py migrate
4. Collectstatic files: python manage.py collectstatic
5. Create a superuser to access admin panel: python manage.py createsuperuser
6. Run server: python manage.py runserver <port>
7. Access admin and create some entries for each data model.

Note: Environment setting has been kept at DEV for easy discovery of bugs. However, will be turned off with APP_ENV set to PROD.

Shortcomings of the project due to time constraint:
1. Security of detail pages. Detail pages are accesible without necessary permissions if the url is known.
2. User, Prescription and medical records need to be currently created by the admin panel. This could've been implmeneted with the frontend which would have enabled necessary filtering. For e.g.: Anyone can create prescriptions currently. Only doctors should be able to in ideal case. However, the moto of the project was approvals flow. Hence, this was ignored.
3. Bad UI/UX. Very basic bootstrap is used to showcase the Approvals flow.
4. Project structure can be further divided to support multi-app structure and code readability.
5. Dockerization and init scripts for auto-deployment.
6. Unit test cases to create and test models and views.
7. Usage of django template for frontend. Website should ideally be divided and REST APIs should be used to communicate.
8. No throttling on view requests.
9. No caching.
10. Model level authorization for user permissions.

A test enviornment has been setup on an AWS EC2 micro instance. Here are the instructions:

User accounts created:
1. ernesto@barcelona.com - Superuser
2. iniesta@barcelona.com - Patient
3. nelson@barcelona.com - Patient
4. messi@barcelona.com - Doctor
5. suarez@barcelona.com - Pharmacist

Note: Email and Passwords for all the accounts are kept identical for ease.

For e.g. to login as Patient - Iniesta:
Email: iniesta@barcelona.com
Password: iniesta@barcelona.com

A couple of prescriptions and medical records are created with different statuses for illustration purpose. Please feel free to create more users and prescriptions through the admin panel for further testing.

URLS:
Frontend --> http://35.154.236.204
Admin --> http://35.154.236.204/admin/

Please use the frontend to logout/login with each of the account types to check the approval flow!