import pickle
from CheckServer import Server
import os

def ShowServers(servers):
    for i, server in enumerate(servers):
        print("{}: {} port: {} connection: {} priority: {}".format(i, server.name, server.port, server.connection_type, server.priority))

def UpdateServers(servers):
    if len(servers) == 0:
        os.remove("servers.pickle")
    else:
        pickle.dump(servers, open("servers.pickle", "wb"))
    print("Deleting process finished.")

def DeleteServer(servers):
    try:
        ShowServers(servers)
        while True:
            index = input("Enter index of server you would like to delete [0-{}]: ".format(len(servers) - 1))
            del servers[int(index)]
            if len(servers) == 0:
                print("No servers left in pickle file.")
                UpdateServers(servers)
                break
            print("\nNew server list:")
            ShowServers(servers)
            decision = input("Delete more? [y/n]: ")
            if decision == "y":
                continue
            else:
                UpdateServers(servers)
                break
    except IndexError:
        print("Wrong index. Try again")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    try:
        servers = list(pickle.load(open("servers.pickle", "rb")))
        DeleteServer(servers)
    except FileNotFoundError:
        print("Pickle file not found. First create pickle file where you will store list of servers.")
    except Exception as e:
        print(e)