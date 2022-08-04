function dv = dynamics(t, v, f)

    m = 1;
    c = 2;

    dv = -c/m*v + f;

end