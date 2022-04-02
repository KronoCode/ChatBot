import re


def get_response(user_input):
    split_message=re.split(r'\s+|[,;:=/.?-]\s*',user_input.lower())

    print(split_message)
    response=check_user_message(split_message)

    return response


def check_user_message(message):
    highest_prob_list={}

    def responses_bot(bot_response,recognised_words,required_words):
        nonlocal highest_prob_list

        highest_prob_list[bot_response]=message_certainty(message,recognised_words,required_words)

    dates_choice = ['wednesday 15 September', 'thursday 16 September', 'monday 20 September']

    responses_bot('Hi',['hi','hello','sup'],['hi','hello','sup'])
    responses_bot('I\'m good and you?', ['how', 'are', 'you'], ['how', 'you'])
    responses_bot('Sure, here are the available dates, please choose one: ' + str(dates_choice), ['appointment','would', 'like', 'take'],
                  ['appointment'])
    try:
        responses_bot('Your appointment will take place'+str((" ".join(re.split(r'\s+|[,;:=/.?-]\s*',user_input.lower()))).split('wednesday')[1])+ '.Can i help you with something else?' , [ 'monday' ,'tuesday','wednesday','thursday','friday'],[ 'monday' ,'tuesday','wednesday','thursday','friday'])
    except:
        pass
    best_response = max(highest_prob_list, key=highest_prob_list.get)

    print(highest_prob_list)

    return best_response


def message_certainty(message,recognised_words=[],required_words=[]):
    certainty=0

    for word in message:
        if word in recognised_words:
            certainty += 1

    percentage = float(certainty)/float(len(recognised_words))
    for word in message:
        if word in required_words:
            return int(percentage*100)

    else:
        return 0


def intro():

    return 'Hi, how can I help you?'

print('Bot: '+ intro())
while True:
    user_input=input('You :')
    print('Bot: '+ get_response(user_input))