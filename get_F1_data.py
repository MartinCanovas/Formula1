#!/usr/bin/env python

import urllib2
import argparse
import sys
from blessings import Terminal

URL_DRIVER_CURRENT = 'http://ergast.com/api/f1/current/driverStandings'
URL_CONSTRUCTOR_CURRENT = 'http://ergast.com/api/f1/current/constructorStandings'
URL_BASE = 'http://ergast.com/api/f1/'

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Python script to fetch Formula 1 data.')
    parser.add_argument('-race', '--race', help='Race Results', action='store_true')
    parser.add_argument('-q', '--qualifying', help='Qualifying Results', action='store_true')
    parser.add_argument('-d', '--driver_standings', help='Driver Standings', action='store_true')
    parser.add_argument('-c', '--constructor_standings', help='Constructor Standings', action='store_true')
    parser.add_argument('-y', '--year', help='Year', type=str)
    parser.add_argument('-r', '--round', help='Round', type=str)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.1')
    args = parser.parse_args(args)

    if len(sys.argv) == 1:                       # check if no arguments were provided
        parser.print_help()
        print
        sys.exit(1)

    return args

def find_between(char, first, last):
    try:
        start = char.index(first) + len(first)
        end = char.index(last, start)
        return char[start:end]
    except ValueError: return ""

def getDriversInfo(url):
    httpGet = urllib2.urlopen(url)
    page = httpGet.read()
    page = page.split('\n')
    term = Terminal()
    print
    for line in page:

        if 'position=' in line:
            position = line.split(' ')[1]
            with term.location(x=0):
                print find_between(position, "position=\"", "\""),
            points = line.split(' ')[3]
            with term.location(x=24):
                print find_between(points, "points=\"", "\""),
        elif 'GivenName' in line:
            firstName = line.split('/')[0]
            with term.location(x=3):
                print find_between(firstName, ">", "<"),
        elif 'FamilyName' in line:
            lastName = line.split('/')[0]
            with term.location(x=13):
                print find_between(lastName, ">", "<")
    print

def getConstructorInfo(url):
    httpGet = urllib2.urlopen(url)
    page = httpGet.read()
    page = page.split('\n')
    term = Terminal()
    print
    for line in page:
        if 'position' in line:
            position = line.split(' ')[1]
            with term.location(x=0):
                print find_between(position, "position=\"", "\""),
            points = line.split(' ')[3]
            with term.location(x=18):
                print find_between(points, "points=\"", "\""),
        elif 'Name' in line:
            constructor = line.split('/')[0]
            with term.location(x=3):
                print find_between(constructor, ">", "<")
    print

def getRaceResults(url):
    httpGet = urllib2.urlopen(url)
    page = httpGet.read()
    page = page.split('\n')
    term = Terminal()
    print
    for line in page:
        if 'RaceName' in line:
            RaceName = line
            print term.magenta(find_between(RaceName, ">", "<")),
            print term.magenta('-'),
        elif '<Date>' in line:
            Date = line
            print term.magenta(find_between(Date, ">", "<"))
            print '---------------------------------'
        elif 'position=' in line:
            position = line.split(' ')[2]
            with term.location(x=0):
                print find_between(position, "position=\"", "\""),
            points = line.split(' ')[4]
            with term.location(x=27):
                print find_between(points, "points=\"", "\""),
        elif 'GivenName' in line:
            firstName = line.split('/')[0]
            with term.location(x=3):
                print find_between(firstName, ">", "<"),
        elif 'FamilyName' in line:
            lastName = line.split('/')[0]
            with term.location(x=13):
                print find_between(lastName, ">", "<")
    print

def getQualifying(url):
    httpGet = urllib2.urlopen(url)
    page = httpGet.read()
    page = page.split('\n')
    term = Terminal()
    print
    for line in page:
        if 'RaceName' in line:
            RaceName = line
            print term.magenta(find_between(RaceName, ">", "<")),
            print term.magenta('-'),
        elif '<Date>' in line:
            Date = line
            print term.magenta(find_between(Date, ">", "<"))
            print '---------------------------------'
        elif 'position=' in line:
            position = line.split(' ')[2]
            with term.location(x=0):
                print find_between(position, "position=\"", "\""),
        elif 'GivenName' in line:
            firstName = line.split('/')[0]
            with term.location(x=3):
                print find_between(firstName, ">", "<"),
        elif 'FamilyName' in line:
            lastName = line.split('/')[0]
            with term.location(x=13):
                print find_between(lastName, ">", "<"),
        elif 'Q1' in line:
            q1Laptime = line.split('/')[0]
            if 'Q2' in page[page.index(line) + 1]:
                with term.location(x=27):
                    print find_between(q1Laptime, ">", "<"),
            else:
                with term.location(x=27):
                    print find_between(q1Laptime, ">", "<")
        elif 'Q2' in line:
            q2Laptime = line.split('/')[0]
            if 'Q3' in page[page.index(line) + 1]:
                with term.location(x=37):
                    print find_between(q2Laptime, ">", "<"),
            else:
                with term.location(x=37):
                    print find_between(q2Laptime, ">", "<")
        elif 'Q3' in line:
            q3Laptime = line.split('/')[0]
            with term.location(x=47):
                print term.red(find_between(q3Laptime, ">", "<"))

    print

def main():
    args = getOptions(sys.argv[1:])

    if args.year and args.round and args.driver_standings:
        url = URL_BASE + args.year + '/' + args.round + '/driverStandings'
        getDriversInfo(url)
    elif args.year and args.round and args.constructor_standings:
        url = URL_BASE + args.year + '/' + args.round + '/constructorStandings'
        getConstructorInfo(url)
    elif args.year and args.round and args.race:
        url = URL_BASE + args.year + '/' + args.round + '/results'
        getRaceResults(url)
    elif args.year and args.round and args.qualifying:
        url = URL_BASE + args.year + '/' + args.round + '/qualifying'
        getQualifying(url)
    elif args.driver_standings:
        getDriversInfo(URL_DRIVER_CURRENT)
    elif args.constructor_standings:
        getConstructorInfo(URL_CONSTRUCTOR_CURRENT)

if __name__ == '__main__':
    main()