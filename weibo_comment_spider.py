import random
import re
import requests
import sys
import time

httpHeaders = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Host': 'm.weibo.cn',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'xxxxxxxxxxxxxxxxxxx',  # input your cookie here
    'DNT': '1',
    'Connection': 'keep-alive',
}


def main(argv):
    comment_id = "4211804613220003"
    url = "https://m.weibo.cn/api/comments/show?id=" + comment_id + "&page={}"
    f_orig = open("orig_data.txt", "wb+")
    f_mod = open("mod_data.txt", "wb+")
    comment_detail = {}
    i = 1

    while True:
        req = requests.get(url=url.format(i), headers=httpHeaders)
        status_code = req.status_code

        if status_code == 200 and i < 101:
            print('正在读取第 %d 页评论：' % i)
            comment_page = req.json()['data']['data']

            for j in range(0, len(comment_page)):
                f_orig.write((str(comment_page[j]) + '\n').encode('utf-8'))

                comment_detail['id'] = comment_page[j]['id']
                comment_detail['created_at'] = comment_page[j]['created_at']
                comment_detail['user_id'] = comment_page[j]['user']['id']
                comment_detail['screen_name'] = comment_page[j]['user']['screen_name']
                comment_detail['text'] = re.sub('<.*?>|回复<.*?>:', '', comment_page[j]['text'])

                f_mod.write((str(comment_detail) + '\n').encode('utf-8'))
                print('第 %d 条评论: %s' % (j, str(comment_detail)))

            i += 1
            time.sleep(random.randint(5, 10))
        else:
            break

    f_mod.close()
    f_orig.close()


if __name__ == "__main__":
    main(sys.argv)
