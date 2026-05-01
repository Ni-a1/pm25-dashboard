data=readtable('delhi_pm25_aqi.csv');
pm25=data.value
time=data.Time;
time = datetime(time,'InputFormat','yyyy-MM-dd''T''HH:mm:ssX','TimeZone','UTC');
time.TimeZone='UTC'
close all
figure
subplot(2,1,1)
plot(time,pm25);
title('PM 2.5 REAL DATA ');
ylabel('PM2.5')
xlabel('Time')
grid on

t_num=1:length(time);
X=[pm25(1:end-1),t_num(1:end-1)']
Y=pm25(2:end);
model = fitrtree(X, Y);
Y_pred = predict(model, X);
subplot(2,1,2)
cla reset
t_plot=time(2:end)
plot(t_plot, Y,'y')
hold on
plot(t_plot, Y_pred,'r')
legend('Actual','Predicted')
title('PM2.5 Prediction')
xlabel('Time')
ylabel('PM2.5')
grid on
mse = mean((abs(Y - Y_pred)).^2);
disp(['MSE: ', num2str(mse)])
result=table(t_plot,Y,Y_pred)
writetable(result, 'pm25_results.csv');
