import pickle
import os

def show_servers(servers):
    for i, server in enumerate(servers):
        print("{}: {} port: {} connection: {} priority: {}".format(i, server.name, server.port, server.connection_type, server.priority))

def update_servers(servers):
    if len(servers) == 0:
        os.remove("servers.pickle")
    else:
        pickle.dump(servers, open("servers.pickle", "wb"))
    print("Deleting process finished.")

def delete_server(servers):
    try:
        show_servers(servers)
        while True:
            index = input("Enter index of server you would like to delete [0-{}]: ".format(len(servers) - 1))
            del servers[int(index)]
            if len(servers) == 0:
                print("No servers left in pickle file.")
                update_servers(servers)
                break
            print("\nNew server list:")
            show_servers(servers)
            decision = input("Delete more? [y/n]: ")
            if decision == "y":
                continue
            else:
                update_servers(servers)
                break
    except IndexError:
        print("Wrong index. Try again")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    try:
        servers = list(pickle.load(open("servers.pickle", "rb")))
        delete_server(servers)
    except FileNotFoundError:
        print("Pickle file not found. First create pickle file where you will store list of servers.")
    except Exception as e:
        print(e)