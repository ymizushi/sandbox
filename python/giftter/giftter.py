#!/usr/bin/env python3
import twitter
import MeCab



class User:
    def __init__(self, name, profile):
        self._name = name
        self._profile =profile


    def is_adhd(self):
        """
        ADHDが含まれていたらTrue
        """
        pass


class TwitterClient:
    CONSUMER_KEY = '0ymMbsjSqPGcdug8Bcm84fjhC'
    CONSUMER_SECRET = 'tYPG4aqFzpr3qSwLa44CZhMBUkrgtf86GHbwCAufulmJLbuAqU'
    OWNER_ID = '3261343579'
    ACCESS_TOKEN = '3261343579-fKm8K6H8C4Eiva6yTSefETK67p57g8hlzkvnIAO'
    ACCESS_TOKEN_SECRET = 'HqArXFde1Kk1B6a27rp9Yuv5bXINgimlMQPUQTsRzzQ8Y'

    def __init__(self):
        self._client = twitter.Api(consumer_key=self.CONSUMER_KEY,
                          consumer_secret=self.CONSUMER_SECRET,
                          access_token_key=self.ACCESS_TOKEN,
                          access_token_secret=self.ACCESS_TOKEN_SECRET)

    def search_adhd_accounts():

        pass

    def search_normal_accounts() -> [User]:
        """
        返り値は keyをアカウント名, valueをコメントのリストににしたDict
        """
        pass

    def get_latest_comment(name, count=100) -> [str]:
        """
        userからコメントを取得
        """
        pass

    def get_user_timeline():
        statuses = api.GetUserTimeline(screen_name='ymizushi')
        print([s.text for s in statuses])
        print(api.VerifyCredentials())

class MecabClient:
    def __init__(self, client=MeCab.Tagger ("-Ochasen")):
        self._client = client

    def parse(text):
        return self._client.parse(text)


GLOBAL_FEATURE_WORD_DICT = {} # {単語名: 真偽値}
def create_feature_word_list(text, mecab_client):
    filtered_text = mecaba_client.parse(text)
    # TODO: ADHDをフィルター
    return filtered_text


def shuffle(a, b):
    pass


def __name__ == '__main__':
    twitter_client = TwitterClient()
    adhd_accounts = twitter_client.search_adhd_accounts()
    normal_accounts = twitter_client.search_normal_accounts()
    accounts = shuffle(adhd_accounts, normal_accounts)
    account_comments = [(account, twitter_client.get_latest_comment(account.name)) for account in accounts]
    for account, comments in account_comments:
        

        mecab_client = MecabClient)
