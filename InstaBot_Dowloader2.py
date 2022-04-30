#Downloading pictures and comments/hashtags from those posts that have certain hashtags

import instaloader

from instaloader import Profile, Post
insta = instaloader.Instaloader()
insta.download_hashtag(hashtag="nflgame", max_count=10)