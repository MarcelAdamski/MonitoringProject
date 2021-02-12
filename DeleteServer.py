import pickle
from CheckServer import Server

def ShowServers(servers):
    for i, server in enumerate(servers):
        print("{}: {} port: {} connection: {} priority: {}".format(i, server.name, server.port, server.connection_type, server.priority))
def DeleteServer(servers):
    try:
        index = input("Enter index of server you would like to delete 0-{}:?".format(len(servers) - 1))
        del servers[int(index)]
    except Exception as e:
        print(e)
try:
    servers = list(pickle.load(open("servers.pickle", "rb")))
    ShowServers(servers)
    while True:
        DeleteServer(servers)
        print("\nNew server list:")
        ShowServers(servers)
        decision = input("Delete more? [y/n]: ")
        if decision == "y":
            continue
        else:
            print("Deleting process finished.")
            pickle.dump(servers, open("servers.pickle", "wb"))
            break
except Exception as e:
    print(e)
    print("Server list is empty! Nothing to delete here.")
