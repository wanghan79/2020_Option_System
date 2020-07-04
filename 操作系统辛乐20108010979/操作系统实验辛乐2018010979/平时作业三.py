import os, multiprocessing

cpu=os.cpu_count # 获取电脑核数
p = multiprocessing.Pool(processes=cpu)

for rankBY in data:   # data 是要多进程处理的参数
    p.apply_async(main, args=(rankBY, ))
print('正在多进程抓取写入第goods层链接')
p.close()
p.join()
print('第goods层链接写入完成!')
print("line to mysql..")