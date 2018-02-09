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
import os
import os.path

# global variable
OID_LEN = 6
ISSUER_LEN = 16
REMARK_LEN = 16
OTP_LEN = 16
JSON_URL = os.path.expanduser("~") + os.sep + '.mina.json'

# configure the basic logging level
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)

# load tokens from json file
def load_json(json_url):
    with open(json_url, "r") as f:
        return json.load(f)

# update token to json file
def upd_json(data, json_url):
    with open(json_url, "w") as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ':'))

# list all tokens
def list(tokens):
    print("OID".center(OID_LEN, "="), "ISSUER".center(ISSUER_LEN, "="), "REMARK".center(REMARK_LEN, "="), "OTP".center(OTP_LEN, "="))
    for oid, token in enumerate(tokens):
        # generate tmp TOTO object and calculate the token
        secret = token["secret"]
        remark = token["remark"]
        issuer = token["issuer"]
        totp_tmp = pyotp.TOTP(secret)
        current_otp = totp_tmp.now()
        print(str(oid).center(OID_LEN), issuer.center(ISSUER_LEN), remark.center(REMARK_LEN), current_otp.center(OTP_LEN))

# show a token on-time
def show(oid, tokens):
    print("OID".center(OID_LEN, "="), "ISSUER".center(ISSUER_LEN, "="), "REMARK".center(REMARK_LEN, "="), "OTP".center(OTP_LEN, "="))
    token = tokens[int(oid)]
    issuer = token["issuer"]
    secret = token["secret"]
    remark = token["remark"]
    # generate tmp TOTO object and calculate the token
    totp_tmp = pyotp.TOTP(secret)
    current_otp = totp_tmp.now()
    print(oid.center(OID_LEN), issuer.center(ISSUER_LEN), remark.center(REMARK_LEN), current_otp.center(OTP_LEN))

# add a new token
def add(otp, tokens):
    tokens.append(otp)
    upd_json(tokens, JSON_URL)

# remove a token
def remove(oid, tokens):
    tokens.pop(int(oid))
    upd_json(tokens, JSON_URL)

# the main function to control the script
def main():
    # Load the json file
    tokens = load_json(JSON_URL)

    # Define the basic_parser and subparsers
    logging.debug('Initial basic_parser')

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
    # OTP optional arguments
    add_parser.add_argument(
        "--secret",
        required=True,
        help="Secret info to generate otp object."
    )
    add_parser.add_argument(
        "--issuer",
        required=True,
        help="Issuer info about new otp object."
    )
    add_parser.add_argument(
        "--remark",
        required=True,
        help="Remark info about new otp object."
    )

    # Subparser for the remove command
    logging.debug("Initial remove subparser")

    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove a token."
    )
    remove_parser.add_argument(
        "oid",
        help="oid of the token"
    )

    # Subparser for the show command
    logging.debug("Initial show subparser")

    show_parser = subparsers.add_parser(
        "show",
        help="Show a token on-time"
    )
    show_parser.add_argument(
        "oid",
        help="oid of the token"
    )

    # handle the args input by user
    args = basic_parser.parse_args()
    # convert arguments to dict
    arguments = vars(args)
    command = arguments.pop("command")

    if command == "list":
        list(tokens)
    if command == "add":
        otp = {
            "secret": args.secret,
            "issuer": args.issuer,
            "remark": args.remark
        }
        add(otp, tokens)
    if command == "remove":
        target_oid = args.oid
        remove(target_oid, tokens)
    if command == "show":
        target_oid = args.oid
        show(target_oid, tokens)


if __name__ == '__main__':
    main()