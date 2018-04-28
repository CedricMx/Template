# !/usr/bin/python2
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

import ftrack_api
import pprint

# # Print all value by session
# session = ftrack_api.Session(
#     server_url='https://ftk.soovii.com',
#     api_user='cedric_tan@soovii.com',
#     api_key='44e604d6-25a4-11e8-a91b-14187740b71a'
#     )
#
# pprint.pprint(session.types.keys())
# session.close()


# Print all value
def print_all_value():
    session = ftrack_api.Session(
        server_url='https://ftk.soovii.com',
        api_user='cedric_tan@soovii.com',
        api_key='44e604d6-25a4-11e8-a91b-14187740b71a'
        )

    values = session.types.keys()
    pprint.pprint(values)
    session.close()

    # for value in values:
    #     try:
    #         check_info(value)
    #     except:
    #         continue


def check_info(session_value):
    session = ftrack_api.Session(
        server_url='https://ftk.soovii.com',
        api_user='cedric_tan@soovii.com',
        api_key='44e604d6-25a4-11e8-a91b-14187740b71a'
        )

    values = session.query(session_value)
    print '-'*80
    print 'Value of {} :'.format(session_value)
    pprint.pprint(values[0].keys())

    session.close()


# Test
# print_all_value()
check_info('Component')
