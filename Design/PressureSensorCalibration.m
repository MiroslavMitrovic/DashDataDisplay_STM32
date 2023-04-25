
%Pressure Sensor mapping script 


p = [0, 1, 1.5, 2. 2.5, 3, 3.5, 4, 4.5, 5 ,5.5]; %pressure in [bar]

R = [21.1, 27.5, 37.5, 47.5, 60.5, 70, 83.5, 90, 100, 106.5, 123 ]; % Resistance in [Ohm]

n = 1; %Degree of polynomial

fit = polyfit(p, R, n);

k = fit(1,1);
n = fit(1,2);

Rcorrected = k .*p + n;

figure(1)
hold on 
plot(p,R,'-r');
plot(p,Rcorrected,'-c');