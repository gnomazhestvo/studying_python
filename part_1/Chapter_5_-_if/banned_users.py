banned_users = ['andrew', 'carolina', 'david']
users = ['marie', 'andrew', 'nastya', 'david', 'carolina', 'mashhur']

for user in users:
    if user not in banned_users:
        print(f'Congratulations, {user.title()}! You can post a response if you wish.')
    else:
        print(f'Hehe, {user.title()}! Probably you are frik (banned).')