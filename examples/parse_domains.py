from pddl import parse_domain, parse_problem
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Parse domains')
parser.add_argument('--domain','-d', type=str, help='Domain file')
parser.add_argument('--all', '-a', action='store_true', help='Parse all domains')
parser.add_argument('--show_error', '-e', action='store_true', help='Show errors', default=False)
args = parser.parse_args()

if args.all:
    directory = Path("./domains")
    folders = [f.name for f in directory.iterdir() if f.is_dir()]
elif args.domain: 
    folders = [args.domain]

for domain_name in folders:
    try:
        domain = parse_domain(f'./domains/{domain_name}/domain.pddl')
    except Exception as e:
        print(f"Error parsing domain {domain_name}")
        if args.show_error:
            print(e)
