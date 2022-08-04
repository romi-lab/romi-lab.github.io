clc; clear;
close all;

% comment the next line if you are using Matlab
pkg load signal;

t = 0:0.001:20;
%% transfer function
s = tf('s');
G = 16/(s^2+3*s+16);

%% step response
[y1, t] = step(G, t);

figure(1);
plot(t, y1);
xlabel('t(s)'); ylabel('y');
title('Step Response');

%% impulse response
[y2, t] = impulse(G, t);

figure(2)
plot(t, y2);
xlabel('t(s)'); ylabel('y');
title('Impulse Response');

%% square wave response
f = square(2*pi*t/8);
[y3, t] = lsim(G, f, t);

figure(3)
plot(t, f);
xlabel('t(s)'); ylabel('f');
title('Square Wave');

figure(4)
plot(t, y3);
xlabel('t(s)'); ylabel('y');
title('Square Wave Response');
