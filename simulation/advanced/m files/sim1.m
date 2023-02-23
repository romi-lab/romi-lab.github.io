clc; clear;
close all;

%% Usage in Octave
% Uncomment the next line to use in Octave
%pkg load control;

%% Calculate transfer function
s = tf('s');

sys1 = 20/((s+1)*(s+4));
h1 = 0.4490;

G1 = feedback(sys1, h1, -1);
sys2 = 1/s;
G2 = series(G1, sys2);

h2 = 1;
G = feedback(G2, h2, -1)

%% Time responses
t = 0:0.001:10;

[y1, t] = step(G, t);
stepinfo(G) % not available in Octave

[y2, t] = impulse(G, t);

[y3, t] = lsim(G, sin(t), t);

%% Stability analysis
p = pole(G)

%% Plotting
figure(1)
plot(t, y1);
xlabel('t(s)'); ylabel('y');
title('Step Response');

figure(2)
plot(t, y2);
xlabel('t(s)'); ylabel('y');
title('Impulse Response');

figure(3)
plot(t, y3);
xlabel('t(s)'); ylabel('y');
title('Time Response with sin(t) Input');

figure(4)
pzmap(G);
