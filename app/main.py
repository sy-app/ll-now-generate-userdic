from print_event import *
from update_userdic import *

table_name = 'll-now-user-dict'
bucket_name = 'll-now-material'


def main(event, context):
    print_event(event)
    update_userdic(table_name, bucket_name)
