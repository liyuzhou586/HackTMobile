import random

def about(para):
    return str(para)

def giveUserPhoneOption():
    phoneOptionList = ['Iphone 6', 'Iphone 6s', 'Iphone 7', 'IPhone8', 'IphoneX', 'IphoneXS', 'IphoneXS_MAX']
    rd = random.randint(0,len(phoneOptionList)-1)
    return phoneOptionList[rd]

def queryFunc1(queryParam):
    # Better to implement it in another file.
    #TODO: Impmentent real query algorithm.
    return queryParam
