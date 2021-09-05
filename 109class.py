import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go 

dice_result  = []
count = []
for i in range(0,1000):
  dice1 = random.randint(1,6)

  dice2 = random.randint(1,6)
  dice_result.append(dice1+dice2)
  mean = sum(dice_result)/len(dice_result)

print(mean)

standard_deviation  = statistics.stdev(dice_result)
print(standard_deviation)

median = statistics.median(dice_result)
print(median)

mode = statistics.mode(dice_result)
print(mode)

fig = ff.create_distplot([dice_result],["result"],show_hist = False)
fig.show()

first_standard_deviation_start,first_standard_deviation_end = mean-standard_deviation,mean+standard_deviation
second_standard_deviation_start,second_standard_deviation_end = mean-(2*standard_deviation),mean+(2*standard_deviation)
third_standard_deviation_start,third_standard_deviation_end = mean-(3*standard_deviation),mean+(3*standard_deviation)
fig.add_trace(go.Scatter(
    x = [mean,mean],  y = [0,0.17],mode = "lines",name = "mean"
))

fig.add_trace(go.Scatter(
    x = [first_standard_deviation_start,first_standard_deviation_start],  y = [0,0.17],mode = "lines",name = "mean"
))

fig.add_trace(go.Scatter(
    x = [first_standard_deviation_end,first_standard_deviation_end],  y = [0,0.17],mode = "lines",name = "mean"
))



fig.add_trace(go.Scatter(
    x = [second_standard_deviation_start,second_standard_deviation_start],  y = [0,0.17],mode = "lines",name = "mean"
))

fig.add_trace(go.Scatter(
    x = [second_standard_deviation_end,second_standard_deviation_end],  y = [0,0.17],mode = "lines",name = "mean"
))


fig.add_trace(go.Scatter(
    x = [third_standard_deviation_start,third_standard_deviation_start],  y = [0,0.17],mode = "lines",name = "mean"
))

fig.add_trace(go.Scatter(
    x = [third_standard_deviation_end,third_standard_deviation_end],  y = [0,0.17],mode = "lines",name = "mean"
))


list_of_data_first_standard_deviation = [result for result in dice_result if result>first_standard_deviation_start and result<first_standard_deviation_end ]
list_of_data_second_standard_deviation = [result for result in dice_result if result>second_standard_deviation_start and result<second_standard_deviation_end ]
list_of_data_third_standard_deviation = [result for result in dice_result if result>third_standard_deviation_start and result<third_standard_deviation_end ]
print("mean of the data is {}".format(mean))
print("median of the data is {}".format(median))
print("mode of the data is {}".format(mode))
print("standard deviation of the data is {}".format(standard_deviation))

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_second_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_third_standard_deviation)*100.0/len(dice_result)))





  


