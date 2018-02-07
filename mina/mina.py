#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : since 2018-02-06 02:26
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : add remove show and list totp tokens in the terminal

import argparse
    
# the main function to control the script
def main():
    _desc = 'MinaOTP is a two-factor authentication tool that runs in the terminal'
    parser = argparse.ArgumentParser(description=_desc)

    parser.add_argument(
        dest='list',
        action='store',
        help='list all tokens that have been added to local'
    )
    parser.add_argument(
        '-a',
        dest='new_token',
        action='store',
        help='add a new token'
    )
    parser.add_argument(
        '-r',
        dest='err_token',
        action='store',
        help='remove a token'
    )
    parser.add_argument(
        '-s',
        dest='token_to_show',
        action='store',
        help='show a token on-time'
    )

    args = parser.parse_args()

if __name__ == '__main__':
    main()