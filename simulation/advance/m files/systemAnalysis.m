% uncomment the next line if you are using Octave
%pkg load control;

s = tf('s');
sys = 1/(s^2+0.6*s+1);

t = 0:0.001:30;
[ y, t] = step(sys, t);
figure(1);
plot(t, y);
xlabel('t(s)'); ylabel('y');
stepinfo(y, t) % not available in Octave

[y, t] = impulse(sys, t);
figure(2);
plot(t, y);
xlabel('t(s)'); ylabel('y');

[y, t] = lsim(sys, sin(t), t);
figure(3);
plot(t, y);
xlabel('t(s)'); ylabel('y');

den = [1, 0.6, 1];
roots(den)

G = 1/(s^2+0.6*s+1);
pole(G)
figure(4);
pzmap(G);
axis([-0.4, 0, -1, 1]);
