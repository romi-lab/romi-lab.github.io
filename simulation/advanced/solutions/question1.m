clc; clear;
close all;

% comment the next line if using Matlab
% pkg load control;

% show the Laplace transformation
s = tf('s');
sys = s/((s^2+4)*(s^2+2*s+10))

% compute the partial fraction decomposition
num = [1, 0];
den = [1, 2, 14, 8, 40];
[r, p, k] = residue(num, den)
