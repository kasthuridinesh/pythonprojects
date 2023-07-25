def func1():
    achievements = 9

    def func2():
        nonlocal achievements
        achievements += 2
        print(achievements)
    func2()


func1()
