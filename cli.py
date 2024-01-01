import argparse
from network_security import scan_network

def cli():
    parser = argparse.ArgumentParser(description="Network Security Assistant CLI")
    parser.add_argument("--scan-network", help="Scan the network for active machines")
    args = parser.parse_args()

    if args.scan_network:
        active_machines = scan_network(args.scan_network)
        if active_machines:
            print("Active machines on the network:")
            for machine in active_machines:
                print(machine)
        else:
            print("No active machines found on the network.")

if __name__ == "__main__":
    cli()
