with open ('D:\TestCode\hclg_testcode\hz2phone.txt','r',encoding='utf-8') as f1 , open ('D:\TestCode\hclg_testcode\corpus_class_based.txt','r',encoding='utf-8') as f2:
    linelist = [l.strip('\n') for l in f1.readlines()] #末尾空格不去除，因为需要多个词的拼音组合
    linelist_2 = [l.strip('\n') for l in f2.readlines()] 
f1.close()
f2.close()

dict_hz2phone = dict([tuple(l.split(" ",1)) for l in linelist]) #将hz2phone.txt文件转化成字典，键为汉字，值为音素
k1_k2_list = [(l.split(" ",2))[:2] for l in linelist_2] #取每行前两个词放入列表
ci_list = list(set([x for list_outer in k1_k2_list for x in list_outer if "CLASS" not in x ])) #不含CLASS字符的词，去重

with open("D:\TestCode\hclg_testcode\dict_py.txt","a+",encoding='utf-8') as f3: 
    for item in ci_list:
        ci2phone_list = []
        for x in item:
            ci2phone_list.append(dict_hz2phone[x])
        f3.write(f"{item} {''.join(ci2phone_list)}\n")
f3.close()