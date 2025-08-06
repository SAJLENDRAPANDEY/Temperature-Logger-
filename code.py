project 2 ---> Temperature Logger
temps=[]
for i in range(7):
    temp=float(input(f"Day{i+1} enter temperature :"))
    temps.append(temp)

# average of 7 days temperature 
avg_temp=sum(temps)//len(temps)
# max day temperatur
max_temp=max(temps)
# min temperature in a week 
min_temp=min(temps)
# which day temperature is max /min
max_day = temps.index(max_temp) + 1
min_day = temps.index(min_temp) + 1

print("\n--- Temperature Report ---")
print(f"Average Temperature: {avg_temp:.2f}")
print(f"Maximum Temperature: {max_temp} (Day {max_day})")
print(f"Minimum Temperature: {min_temp} (Day {min_day})")
