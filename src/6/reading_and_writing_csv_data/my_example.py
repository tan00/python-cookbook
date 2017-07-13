#将指令性能测试工具生成的结果'HsmPerfTestResult.txt' \
#转换为csv格式, 可直接用excel打开

def chdir_to_curfiledir():
    import os,sys
    def cur_file_dir():
        path = sys.path[0]
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)
    os.chdir( cur_file_dir() )

chdir_to_curfiledir()

import re 
import csv 
class gen_csv_from_txt:    
    headers = ['线程数','循环数','效率(笔/秒)','吞吐量(Mbps)','成功率','请求报文']
    
    pattern_block = re.compile(r'运行统计结果((.|\n)*?)运行统计结束')
    pattern_threadnum = re.compile(r'线程数.*')
    pattern_loopnum = re.compile(r'单线程循环次数.*')
    pattern_reqmsg = re.compile(r'请求报文.*')
    pattern_rate = re.compile(r'成功率.*')
    pattern_eff = re.compile(r'效率.*')            #笔/秒
    pattern_throughput = re.compile(r'吞吐量.*')   #Mbps

    def __init__(self, sourceName='HsmPerfTestResult.txt'):
        self.sour = sourceName
        self.dest = self.sour.replace('.txt','.csv')

    #输入文件名  '''运行统计结果  运行统计结束'''  为界限返回文本块 迭代器
    def get_block(self,filename):
        with open(filename,'rt',encoding='gbk') as f:
            str = f.read() 
            yield from self.pattern_block.finditer(str)
    
    #获取一个块中的有效数据,组成列表
    def gen_listblock(self,iter):
        list = []
        block = iter.group()

        line = self.pattern_threadnum.findall(block)
        threadnum = re.split(r'[:\s]\s*',  str(line[0])) 
        list.append(threadnum[1])

        line = self.pattern_loopnum.findall(block)
        loopnum = re.split(r'[:\s]\s*',  str(line[0])) 
        list.append(loopnum[1])

        line = self.pattern_eff.findall(block)
        eff = re.split(r'[:\s]\s*',  str(line[0]))
        list.append(eff[1])

        line = self.pattern_throughput.findall(block)
        throughput = re.split(r'[:\s]\s*',  str(line[0]))
        list.append(throughput[1])

        line = self.pattern_rate.findall(block)
        rate = re.split(r'[:\s]\s*',  str(line[0]))
        list.append(rate[1])

        line = self.pattern_reqmsg.findall(block)
        reqmsg = re.split(r'[:\s]\s*',  str(line[0]))
        list.append(reqmsg[1])

        return list

    def gen_csv(self):     
        iter = self.get_block(self.sour)
        with open(self.dest ,'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(self.headers)
            for x in iter:
                row = self.gen_listblock(x)            
                f_csv.writerow(row)


if __name__ == '__main__':
    gen = gen_csv_from_txt('HsmPerfTestResult.txt')
    gen.gen_csv()


