# 按照题目顺序读如文件，得到上述四个统计量之后，存储csv文件
import pandas as pd 
import numpy as np
import os

#path = './Result'
#path = './TestResult/aigis-kyber90s_dilithium/Near/kyber90s_dilithium3'

delays = ['Near', 'Medium', 'Far', 'Worst']
algs = ['90s', 'aigis']

#for delay in delays:
#   os.mkdir('./R2/'+delay)

for delay in delays:
    for alg in algs:
        path = './TestResult/90s-aigis/' + delay + '/'+alg
        path_list = os.listdir(path)
        path_list.remove('tm.avg')
        path_list.sort(key=lambda x: int(x.split('.')[0]+x.split('.')[1]))  
        per5list = []
        medianlist = []
        per95list =[]
        meanlist = []
        
        for filename in path_list:
            with open(os.path.join(path,filename)) as f:
                result = [int(x) for x in f]
                result_sorted = sorted(result)

            #5%分位数
            per5 = np.percentile(result_sorted,5)
            per5list.append(per5)

            #中位数
            median = np.median(result_sorted) 
            medianlist.append(median)

            #95%分位数
            per95 = np.percentile(result_sorted,95)
            per95list.append(per95)

            #5% 到 95% 平均数
            result_5and95 = [x for x in result_sorted if x >= per5 and x <= per95]
            mean = np.mean(result_5and95)
            meanlist.append(mean)

            #print(per5,median,per95,mean)
        
        #print(per5list,medianlist,per95list,meanlist)
        dataframe = pd.DataFrame({'per5':per5list,'median':medianlist,'per95':per95list,'mean':meanlist})
        f = './R2/' + delay + '/' + alg +'.csv'
        dataframe.to_csv(f,index=False,sep=',')
