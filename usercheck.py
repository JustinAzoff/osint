#! /usr/bin/python

import requests, argparse, sys

# for debug_api
import logging
import httplib as http_client

def debug_api():
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def main():
    # use argparse instead of getopt
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--userid", required=True, help="Social Media Handle")
    parser.add_argument("--debug", action="store_true", help="Prints debug output using debug_api()")

    args = parser.parse_args()

    websites = ["https://www.instagram.com/", "https://twitter.com/", "http://pastebin.com/u/", "https://www.reddit.com/user/", "https://github.com/"]
    username = args.userid

    if args.debug:
        debug_api()

    for website in websites:
        url = website + username

        # use .json for reddit to avoid rate limiting and stuff
        if "reddit.com" in website:
            url += ".json"

        # use custom user agent because reddit wants bots to use them
        response = requests.get(url, allow_redirects=False, headers={'User-agent': 'uiuc-tsprivsec.usercheck:0.9'})
        if response.status_code == 200:
                print "[*] User exists here: " + url
        else:
                print "[!] User NOT FOUND here: " + url

if __name__ == '__main__':
    main()
