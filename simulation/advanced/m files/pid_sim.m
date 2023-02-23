close all;
clear; clc;

% uncomment the following line if you are using Octave.
% pkg load control

%% parameters
dt = 0.001;   % sampling period

% initial values
u_1 = 0.0;    % u(k-1)
u_2 = 0.0;    % u(k-2)
u_3 = 0.0;    % u(k-3)

x_1 = 0.0;    % x(k-1)
x_2 = 0.0;    % x(k-2)
x_3 = 0.0;    % x(k-3)

e_curr = 0; % current error
e_last = 0; % last error
e_sum = 0;  % interation
e_diff = 0; % differential

% gain parameters
kp = 0.5;
ki = 0.001;
kd = 0.001; 

%% system discretization
sys = tf(5.235e005,[1,87.35,1.047e004,0]);
dsys = c2d(sys,dt,'z');
[num,den] = tfdata(dsys,'v');
n = size(num, 2);
num = num(n-2:n);

for k=1:1:2000
time(k)=k*dt;
   
% controller
u(k) = kp*e_curr + ki*e_sum + kd*e_diff;

%Linear model
x(k)=-den(2)*x_1-den(3)*x_2-den(4)*x_3+num(1)*u_1+num(2)*u_2+num(3)*u_3;

% data recording
xd(k) = 1;  % step singal
error(k) = xd(k)-x(k);

% update
e_last = e_curr;
e_curr = error(k);
e_sum = e_sum + e_curr*dt;
e_diff = (e_curr - e_last)/dt;

u_3 = u_2; u_2 = u_1; u_1 = u(k);
x_3 = x_2; x_2 = x_1; x_1 = x(k);

end

%% plot data
figure(1);
plot(time,xd,'r',time,x,'k','linewidth',1);
xlabel('time(s)');ylabel('xd,x');
legend('Ideal position signal','Position tracking');
