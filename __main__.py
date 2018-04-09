from argparse import ArgumentParser
from utils.templates import get_tempalte, render_context
from data_manager_class import User_Manager


parser = ArgumentParser(prog='hungry')
parser.add_argument('type', type=str, choices=['view', 'message'])
parser.add_argument('-id', '--edit_id', type=int)
parser.add_argument('-e', '--email', type=str)

args = parser.parse_args()

p = User_Manager()
if args.type == 'view':
    print(p.get_user_data(edit_id=args.edit_id, email=args.email))
elif args.type == 'message':
    print(p.message_user(edit_id=args.edit_id, email=args.email))
print('send message')

'''
print(args)
print(args.edit_id)
print (User_Manager.get_user_data(edit_id = args.edit_id))
print (User_Manager.get_user_data(email = args.email))
'''
