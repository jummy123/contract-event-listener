import time
import random

from brownie import *


def deploy_example_contract():
    """
    Deploy the example contract from this project.
    """
    example_contract = Example.deploy({'from': accounts[0]})
    return example_contract


def get_message_filter(example_contract):
    """
    Create the web 3 contract return the event filter.
    """

    web3_contract = web3.eth.contract(
        abi=example_contract.abi,
        address=example_contract.address)

    message_filter = web3_contract.events.Message.createFilter(
        fromBlock='latest')

    return message_filter


def event_printer(example_contract, message_filter):
    """
    A simple example where we print messages to STDOUT.

    This example is synchronous and blocking, for a production
    script you would want to offloan the polling for new
    entries to a thread or process.
    """

    while True:

        # Random amount of transactions to send.
        for i in range(1, random.randint(1, 5)):

            # Send a tx to our contract from random account
            # and with a random value.
            example_contract.message(
                f'Sending a message {i}',
                {
                    'from': accounts[random.randint(1, 9)],
                    'value': random.randint(1, 1000000),
                })

        # Print all the new events emitted.
        for message in message_filter.get_new_entries():
            print(message)

        # Sleep for a bit of time.
        time.sleep(5)


def main():
    """
    The main function that wraps the above 3 functions.
    """
    example_contract = deploy_example_contract()
    message_filter = get_message_filter(example_contract)
    event_printer(example_contract, message_filter)


if __name__ == "__main__":
    main()
