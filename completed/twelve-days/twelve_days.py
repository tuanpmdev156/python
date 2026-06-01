def recite(start_verse, end_verse):
    days_with_gifts = [
        ('first', 'a Partridge in a Pear Tree'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
    ]

   

    # verses = []
    # for day in range(start_verse, end_verse + 1):
    #     reversed_gifts = list(reversed(days_with_gifts[:day]))
    #     date = days_with_gifts[day - 1][0]
    #     gifts = ''
    #     if len(reversed_gifts) == 1: 
    #         # return first gift
    #         gifts = reversed_gifts[0][1]
    #     if len(reversed_gifts) > 1:
    #         # loop to combine gifts
    #         for item in reversed_gifts:
    #             # check last gift to add 'and' word
    #             if reversed_gifts.index(item) == day - 1:
    #                 gifts += 'and ' + item[1]    
    #             else: gifts +=  item[1] + ', '
    #             print('gifts:', gifts)
    #     setence = f'On the {date} day of Christmas my true love gave to me: {gifts}.'
    #     verses.append(setence)
    # return verses

    verse = []

    for day in range(start_verse, end_verse + 1):
        day_word = days_with_gifts[day - 1][0]
        # Gather all gifts from current day, in reverse order
        current_gifts = [item[1] for item in days_with_gifts[:day]][::-1]
        # Format gift string base on day count
        if day == 1:
            gift_str = current_gifts[0]
        else:
            gift_str = ', '.join(current_gifts[:-1]) + f', and {current_gifts[-1]}'
        
        sentence = f'On the {day_word} day of Christmas my true love gave to me: {gift_str}.'
        verse.append(sentence)
    
    return verse


