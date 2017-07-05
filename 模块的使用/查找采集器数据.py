import json

# 根据文件名和内容保存文件
def saveFile(fileName,content):
    svf = open(('File\\%s' % fileName),'w',-1,'UTF_8')
    # for txt_line in content:
    #     savf.write(txt_line)
    svf.writelines(content)  # 可用writelines来代替上面的代码
    svf.close()



# 解析日志文件并选出对应的设备ID,存储为设备ID名.txt
def resolveFile(fileName,deviceNo,chanle):
    log_list = []
    f = open(('File\\%s' % fileName), 'r', -1, 'UTF-8')
    for each_line in f:
        if (('RECV') in each_line) and (('"dev":\"' + deviceNo + '\"') in each_line):

            log_list.append(each_line)
    saveFile(('%s.txt' % deviceNo),log_list)
    f.close()
    resolveDiveceFile(deviceNo,chanle)


# 根据上面方法中保存的设备ID名.txt文件找出特定通道(chanle)中的数据,并存为文件
def resolveDiveceFile(fileName,chanle):
    log_list = []
    f = open(('File\\%s.txt' % fileName), 'r', -1, 'UTF-8')
    for each_line in f:
        if ('"rid":%d' % chanle) in each_line:
            (time,data_temp) = each_line.split('<=')

            time = time.split('DEBUG')[0]
            data_temp = data_temp.split(']',1)[1]

            index = data_temp.find('{\"rid\":%d' % chanle)
            data = data_temp[index:].split('}',1)[0]
            log_list.append(time+":"+data+'\n')

            # log_list.append(time+":"+data_temp)

    saveFile('%s-%s.txt' % (fileName,chanle),log_list)
    f.close()

resolveFile('acp-web-adapter-N.20170702.log','E70017',134)
