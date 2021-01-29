'''
    Author: Joshua Cholmondeley
'''

def hello():
    print("ECSE3038 - Engineering IoT Systems")

def validPassword(password):
    alnum, nums = 0, 0

    if len(password) >= 8 and password.isalnum():
        for val in password:
            try:
                if isinstance(int(val), int):
                    nums += 1
            except:
                pass
        
        if nums >= 2:
            return ("Valid password")
    
    return ("Invalid password")

def sumUpToN(num):
    val = 0

    if num > 1:
        for i in range(1, num+1):
            val += i
    else:
        val = -1

    return val 

if __name__ == "__main__":
    # question 1
    hello()
    print("\n")

    # question 2
    password = "muggl3b0rn"
    print(validPassword(password))
    print("\n")
                
    # question 3
    sum = sumUpToN(25)
    print(sum)