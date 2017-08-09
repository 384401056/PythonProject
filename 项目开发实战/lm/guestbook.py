import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    ''' 保存提交的数据 '''