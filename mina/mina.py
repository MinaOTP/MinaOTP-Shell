#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : since 2018-02-06 02:26
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : add remove show and list totp tokens in the terminal

import json
import logging
import argparse

# configure the basic logging level
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)
# load tokens from json file
def load_json(json_url):
    with open(json_url, 'r') as f:
        return json.load(f)

# list all tokens
def list():
    logging.info("List all tokens")

# the main function to control the script
def main():
    # Load the json file
    _json_url = './.mina.json'
    tokens = load_json(_json_url)
    print(tokens)
    # Define the basic_parser and subparsers
    logging.info('Initial basic_parser')

    _desc = 'MinaOTP is a two-factor authentication tool that runs in the terminal'
    basic_parser = argparse.ArgumentParser(description=_desc)
    subparsers = basic_parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # Subparser for the list command
    logging.debug("Initial list subparser")

    list_parser = subparsers.add_parser(
        "list",
        help="List all tokens."
    )

    # Subparser for the add command
    logging.debug("Initial add subparser")

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new token."
    )

    # Subparser for the remove command
    logging.debug("Initial remove subparser")

    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove a token."
    )

    # Subparser for the show command
    logging.debug("Initial show subparser")

    show_parser = subparsers.add_parser(
        "show",
        help="Show a token on-time"
    )
    show_parser.add_argument(
        "token",
        help="issuer of the token"
    )

    # handle the args input by user
    args = basic_parser.parse_args()
    # convert arguments to dict
    arguments = vars(args)
    command = arguments.pop("command")

    if command == "list":
        list()
    if command == "add":
        print("add a new token")
    if command == "remove":
        print("remove a token")
    if command == "show":
        print("show a token on-time")


if __name__ == '__main__':
    main()