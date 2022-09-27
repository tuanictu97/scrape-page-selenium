import random

from scape import register, User
from util import PHONE_ARRAY, NAME_ARRAY
from slugify import slugify


def write_user_to_file(user: User):
    f = open("user.txt", "a")
    f.write("{}|{}|{}|{}\n".format(user.phone, user.email, user.date, user.password))
    f.close()


def auto_register():
    for e in PHONE_ARRAY:
        random_name = random.choice(NAME_ARRAY)
        date_number = random.randint(1, 28)

        if date_number < 10:
            date_str = '0{}'.format(date_number)
        else:
            date_str = '{}'.format(date_number)
        month_number = random.randint(1, 12)

        if month_number < 10:
            month_str = '0{}'.format(month_number)
        else:
            month_str = '{}'.format(month_number)
        random_num = random.randint(1997, 2004)
        user = User(
            name=random_name,
            date='{}/{}/2000'.format(date_str, month_str),
            email='{}_{}_{}@gmail.com'.format(slugify(random_name), random_num, month_number),
            phone=e,
            password='123123'
        )
        try:
            rs = register(user)
            if rs:
                write_user_to_file(user=user)
        except Exception as e:
            print(e)
            register(user)


if __name__ == '__main__':

    try:
        print('Starting auto.....!')
        auto_register()
    except Exception as e:
        print(e)
