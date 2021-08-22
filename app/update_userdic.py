import boto3
import csv


def update_userdic(table_name, bucket_name):
    # Dynamodbからtermsを取得
    table = boto3.resource('dynamodb').Table(table_name)
    res = table.scan()
    terms = [item['term'] for item in res['Items']]

    # 新しいユーザ辞書を作成
    file_path = '/tmp/lovelive_word_dic.csv'
    with open(file_path, mode="w", encoding="utf_8_sig") as f:
        writer = csv.writer(f)
        for term in terms:
            line = [term, -1, -1, 1000, '名詞', '一般', '*', '*', '*', '*', term, '*', '*']
            writer.writerow(line)

    # ユーザ辞書をs3にアップロード
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    file_key = 'lovelive_word_dic.csv'
    bucket.upload_file(file_path, file_key)
