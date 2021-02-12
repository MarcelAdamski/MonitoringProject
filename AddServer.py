import pickle
from CheckServer import Server
import time

def AddServer(servers):
    while True:
        print("Started adding new server to monitorize")
        name = input("Server name: ")
        port = input("Port: ")
        connection_type = input("Connection type [plain/ssl/ping]: ")
        priority = input("Priority [high/low]: ")
        add = input("Proceed to add? [y/n]: ")
        if add.lower() == "y":
            try:
                server = Server(name, port, connection_type, priority)
                servers.append(server)
                pickle.dump(servers, open("servers.pickle", "wb"))
                print("Added successfully!")
                time.sleep(1)
            except Exception as e:
                print("Something went wrong.",e)
        another = input("Add another? [y/n]: ")
        if another.lower() == "y":
            continue
        else:
            print("Finished adding servers.")
            break
if __name__ == "__main__":
    try:
        servers = list(pickle.load(open("servers.pickle", "rb")))
        AddServer(servers)
    except FileNotFoundError:
        print("Pickle file not found. Created one.")
        servers = []
        AddServer(servers)
    except Exception as e:
        print(e)