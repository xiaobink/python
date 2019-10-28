# 请独立完成这个产品吧，我相信你可以的！
from random import choice

print('欢迎使用推荐吃饭小程序')

restaus = {'第九站': ['农家小炒肉饭', '啤酒鸭饭', '土豆肉丝饭', '红烧茄子'], '五谷鱼粉': ['招牌鱼粉', '酸辣鱼粉', '茄香鱼粉', '酸菜鱼饭'],
           '桂林米粉': ['招牌卤粉', '叉烧卤粉', '牛肉卤粉', '三鲜菌汤粉', '茄汁汤粉']}


ans1 = input('完全不知道吃什么请输入1，输入其他代表你有想吃的那家店：')
if ans1 == '1':

    while 1:
        restau = choice(list(restaus.keys()))

        print('为您推荐%s这家餐厅' % restau)
        ans2 = input('是否喜欢,喜欢请输入1，输入其他表示不喜欢:')

        if ans2 == '1':
            while 1:

                menu = choice(restaus[restau])
                print('为您推荐%s的 %s 这个菜' % (restau, menu))
                ans3 = input('是否喜欢,不喜欢请输入1，输入其他则退出:')
                if ans3 == '1':
                    del restaus[restau][restaus[restau].index(menu)]
                    continue
                else:
                    break
            break

        else:
            del restaus[restau]
            continue

else:

    user_choise = input('请输入你想去的餐厅:')
    while 1:
        menu1 = choice(restaus[user_choise])
        print('为您推荐%s的 %s 这个菜' % (user_choise, menu1))
        ans4 = input('是否喜欢,不喜欢请输入1，输入其他则退出:')
        if ans4 == '1':
            del restaus[user_choise][restaus[user_choise].index(menu1)]
            continue
        else:
            break
print('欢迎再一次使用，下次见')