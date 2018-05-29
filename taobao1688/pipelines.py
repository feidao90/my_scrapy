# -*- coding: utf-8 -*-

import json
from taobao1688.items import Taobao1688DetailItem

class Taobao1688Pipeline(object):
    """
    功能：保存item数据
    """

    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('taobao1688.json', 'a', encoding='utf-8') as writefile:
            json.dump(dict(item), writefile, ensure_ascii=False)
        return item
