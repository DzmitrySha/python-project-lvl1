#!/usr/bin/env python
from brain_games.cli import welcome_user

def greet(who):
    print(f'Welcome to the {who}!')

def main():
    greet('Brain games')
    welcome_user()


if __name__== '__main__':
    main()
    
