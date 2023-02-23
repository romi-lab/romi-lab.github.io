clc; clear;
close all;

t = 0:0.001:5;
f = 1;
v0 = 1;

options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);
[~, v] = ode45(@(t, v)dynamics(t, v, f), t, v0, options);
    
figure(1)
plot(t, v);
xlabel('t'); ylabel('Linear velocity');
