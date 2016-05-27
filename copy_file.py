#!/usr/bin/env python
# coding=utf-8
import os
import time

#the path of data what want to copy
source = '/root/下载/'
#the path where the backup data
target = '/var/root_data_backup'

#create the path,if not exist
if os.path.exists(target)==False:
    os.mkdir(target)

today = target  + os.sep +\
        time.strftime('%Y%m%d');

if os.path.exists(today)==False:
    os.mkdir(today)

zip_file = today +os.sep + time.strftime("%H%M%S")+'.zip'

zip_command = 'zip -r {0} {1}'.format(zip_file, ' '+source)

if os.system(zip_command) == 0:
    print('good')
else:
    print('bad')

exit()


