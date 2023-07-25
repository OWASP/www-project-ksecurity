# www-project-ksecurity
OWASP Foundation Web Respository

## Ksecurity is a monitoring system developed in the Python programming language. 

### Ksecurity features the following functionalities:

- Monitor website availability.
- Monitor external and internal connections to the system.
- Monitor the performance of the selected server.
- Monitor the /etc/apache2 directory of the Apache server.
- Monitor the /etc/nginx directory of the Nginx server.

 #### Ksecurity also allows you to choose which server to monitor, giving you the flexibility to monitor either the Apache or Nginx server based on your preference. Please note that this system may have some false positives and is designed specifically for Linux operating systems.

### Here's a step-by-step guide to execute the Ksecurity project in root mode on Linux:

- Clone the repository: Open the terminal and navigate to the directory where you want to clone the repository.
- Navigate to the project folder:
- Access the Ksecurity folder
- Run the project in root mode

```py
 - git clone https://github.com/OWASP/www-project-ksecurity.git
 - cd www-project-ksecurity
 - cd Ksecurity
 - sudo python3 ksecurity.py
```

  ##### The Ksecurity project should start running, and you will see the output in the terminal as the program monitors the chosen server, checks website availability, and monitors external and internal connections.

Please note that executing any project in root mode requires caution as it grants privileged access to the system. Carefully review the project's code and understand its actions before running it in root mode. Ensure that the project is from a trusted source and that you understand its functionalities before running it in a production environment.

![owasp_ksecurity](
https://raw.githubusercontent.com/OWASP/www-project-ksecurity/main/assets/images/main.png)


![owasp_ksecurity](
https://raw.githubusercontent.com/OWASP/www-project-ksecurity/main/assets/images/end.png)

