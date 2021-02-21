import socket #allows to connect to diffrent servers on certain socket or port
import ssl #wrapping connection in ssl
from datetime import datetime #track time of server downtime
import pickle
import subprocess
import platform
from AlertGmail import email_alert
import time

class Server():
    def __init__(self, name, port, connection_type, priority):
        self.name = name
        self.port = port
        self.connection_type = connection_type.lower()
        self.priority = priority.lower()
        self.send_email = True
        self.msg = ""

        self.history = []
        self.alert = False
    def check_connection(self):
        self.msg = ""
        success = False
        now = datetime.now()
        try:
            if self.connection_type == "plain":
                socket.create_connection((self.name, self.port), timeout=5)
                self.msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                success = True
                self.alert = False
            elif self.connection_type == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=5))
                self.msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                success = True
                self.alert = False
            else: #if not plain or ssl connection it will be treated as a plain ping of the server
                if self.ping():
                    self.msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                    success = True
                    self.alert = False
        except socket.timeout:
            self.msg = f"server: {self.name} timeout on port {self.port} with {self.connection_type} connection."
        except (ConnectionRefusedError, ConnectionResetError) as e:
            self.msg = f"server: {self.name} Error: {e} "
        except Exception as e:
            self.msg = f"{self.name} Other error: {e}"

        if success == False and self.alert == False and self.send_email == True:
            #sending alert via e-mail
            self.alert = True
            time = str(now)
            time = time.split('.')[0]
            email_alert(f"{self.msg}\nWhen: {time}")
        self.create_history(self.msg, success, now)
    def create_history(self, msg, success, now):
        history_max = 100
        self.history.append((msg, success, now))
        while len(self.history) > history_max:
            self.history.pop(0)
        #print('Created history!')
    def ping(self): #function that ping server
        try:
            output = subprocess.check_output("ping -{} {} {}".format('n' if platform.system().lower() == "windows" else "c", 2, self.name), shell = True, universal_newlines=True)
            #print("Output printed\n",output)
            if 'unreachable' in output:
                tmp = str(output.split(": ")[1].split("\n")[0])
                self.msg = f"{self.name} - {tmp}"
                return False
            else:
                return True
        except Exception as e:
            self.msg = f"{self.name} has other error: {e}"
            return False
if __name__ == "__main__":
    print('Started checking servers...')
    timeout = 10
    try:
        servers = pickle.load(open("servers.pickle", "rb"))
    except:
        servers = [
            Server("wp.pl", 80, "plain", "high"),
            Server("onet.pl", 80, "plain", "high"),
            Server("smtp.gmail.com", 465, "ssl", "high"),
            Server("reddit.com", 443, "ssl", "high"),
            Server("facebook.com", 443, "ssl", "high"),
            Server("192.168.8.1", 80, "ping", "high")
        ]
    while True:
        for i, server in enumerate(servers):
            server.check_connection()
            last_log = server.history[-1]
            time_fix = str(last_log[2])
            print('{}.{} Connected? - {}. When: {}'.format(i+1, last_log[0], last_log[1], time_fix.split(".")[0]))
        pickle.dump(servers, open("servers.pickle", "wb"))
        print(f"\nServers will be checked again in {timeout} seconds. Abort to stop script.")
        time.sleep(timeout)