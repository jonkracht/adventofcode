#!/usr/bin/python3
import argparse
import subprocess
import sys


# Taken from https://github.com/jonathanpaulson/AdventOfCode/tree/master

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5fd93aace93ad7e0e2f0e2dcae886c6ca997377eaeb4dd31b217debb80eab220a0e277472952e1dcb1fd65ab913a42ca52eb06b3f7074e6308'

#SESSION = '53616c7465645f5fb1dc6895a282beff4e8cf60807d54389ac940b735c26c3fa1781e2c7229ddb84ee6c8613147f8657683125ed7c6cbdb1eb204d64a27186e9'
#SESSION = '53616c7465645f5f02a746d34b0f0ae70dd29a2c2d6ffe48cf7682048c51abb2a8f96dcfdf37739212e1e6bdc8ad76f36de494a0a31ca71789b61269fe515248'
useragent = 'github.com/jonkracht'

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2024)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A \'{useragent}\''
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
