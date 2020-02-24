from twitter_bot import TwitterBot

def main():
    bot = TwitterBot()

    print("Logging you in!")
    bot.login()

    cont = True

    while(cont):
        print("What would you like to do?")
        print("\t1. Write a tweet")
        print("\t2. Get trending topics")
        print("\t3. Get number of and read notifications")
        print("\t4. Logout")
        print("\t5. Exit")

        reply = input("Choice: ")
        
        if(int(reply) == 1):
            tweet_text = input("Tweet: ")
            image_path = input("image path (leave empty if none): ")

            if(image_path == ""):
                bot.sendTweet(tweet_text, None)
            else:
                bot.sendTweet(tweet_text, image_path)
        elif(int(reply) == 2):
            bot.getTrendingTopics()
        elif(int(reply) == 3):
            bot.getNumberofNotifications()
        elif(int(reply) == 4):
            bot.logout()
        elif(int(reply) == 5):
            cont = False

    exit()

if __name__ == "__main__":
    main()