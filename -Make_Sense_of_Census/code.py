# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#Step 1

path="subset_1000.csv"
#print(data)
#print(type(data))
census=np.concatenate((new_record,data))
#print(data)
#print(census)

#Step 2

max_age=np.max(census[:,0])
print("max_age : ",max_age)
min_age=np.min(census[:,0])
print("min_age : ",min_age)
age_mean=np.mean(census[:,0])
print("age_mean : ",age_mean)
age_std=np.std(census[:,0])
print("age_std : ",age_std)

#Step 3
race=census[:,2]
race0=race==0
race_0=race0.astype(int)
race1=race==1
race_1=race1.astype(int)
race2=race==2
race_2=race2.astype(int)
race3=race==3
race_3=race3.astype(int)
race4=race==4
race_4=race0.astype(int)
print("race_0 : ",race_0)
print("race_1 : ",race_1)
print("race_2 : ",race_2)
print("race_3 : ",race_3)
print("race_4 : ",race_4)


len_0 = np.count_nonzero(race0)
len_1 = np.count_nonzero(race1)
len_2 = np.count_nonzero(race2)
len_3 = np.count_nonzero(race3)
len_4 = np.count_nonzero(race4)
print("len_0 : ",len_0)
print("len_1 : ",len_1)
print("len_2 : ",len_2)
print("len_3 : ",len_3)
print("len_4 : ",len_4)


if len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4 :
    minority_race=0
    print("minority_race : ",minority_race)
elif len_1 < len_0 and len_1 < len_2 and len_1 < len_3 and len_1 < len_4 :
    minority_race=1
    print("minority_race : ",minority_race)
elif len_2 < len_0 and len_2 < len_1 and len_2 < len_3 and len_2 < len_4 :
    minority_race=2
    print("minority_race : ",minority_race)
elif len_3 < len_0 and len_3 < len_1 and len_3 < len_2 and len_3 < len_4 :
    minority_race=3
    print("minority_race : ",minority_race)
elif len_4 < len_0 and len_4 < len_1 and len_4 < len_2 and len_4 < len_2 :
    minority_race=4
    print("minority_race : ",minority_race)
else:
    minority_race=5
    print("minority_race : ",minority_race)

#step_4

senior_citizens=census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print("working_hours_sum : ",working_hours_sum)
print("avg_working_hours : ",avg_working_hours)

#step5
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print("avg_pay_high : ",avg_pay_high)
print("avg_pay_low : ",avg_pay_low)


