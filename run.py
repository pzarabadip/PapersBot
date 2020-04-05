# -*- coding: utf-_8 -*-
from __future__ import absolute_import
import sys
import click
from .papersbot import PapersBot


@click.command('cli')
@click.argument('bot_type')
@click.option('--doTweet', is_flag=True, help='Tweets the matched content')
@click.option('--toptweet', is_flag=False, help='Print top tweets')
def main(bot_type, doTweet, toptweet):  #pylint: disable=invalid-name
    """Missing Docstring """
    # try:
    #     regex = get_regex(bot_type)
    # except NameError:
    #     print("The requested '{}' does not exist".format(bot_type))
    #     sys.exit(1)

    # Initialize our bot
    if doTweet:
        bot = PapersBot(doTweet)

    # We can print top tweets
    if toptweet:
        bot.printTopTweets()
        sys.exit(0)

    bot.run()
    bot.printStats()


if __name__ == "__main__":
    main()
