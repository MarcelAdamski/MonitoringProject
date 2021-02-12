import socket #allows to connect to diffrent servers on certain socket or port
import ssl #to wrap connection in ssl (if server requires it)
from datetime import datetime #track time of server downtime
import pickle #allows to propagate data from run to run with program

import subprocess
import platform #whether running on win/unix system

class Server():
    def __init__(self, name, port, connection_type, priority):
        self.name = name
        self.port = port
        self.connection_type = connection_type.lower()
        self.priority = priority.lower()

        self.history = []
        self.alert = False
    def check_connection(self):
        msg = ""
        success = False
        now = datetime.now()
        try:
            if self.connection_type == "plain":
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                success = True
                self.alert = False
            elif self.connection_type == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                success = True
                self.alert = False
            else: #if not plain or ssl connection it will be treated as a plain ping of the server
                if self.ping():
                    msg = f"{self.name} is up on port {self.port} with {self.connection_type} connection."
                    success = True
                    self.alert = False
        except socket.timeout:
            msg = f"server: {self.name} timeout on port {self.port} with {self.connection_type} connection."
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} Error: {e} "
        except Exception as e:
            msg = f"Other error: {e}"
        self.create_history(msg, success, now)
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
                return False
            else:
                return True
        except Exception:
            return False
if __name__ == "__main__":
    print('Started checking servers...')
    try:
        servers = pickle.load(open("servers.pickle", "rb"))
    except:
        servers = [
            Server("reddit.com", 80, "plain", "high"),
            Server("msn.com", 80, "plain", "high"),
            Server("smtp.gmail.com", 465, "ssl", "high"),
            Server("192.168.8.154", 80, "ping", "high")
        ]
    for server in servers:
        server.check_connection()
        for log in server.history:
            print('{} Connected? - {}. Date: {}'.format(log[0],log[1],log[2]))
            #print(log)
        #print(server.history[-1]) #priting last append to the history
    pickle.dump(servers, open("servers.pickle", "wb"))