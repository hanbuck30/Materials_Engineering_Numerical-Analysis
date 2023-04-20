import numpy as np
import matplotlib.pyplot as plt

# 입력값 설정
Vf = 0.5 # 섬유의 분율
sigma_f = 400 # 섬유의 인장강도 (Fiber tensile strength)
sigma_m = 50 # 매트릭스 수지의 인장강도(Matrix tensile strength)
eta_0_list = [1.0, 0, 0.5, 3/8, 0.2] # 섬유배향계수(일방향배향 : 1.0, 직각방향 : 0, 직교배향 : 0.5, 2차원 random 배향 : 3/8, 3차원 random 배향 : 0.2)
Lc = 10 # 섬유 임계 길이 (Fiber critical length)

# 섬유 길이 범위 설정
L_range = np.linspace(1, 100, 99) # 1 ~ 100 범위 내에서 99개의 데이터 생성

# 그래프 그리기


plt.figure(figsize=(7,7)) 
for i, eta_0 in enumerate(eta_0_list):
    # 섬유길이계수 설정
    eta_L = np.zeros(len(L_range))
    for j in range(len(L_range)):
        if L_range[j] >= Lc :
            eta_L[j] = 1 - Lc / (2 * L_range[j])
        else :
            eta_L[j] = L_range[j] / (2 * Lc)
    sigma_comp = eta_0 * eta_L * sigma_f * Vf + sigma_m * (1 - Vf)
    if i ==0:
        plt.plot(L_range,sigma_comp, color='limegreen' ,label ="일방향배향 : 1.0") 
    elif i ==1:
        plt.plot(L_range,sigma_comp, color='violet',label ="직각방향 : 0") 
    elif i ==2:
        plt.plot(L_range,sigma_comp, color='dodgerblue',label ="직교배향 : 0.5") 
    elif i ==3:
        plt.plot(L_range,sigma_comp,'r',label ="2차원 random 배향 : 3/8") 
    elif i ==4:
        plt.plot(L_range,sigma_comp,'b',label ="3차원 random 배향 : 0.2")   
plt.legend(loc=(0.85,0.85))
plt.xlabel('Fiber length')
plt.ylabel('Tensile strength (MPa)')       
plt.title('앙 기모띠')
plt.ylim(0,250)

plt.show()