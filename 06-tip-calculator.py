#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Wellcome to the tip caculator!")
# input số tiền trả
total_bill = float(input("What was the total bill? $"))
# input số tiền tip
tip_bill = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
# input số người chia đơn
split_bill = int(input ("How many people to split the bill? "))
# tính toán kết quả cuối
result = (total_bill / split_bill) * (1 + tip_bill)
# hiển thị kết quả
print("Each person should pay: $" + str(round(result,2)))

# result_round = "{:.2f}".format(result)
