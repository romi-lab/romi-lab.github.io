% time span
t = 0:0.001:20;

% initial conditions
x0 = [0, 0];
f = 1;

% simulation
options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);
[t, x] = ode45(@(t, x)dynamics_q4(t, x, f), t, x0, options);

% plotting
figure(1)
plot(t, x(:, 1));
xlabel('t(s)'); ylabel('Linear velocity');
