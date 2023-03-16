close all;
clear;

% System function
G = tf(5,[1, 5, 0]);
% PID controller
G_c = tf([0, 0.5, 0.0], [1, 0]);

sys1 = series(G, G_c);
% Closed-loop system
sys2 = feedback(sys1, 1)

t = 0:0.01:30;
[y, t] = step(sys2, t);

plot(t, ones(size(t)), 'Color', 'r', 'LineWidth', 1)
hold on;
plot(t, y, 'Color', 'k', 'LineWidth', 1)
xlabel('time (s)')
legend('Reference', 'Control result', 'Location', 'southeast')
