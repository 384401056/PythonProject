
# 根据文件名和内容保存文件

def saveFile(fileName,content):
    savf = open(('File\\%s' % fileName),'w',-1,'UTF_8')

    # for txt_line in content:
    #     savf.write(txt_line)

    savf.writelines(content)  # 可用writelines来代替上面的代码
    savf.close()

# 解析record.txt文件
def resolveFile(fileName):
    boy = []
    girl = []
    i = 1
    myFile = open(fileName, 'r', -1, 'UTF-8')
    for each_line in myFile:
        if each_line[:6] != '======':

            # 通过':'来分割成somebody和speakContent
            (somebody,speakContent) = each_line.split(':',1)

            if somebody == '小明说':
                boy.append(speakContent)
            elif somebody == '小红说':
                girl.append(speakContent)
        else:
            saveFile(('boy_%02d.txt' % i), boy)
            saveFile(('girl_%02d.txt' % i),girl)
            boy.clear()
            girl.clear()
            i += 1

    saveFile(('boy_%02d.txt' % i), boy)
    saveFile(('girl_%02d.txt' % i),girl)
    myFile.close()

# 调用方法
resolveFile('record.txt')