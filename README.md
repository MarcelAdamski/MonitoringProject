# MonitoringProject
Simple project that monitorize servers or computers with statistics of their uptime. Made for educational purposes only.

## How it works?
Project MonitoringProject monitorize whether server is on or off. Script requires server name, port, connection type(ssl, plain or simple ping) and priority. Script is saving last 100 history logs to pickle file. Script provides gmail alerts when server is down or not responding.

## CheckServer
Main script for project. Allows you to set up starting servers, ports, type of connection and priority. If you wan't to create your own, delete *servers.pickle* and re-run *CheckServer.py*. Variable timeout describe time intervals which will check whether server is running or not.

## AlertGmail
This file describes how sending alerts via gmail are made. Change *adress* and *password* variable to your gmail account from where you want to send alers and *mailTo* variable describes to who you want send alerts. Remember to work properly, you have to change *send_email* variable in class *Server* inside *CheckServer.py* to *True*.

## Stats
Run to see basic statistics of checked servers. 

## DeleteServer & AddServer 
Run each to add another server to pickle file or delete one.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
