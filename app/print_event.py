import json


def print_event(event):
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        if record['eventName'] == 'INSERT':
            newimage = record['dynamodb']['NewImage']
            print("newimage: " + json.dumps(newimage))
        elif record['eventName'] == 'MODIFY':
            olditem = record['dynamodb']['OldImage']
            newitem = record['dynamodb']['NewImage']
            print("olditem: " + json.dumps(olditem))
            print("newitem: " + json.dumps(newitem))
        elif record['eventName'] == 'REMOVE':
            deletedItem = record['dynamodb']['OldImage']
            print("deleteimage: " + json.dumps(deletedItem))
