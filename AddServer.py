import pickle
from CheckServer import Server

servers = pickle.load(open("servers.pickle", "rb"))

while True:
    print("Started adding new server to monitorize")
    name = input("Server name: ")
    port = input("Port: ")
    connection_type = input("Connection type [plain/ssl/ping]: ")
    priority = input("Priority [high/low]: ")
    decision = input("Are you sure you want to add? [y/n]: ")
    if decision.lower() == "y":
        try:
            server = Server(name, port, connection_type, priority)
            servers.append(server)
            pickle.dump(servers, open("servers.pickle", "wb"))
            print("Added successfully!")
        except Exception as e:
            print("Something went wrong.",e)
        break
    else:
        break

