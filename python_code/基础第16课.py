import time
count=0

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = float(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：'%(task_name,task_time))
    # 下面应该要有两行代码，自动记录可以计算以及可以打印的开始时间。
    time0=time.time()
    time1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time0))
    print('当前时间为%s,现在开始计时'%time1)


    # 这里可以加一个倒计时，实时显示还剩多少时间，可参考左侧提供的资料。代码量大概有5行。
    while 1:
        count_now=time0-count
        time2=time.localtime(count_now)
        time3=time.strftime('%M:%S',time2)
        print('倒计时中：%s'%time3)
        time.sleep(1)
        count+=1
        if count>task_time*60:
            print(count)
            break

    task_status = input('请在任务完成后按输入y:')
    actual_time = input('该任务实际用时为几分钟？')
    if task_status == 'y':
        # 下面应该要有两行代码，自动记录可以计算以及可以打印的结束时间。
        # 有了自动记录的始末时间后，记录的代码也需要随之改变。
        with open('timelog2.txt','a', encoding = 'utf-8') as f:
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':            
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')
