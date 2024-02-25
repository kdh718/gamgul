import random
import math

def generate_denominator():
    # 2 또는 5의 거듭제곱으로만 소인수분해될 수 있는 분모 생성
    denominator = 1
    powers_of_2 = [2**i for i in range(1, 6)]  # 2의 거듭제곱 리스트 [2, 4, 8, 16, 32]
    powers_of_5 = [5**i for i in range(1, 4)]  # 5의 거듭제곱 리스트 [5, 25, 125]

    # 2 또는 5의 거듭제곱을 무작위로 선택하여 분모에 곱함
    while True:
        choice = random.choice([2, 5])
        if choice == 2:
            denominator *= random.choice(powers_of_2)
        else:
            denominator *= random.choice(powers_of_5)
        
        # 분모가 50 미만인 경우 생성 완료
        if denominator <= 200 and denominator>5:
            return denominator
        else:
            denominator = 1

def q1(i): #평균 1 유형
    noshow = random.randint(3,7)
    realmember = random.randint(3,7) * noshow
    totalmember = realmember + noshow
    noshowmoney = random.randint(1,7) * 1000
    mul = realmember // noshow; q1money = noshowmoney * mul; ans = "%d원"%(q1money * totalmember)
    question_str1 = "여행을 가기위해 %d명이 버스를 대여했습니다. 그 중 %d명이 못가게 되어 나머지 사람이 %d원을 더 내게 되었을 때 버스 대여비는 얼마입니까?"%(totalmember, noshow, noshowmoney)
    while True:
        input_ans = input("%d. %s\n"%(i, question_str1))
        if input_ans == ans:
            break

def q2(i): #평균 2 유형
    noshow = random.randint(3,7)
    realmember = random.randint(3,7) * noshow
    totalmember = realmember + noshow
    noshowmoney = random.randint(1,7) * 1000
    mul = totalmember // noshow; q2money = noshowmoney * mul; ans = "%d원"%(q2money * realmember)
    question_str2 = "여행을 가기위해 %d명이 버스를 대여했습니다. 그 중 %d명이 더 가게 되어 %d원씩 덜 내게 되었습니다. 전체 요금은 동일할때 대여비는 얼마입니까?"%(realmember, noshow, noshowmoney)
    while True:
        input_ans = input("%d. %s\n"%(i, question_str2))
        if input_ans == ans:
            break

def q3(i): #간격 구하기
    str_type = ["직선", "원형"]
    num_type = [0, "한쪽", "양쪽"]
    while True:
        a = random.randint(30, 180)
        b = random.randint(5,13)
        if a % b!=0:
            break
    while True:
        str_type_idx = random.randint(0,1)
        num_street = random.randint(1,2)
        light = random.randint(15,50)
        real_light = light
        if num_street == 2:
            if light % 2 == 1:
                continue
            real_light = light // 2
        break
    if str_type_idx == 0:
        real_light = real_light - 1
    else:
        real_light = real_light
    gcd = math.gcd(a, real_light)
    Qa = "길이가 %d/%dkm인 %s 길의 %s에 같은 간격으로"%(a,b,str_type[str_type_idx], num_type[num_street])
    Qb = "가로등 %d개를 세우려고 할 때 가로등 사이의 간격은 몇 km인지 구하시오"%light
    Q = Qa + " " + Qb
    a = a / gcd; real_light = real_light / gcd
    ans = "%d/%dkm"%(a, b * real_light)
    while True:
        input_ans = input("%d. %s\n"%(i, Q))
        if input_ans == ans:
            break

def q4(i): #최소공배수 구하기
    while True:
        a=random.randint(12,99)
        b=random.randint(12,99)
        d=random.randint(12,99)
        ans=math.lcm(a,b,d)
        if a!=b and b!=d and ans<999: break
    while True:
        input_ans = input("%d. %d, %d, %d의 최소공배수를 구하시오.\n"%(i,a,b,d))
        if int(input_ans) == ans:
            break

def q5(i): #최대공약수 구하기
    while True:
        a=random.randint(50,999)
        b=random.randint(50,999)
        d=random.randint(50,999)
        ans=math.gcd(a,b,d)
        if a!=b and b!=d and ans>10: break
    while True:
        input_ans = input("%d. %d, %d, %d의 최대공약수를 구하시오.\n"%(i,a,b,d))
        if int(input_ans) == ans:
            break

def q6(i): #분배법칙
    while True:
        a = random.randint(-9,9)
        b = random.randint(-9,9)
        c = random.randint(-9,9)
        d = random.randint(-9,9)
        e = random.randint(-9,9)
        f = random.randint(-9,9)
        if a*b*c*d*e*f != 0 and a!=1 and d!=1:
            break
    str_a = a if a!=-1 else '-'
    str_b = b if b!=-1 else '-'
    str_e = e if e!=-1 else '-'
    str_c = "%d"%c if c<0 else "+%d"%c
    str_d = "%d"%d if d<0 else "+%d"%d
    if d==-1: str_d = "-"
    str_f = "%d"%f if f<0 else "+%d"%f
    q = "%s(%sx%s)%s(%sx%s)"%(str_a,str_b,str_c,str_d,str_e,str_f)
    if b==1:
        q = "%s(x%s)%s(%sx%s)"%(str_a,str_c,str_d,str_e,str_f)
    if e==1:
        q = "%s(%sx%s)%s(x%s)"%(str_a,str_b,str_c,str_d,str_f)
    if b==1 and e==1:
        q = "%s(x%s)%s(x%s)"%(str_a,str_c,str_d,str_f)
    co_x = a*b + d*e; cons = a*c + d*f
    if cons<0:
        str_cons = "%d"%cons
    elif cons==0:
        str_cons=""
    else:
        str_cons = "+%d"%cons
    ans = "%sx%s"%(co_x,str_cons)
    if co_x == 1:
        ans = "x%s"%(str_cons)
    elif co_x == 0:
        ans = "%s"%(cons)
    while True:
        input_ans = input("%d. %s = \n"%(i,q))
        if input_ans == ans:
            break

def q7(i): #분수의 나눗셈
    while True:
        a = random.randint(2,21)
        b = random.randint(2,21)
        c = random.randint(2,16)
        d = random.randint(2,16)
        e = random.randint(2,16)
        f = random.randint(2,16)
        c*=a; e*=a; d*=b;f*=b
        if a!=b and c<d and e<f and c!=e and d!=f: break
    cc = c//a; ee = e//a; dd = d//b;ff = f//b
    ans_1 = cc*ff; ans_2 = dd*ee
    g = math.gcd(ans_1, ans_2)
    ans_1/=g;ans_2/=g
    ans = "%d/%d"%(ans_1,ans_2)
    while True:
        input_ans = input("%d. %d/%d ÷ %d/%d = \n"%(i, c,d,e,f))
        if input_ans == ans:
            break

def q8(i): #비례식
    money = random.randint(2,15) * 100000
    str1 = "갑, 을, 병은 투자해서 얻은 수익금 %d원을 각각 투자한 비율만큼 나눠서 가지려고 한다. "%money
    deno = generate_denominator()
    while True:
        a, b, c = random.sample(range(1, deno), 3)
        if a+b+c==deno:
            break
    GCD = math.gcd(a,b,c)
    a//=GCD;b//=GCD;c//=GCD
    str2 = "갑, 을, 병의 투자 비율은 %d : %d : %d 일 때 ,"%(a,b,c)
    money_a = money //deno *a; money_b = money //deno *b; money_c = money //deno *c
    str3 = str1 + str2 + "갑, 을, 병이 받게 되는 투자금을 구하여라. (순서대로 입력, 띄어쓰기로 구분. 예)100원 200원 300원)"
    ans = "%d원 %d원 %d원"%(money_a,money_b,money_c)
    while True:
        input_ans = input("%d. %s\n"%(i,str3))
        if input_ans == ans:
            break

def q9(i): #소금물 1
    while True:
        after_salt_per = random.randint(1,30)
        solution = random.randint(1,9) * 100
        k = solution//100
        removed = random.randint(1,4) * 100
        if solution>removed and after_salt_per%k==0:
            break
    salt = (after_salt_per * (solution - removed))//100
    salt = salt // k
    ans = "%d%%"%salt
    str1 = "무게가 %dg이고 농도가 x%%인 소금물이 증발하여 %dg이 되었습니다."%(solution,solution - removed)
    str2 = "증발한 후의 소금물의 농도가 %d%%일떄 처음 소금물의 농도를 구하시오"%(after_salt_per)
    str3 = str1 + " " + str2
    while True:
        input_ans = input("%d. %s\n"%(i,str3))
        if input_ans == ans:
            break

def q10(i): # 소금물 2
    while True:
        after_salt_per = random.randint(5,20)
        solution = 1000
        after_salt = after_salt_per * solution // 100
        solution_a = random.randint(1,9) * 100
        if solution_a <= after_salt:
            continue    
        solution_b = solution - solution_a
        salt_a = random.randint(30,after_salt)
        salt_b = after_salt - salt_a
        salt_a_per = salt_a  * 100 // solution_a
        salt_b_per = salt_b  * 100 // solution_b
        if (salt_a * 100) % solution_a == 0 and (salt_b * 100) % solution_b == 0:
            break
    str1 = "%d%%의 소금물 %dg과"%(salt_a_per, solution_a)
    str2 = "%d%%의 소금물 %dg을 섞어서"%(salt_b_per, solution_b)
    str3 = "만든 소금물의 농도는 몇퍼센트인지 구하시오."
    str4 = str1 + " " + str2 + " " + str3
    ans = "%d%%"%(after_salt_per)
    while True:
        input_ans = input("%d. %s\n"%(i,str4))
        if input_ans == ans:
            break

def time_convert(s):
    h = s // 3600; s = s - h * 3600
    m = s // 60; s = s - m * 60
    return h,m,s

def day_caculate(day2_h, h):
    clock_h = day2_h + h
    if clock_h >= 24:
        clock_h -= 24
    return clock_h

def q12(i): #시간 느려지는 문제
    month = 10
    while True:
        day1 = random.randint(1,31)
        day2 = random.randint(1,31)
        if day1<day2:
            break
    during_time = (day2 - day1) * 24
    day1_h = random.randint(1,23)
    day2_h = random.randint(1,23)
    during_hour = day2_h - day1_h
    delay = random.randint(5,20)
    during = during_hour + during_time
    addition = delay * during
    h,m,s = time_convert(addition)
    clock_h = day_caculate(day2_h, h)
    ans = "%d시 %d분 %d초"%(clock_h,m,s)
    while True:
        input_ans = input("%d. 한시간에 %d초 빨라지는 시계가 있습니다. %d월 %d일 %d시에 이 시계를 정확히 맞췄다면, %d월 %d일 %d시에 이 시계는 몇시 몇분 몇초를 가리키고 있는지 답하시오.(에.10시 10분 10초)\n"%(i, delay,month,day1,day1_h,month,day2,day2_h))
        if input_ans == ans:
            break

def q13(i): #시간 소수로 변경
    h = random.randint(1,9)
    while True:
        m = random.randint(1,60)
        if math.gcd(m,60) % 3 == 0:
            break
    gcd_num = math.gcd(m,60)
    ans = "%d시 %d분"%(h, m)
    m //= gcd_num; b = 60 // gcd_num
    if m*100//b<10:
        while True:
            input_ans = input("%d. 주어진 소수를 시간으로 쓰시오(예. 1.5 = 1시 30분)\n%d.0%d = "%(i, h, m*100//b))
            if input_ans == ans:
                break
    else:
        while True:
            input_ans = input("%d. 주어진 소수를 시간으로 쓰시오(예. 1.5 = 1시 30분)\n%d.%d = "%(i, h, m*100//b))
            if input_ans == ans:
                break

def q14(i): # 평균 3
    while True:
        total = random.randint(200,500)
        div = random.randint(15,30)
        case1 = total // div
        case2 = case1 + 1
        mod1 = total % case1; mod2 = div * case2 - total; mod3 = total % case2
        total = case1 * div + mod1
        if mod1 != 0 and mod2 != 0:
            break
    question_str1 = "학생들에게 초콜릿을 %d개 나눠주면 %d개가 남고, %d개 나눠주면 %d개가 부족합니다. 초콜릿은 몇개입니까?"%(case1, mod1, case2, mod2)
    question_str2 = "학생들이 %d대 버스에 타면 %d자리가 남고, %d대 버스에 타면 %d명이 타지 못합니다. 한 버스에 가능한 많은 학생 수가 탈 때 전체 학생수는 몇명입니까?"%(case2, mod2, case1, mod1)
    question_str3 = "정해진 기간 동안 책 한권을 하루에 %d장씩 읽으면 %d장이 남고, %d장씩 읽으면 마지막 날에는 %d장만 읽습니다. 책은 총 몇장입니까?"%(case1, mod1, case2, mod3)
    question_str4 = "이번에 수확한 고구마를 한 상자에 %d개 씩 담으면 %d개가 남고, %d개에 담으면 %d개가 부족합니다. 고구마는 총 몇 개 입니까?"%(case1, mod1, case2, mod2)
    question_str5 = "크기가 같은 컵 %d개에 음료수를 담으면 %dml가 남고, 컵 %d개 씩 담으면 마지막 컵에는 %dml만 담습니다. 음료수는 총 ml입니까?"%(case1, mod1, case2, mod2)
    q = [question_str1, question_str2, question_str3, question_str4, question_str5]
    qnum = random.randint(0,4)
    ans = "%d"%total
    while True:
        input_ans = input("%d. %s(이 문제는 단위 쓰지 말것)\n"%(i,q[qnum]))
        if input_ans == ans:
            break

def q15(i): #원 둘레 넓이 문제
    iidx = random.randint(0,1)
    r = random.randint(5,15)
    idx = random.randint(0,1)
    type_of_square = [0,1]
    if iidx%2 == 0:
        if type_of_square[idx]==0:
            str1="한 대각선의 길이가 %d인 정사각형을 둘러싼 원의 둘레를 구하시오."%(2*r)
            ans = 2*r*3.14
        else:
            str1="원을 둘러싼 정사각형의 한 변의 길이가 %d일 때 원의 둘레를 구하시오."%(2*r)
            ans = 2*r*3.14
    else:
        if type_of_square[idx]==0:
            str1="한 대각선의 길이가 %d인 정사각형을 둘러싼 원의 넓이를 구하시오."%(2*r)
            ans = r*r*3.14
        else:
            str1="원을 둘러싼 정사각형의 한 변의 길이가 %d일 때 원의 넓이를 구하시오."%(2*r)
            ans = r*r*3.14
    ans = "%.2f"%ans
    while True:
        input_ans = input("%d. %s(원주율은 3.14)\n"%(i,str1))
        if input_ans == ans:
            break

def q16(i): #음수연산
    while True:
        a = random.choice([x for x in range(-99, 100) if x != 0])
        b = random.choice([x for x in range(-99, 100) if x != 0])
        c = random.choice([x for x in range(-99, 100) if x != 0])
        if a>0 and b>0 and c>0 and a==b and b==c and c==a:
            continue
        else:
            break
    ans = a + b + c
    str_b = "+%d"%b if b>0 else "-%d"%abs(b)
    str_c = "+%d"%c if c>0 else "-%d"%abs(c)
    str1 = "%d"%a+str_b+str_c+"="
    ans = "%d"%ans
    while True:
        input_ans = input("%d. %s\n"%(i, str1))
        if input_ans == ans:
            break

def interest_compute(money, interest_per, years):
    for _ in range(years):
        interest_per_pow = pow((1000+interest_per), years)
        ten_pow = pow(1000, years)
        saving = (money * interest_per_pow) // ten_pow
    return saving

def q17(i): #이자문제
    money = random.randint(1,9) * 100000000
    interest_per = random.randint(11,29)
    interest_per_1 = interest_per//10; interest_per_0 = interest_per%10
    years = random.randint(1,2)
    saving = interest_compute(money, interest_per, years)
    str1 = "담임선생님은 재산의 %d원을 은행에 저금했습니다."%money
    str2 = "매년 이자율이 %d.%d%%일때 %d년 후에 저금 되어 있는 돈은 얼마입니까?"%(interest_per_1, interest_per_0, years)
    str3 = str1+ " " + str2
    ans = "%d원"%saving
    while True:
        input_ans = input("%d. %s\n"%(i, str3))
        if input_ans == ans:
            break

def q18(i): #일차방정식
    a = random.randint(5,20)
    b = random.randint(5,100)
    c = random.randint(5,100)
    if b>c: b,c=c,b
    over_x = c - b; under_x = a
    div = math.gcd(over_x,under_x)
    over_x//=div;under_x//=div
    if under_x == 1:
        ans = "x = %d"%over_x
    else:
        ans = "x = %d/%d"%(over_x,under_x)
    while True:
        input_ans = input("%d. %dx + %d = %d(예.x = 1/2, 띄어쓰기 잘못하면 틀린것으로 채점됨)\n"%(i,a,b,c))
        if input_ans == ans:
            break

def surface(row, col, height):
    return 2 * (row * col + col * height + height * row)
def volume(row, col, height):
    return row * col * height

def q19(i): #입체도형 연산
    while True:
        row = random.randint(5,50)
        col = random.randint(5,50)
        height = random.randint(5,50)
        if row == col and col == height:
            continue
        else:
            break
    type_idx = random.randint(0,3)
    if type_idx==0:
        surf = surface(row,col,height)
        str1 = "직육면체 가로가 %dcm, 세로가 %dcm, 높이가 %dcm일 때 겉넓이를 구하시오."%(row,col,height)
        ans = "%dcm2"%surf
    elif type_idx==1:
        surf = surface(row,col,height)
        str1 = "겉넓이가 %dcm2인 직육면체의 가로가 %dcm, 세로가 %dcm일 때 높이를 구하시오."%(surf,row,col)
        ans = "%dcm"%height
    elif type_idx==2:
        vol = volume(row,col,height)
        str1 = "직육면체 가로가 %dcm, 세로가 %dcm, 높이가 %dcm일 때 부피를 구하시오."%(row,col,height)
        ans = "%dcm3"%vol
    elif type_idx==3:
        vol = volume(row,col,height)
        str1 = "부피가 %dcm2인 직육면체의 가로가 %dcm, 세로가 %dcm일 때 높이를 구하시오."%(vol,row,col)
        ans = "%dcm"%height
    while True:
        input_ans = input("%d. %s(단위 정확히 쓸 것. 제곱은 cm2, 세제곱은 cm3)\n"%(i,str1))
        if input_ans == ans:
            break

def col_space(n):
    return n + 2
def col_point(n):
    return n * 2
def col_side(n):
    return n * 3
def py_space(n):
    return n + 1
def py_point(n):
    return n + 1
def py_side(n):
    return n * 2

def q20(i): #입체도형 각변면
    col = [col_space, col_point, col_side]
    py = [py_space, py_point, py_side]
    fig_type = [col, py]
    fig_type_kor = ["기둥", "뿔"]
    que_type_kor = ["면", "꼭짓점", "모서리"]
    while True:
        type_a = random.randint(0,1)
        type_b = random.randint(0,1)
        qu_a = random.randint(0,2)
        qu_b = random.randint(0,2)
        if type_a != type_b or qu_a != qu_b:
            break
    a = random.randint(3,25)
    A = fig_type[type_a][qu_a](a)
    B = fig_type[type_b][qu_b](a)
    Qa = "어떤 각%s의 %s의 수"%(fig_type_kor[type_a],que_type_kor[qu_a])
    Qb = "밑면의 각의 개수가 같은 각%s의 %s의 수"%(fig_type_kor[type_b],que_type_kor[qu_b])
    Qc = "의 합이 %d일 때 이 입체도형 밑면의 각 개수를 구하시오."%(A+B)
    Q = Qa + "와 " + Qb + Qc
    ans = "%d개"%a
    while True:
        input_ans = input("%d. %s\n"%(i, Q))
        if input_ans == ans:
            break
title = "*문제 생성기! V1.0.0 현재 등록된 문제 유형은 19가지입니다.*"
print(title)
print()
for i in range(1,101):
    q = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q12,q13,q14,q15,q16,q17,q18,q19,q20]
    random.choice(q)(i)
    print()