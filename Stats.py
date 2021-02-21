import pickle
from CheckServer import Server
def show_stats(servers):
    print("###=======SERVER=======###====LOGS====###===UP FOR===###")
    for server in servers:
        up_times = 0
        all_times = len(server.history)
        for log in server.history:
            if log[1] is True:
                up_times+=1
        print("\t\t{:20s} {:4d} {:15.1f}%".format(server.name, all_times, (up_times*100)/all_times))
if __name__ == '__main__':
    try:
        servers = list(pickle.load(open("servers.pickle", "rb")))
        show_stats(servers)
    except FileNotFoundError:
        print("Pickle file not found. Stopping script")
    except Exception as e:
        print(e)