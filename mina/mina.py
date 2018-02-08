#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : since 2018-02-06 02:26
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : add remove show and list totp tokens in the terminal

import json
import logging
import argparse
import pyotp

# global variable
ISSUER_LEN = 16
REMARK_LEN = 16
OTP_LEN = 16

# configure the basic logging level
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

# load tokens from json file
def load_json(json_url):
    with open(json_url, "r") as f:
        return json.load(f)

# list all tokens
def list(tokens):
    print("SECRET".center(ISSUER_LEN, "="), "REMARK".center(REMARK_LEN, "="), "OTP".center(OTP_LEN, "="))
    for token in tokens:
        secret = token["secret"]
        issuer = token["issuer"]
        remark = token["remark"]
        # generate tmp TOTO object and calculate the token
        totp_tmp = pyotp.TOTP(secret)
        current_otp = totp_tmp.now()
        print(issuer.center(ISSUER_LEN), remark.center(REMARK_LEN), current_otp.center(OTP_LEN))

# the main function to control the script
def main():
    # Load the json file
    _json_url = './.mina.json'
    tokens = load_json(_json_url)

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
        list(tokens)
    if command == "add":
        print("add a new token")
    if command == "remove":
        print("remove a token")
    if command == "show":
        print("show a token on-time")


if __name__ == '__main__':
    main()