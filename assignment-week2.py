# 要求一
def calculate(min,max):
    total=0
    for i in range(min,max+1):
        total=total+i
    print(total)
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#要求二 
def avg(data):
    long=len(data["employees"])
    count=data["count"]
    employees=data["employees"]
    a=0
    for i in range(0,long):
        name=dict(employees[i])
        salary=name["salary"]
        a=a+salary
    print("薪水平均是",a/long)
# 請用你的程式補完這個函式的區塊
avg({
        "count":3,
        "employees":[
            {
            "name":"John",
            "salary":30000
            },
            {
            "name":"Bob",
            "salary":60000
            },
            {
            "name":"Jenny",
            "salary":50000
            }
        ]
}) # 呼叫 avg 函式

# 要求三
def maxProduct(nums):
        a=0
        b=0    
        for i in nums:
            if i > a :
                a=i
            elif b < i < a :
                b=i           
        print(a*b,"因為",a,"和",b,"相乘得到最大值")        
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

# 要求四
def twoSum(nums, target):
    a=0
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
                a=nums[i]+nums[j]
                if a == target:
                    if i < j:
                        print("[",i,",",j,"] because nums[",i,"]+nums[",j,"] is ",target)
# your code here
result=twoSum([2, 11, 7, 15], 9)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9

