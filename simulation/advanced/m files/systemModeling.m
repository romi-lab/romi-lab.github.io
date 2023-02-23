%uncomment the next line if you are using Octave
%pkg load control;

s = tf('s');
sys = 4/(s^3+2*s^2+3*s+4)

num = [1, -3];
den = [1, 3];
sys = tf(num, den)

num = [2, 5, 3, 6];
den = [1, 6, 11, 6];
[r, p, k] = residue(num, den)

r = [-6, -4, 3];
p = [-3, -2, -1];
k = 2;
[num, den] = residue(r, p, k)
sys = tf(num, den)

s = tf('s');
G = 4/(s^3+2*s^2+3*s+4);
G_c = (s-3)/(s+3);
H = 1/(0.01*s+1);

sys1 = series(G, G_c);
sys = feedback(sys1, H)
