from pystark import Stark
from pyromod import listen
from database.users_sql import Users

bot = Stark()
Users.__table__.create(Users.bind, checkfirst=True)


@staticmethod
def main():
    bot.activate()


if __name__ == "__main__":
    try:
        main()
    except:
        print("There was an error while starting the bot.")
        bot.stop()
