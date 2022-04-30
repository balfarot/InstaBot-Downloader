#Instagram bot that downloads profile picture
#Installing a library called instaloader

import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Instagram name of the user: ")
ig.download_profile(dp, profile_pic_only=True)