import argparse
import json

from .agent import run
from .contracts import Session


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline, synthetic agent work sample")
    parser.add_argument("--mode", choices=["starter", "reference"], default="starter")
    parser.add_argument("--message", required=True)
    parser.add_argument("--signed-in", action="store_true", help="Simulate a trusted demo session; this is not real authentication")
    args = parser.parse_args()
    session = Session("demo-customer") if args.signed_in else Session()
    print(json.dumps(run(args.message, session, mode=args.mode).to_dict(), indent=2))


if __name__ == "__main__":
    main()
