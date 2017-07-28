# Reddit Translation Bot

A bot that translates the text of any post or comment when called from any language to any language.

## Table of Contents

- [Project Overview](#project-overview)
- [Demo](#demo)
- [Contact](#contact)

## Project Overview

This was a project I'd been wanting to dig into for a little while. I will shamelessly admit that I'm a frequent Reddit browser, and so I'd seen plenty of bots commenting on random feeds and had to join the party. I also browse r/programming often, and so I knew Reddit was a programmer friendly place. 

I used the Reddit API to read messages from the bots' inbox, find the right place to comment, and post the comment. The Google Translate API handled the translation itself, making translation available to and from any language that it supports.

The Reddit API was the first API I'd ever interacted with, so it was definitely a process of bumbling around a bit before I got my feet under me. I've since used dozens, but at the time I had no experience. I read all of the PRAW docs so that I could have a general understanding of what was going on and proceeded from there. I was thrilled when I first got everything working and saw my translations appearing on the page!

## Demo

Let's head to the CryptoMarkets subreddit to test this out. It's a pretty straightforward process: you simply comment underneath a post or a comment with a call to the bot and the language you'd like to translate to, like so:
![alt text](https://github.com/benhubsch/Reddit-Translation-Bot/blob/master/pics/reddit2.png "Comment")
You can see the call to u/BotTranslator and the request for Russian. Note that the source language need not be specified, as it can be detected by Google Translate. Therefore, you can ask for a translation from a language you don't even recognize and get a response.

Here's a sample response:
![alt text](https://github.com/benhubsch/Reddit-Translation-Bot/blob/master/pics/reddit3.png "Reply")
Assuming that most of you don't know Russian, the response is broken up into two parts. The first starts with "Title:", followed by the title of the post. The second starts with "Content:", followed by the content of the post. Therefore, the title "Bittrex question: Is there a way to change the "% CHANGE" settings in the wallet display?" translates to 
Вопрос Bittrex: Есть ли способ изменить настройки «% CHANGE» на дисплее кошелька?" according to Google Translate, and the content of the post corresponds to "Я заметил, что это показывает изменение% в тот...".

This also works on comments (not just posts), but the difference is that there'd be no "Title:" message:
![alt text](https://github.com/benhubsch/Reddit-Translation-Bot/blob/master/pics/comment.png "Comment Only")
This time, only the content is posted as part of the reply. It's in Japanese, as requested.

## Contributing

I think it would be interesting to come up with a fun data science project using the Reddit API at some point. We could come up with some cool visualizations about how traffic spikes at certain times of the day or during certain days of the year. I don't know. Might have to tackle it at some point. Have any ideas or want to work with me? Let me know!
