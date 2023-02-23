clc; clear;
close all;

% comment the next line if using Matlab
pkg load control;

% show the Laplace transformation
s = tf('s');
sys = 2/(s^3*(s^2+2*s+10))

% compute the partial fraction decomposition
num = [2];
den = [1, 2, 10, 0, 0, 0];
[r, p, k] = residue(num, den)
