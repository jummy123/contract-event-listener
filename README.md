# Example contract event listener

A sample contract and brownie script to listen for events
emitted by a contract.

The two parts to this repo are the [example contract](https://github.com/jummy123/contract-event-listener/blob/master/contracts/Example.sol) which contains a single function which emits an event and the [pyton listener script](https://github.com/jummy123/contract-event-listener/blob/master/scripts/listener.py) which deploys the contracts and simulates some transactions being sent to it, it also includes a simple listener for printing the events it listens to.

## Setup

Intall the python dependencies with pip `pip install -r requirements.txt` (it is recommended to use a [virtual environment](https://docs.python.org/3/library/venv.html) for this).

For my testing I also used the hardhat network which can be install with [npm](https://www.npmjs.com/) `npm install hardhat`.

## Running

To run the script and see the messages printed to the console use

`brownie run scripts/listener.py --network hardhat`.

## Questions

You can ask me questions in the [Avax build guild #dev channel](https://discord.gg/CNK5g9Kc), my handle is _jumbo_.
