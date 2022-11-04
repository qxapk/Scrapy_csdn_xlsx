import json
class Pipeline:
    count = 0
    def __init__(self):
        self.file = open('shuju.txt', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False) + '\n')  # 写入数据到文件
        if(Pipeline.count >= 100):#设置多少条保存一次
            self.file.close()
            Pipeline.__init__(self)
            Pipeline.count = 0
        Pipeline.count+=1
        return item