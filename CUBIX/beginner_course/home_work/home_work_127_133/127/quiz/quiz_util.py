question_bank = [
    ("Hogy írják angolul: 'kedves'", r'^(nice|kind)$'),
    ("Hogy írják angolul: 'szerény'", r'^(modest|humble)$'),
    ("Hogy írják angolul: 'boldog'", r'^(happy|cheerful)$'),
    ("Hogy írják angolul: 'törtető'", r'^(careerist|placeman)$'),
    ("Hogy írják angolul: 'őrült'", r'^(crazy|mad)$'),
    ("Enter an odd integer:", r'^-?\d*[13579]$'),
    ("Enter an even integer:", r'^-?\d*[2468]$'),
    ("Enter a negative integer:", r'^-\d+$'), 
    ("Enter a negative float:", r'^-\d+\.\d+$'),
    ("Enter a float between 100 and 1000:", r'^([1-9]\d{2}\.\d+)$$'),
]