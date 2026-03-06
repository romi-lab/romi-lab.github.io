import control
import numpy as np
import matplotlib.pyplot as plt

# ToDo Model your control plant
G = None

# ToDo: design your controller
Parameter_A, Parameter_B, Parameter_C = None, None, None
C = None

# ToDo: Closed-loop transfer function
T = None

# Step response
t = np.linspace(0, 15, 3000)
t_out, y_out = control.step_response(T, T=t)

# Performance metrics
y_ss     = float(np.mean(y_out[-200:]))
OS       = (np.max(y_out) - y_ss) / y_ss * 100
idx10    = np.argmax(y_out >= 0.1 * y_ss)
idx90    = np.argmax(y_out >= 0.9 * y_ss)
t_rise   = float(t_out[idx90] - t_out[idx10])
outside  = np.where(np.abs(y_out - y_ss) > 0.02 * y_ss)[0]
t_settle = float(t_out[outside[-1]]) if len(outside) else 0.0

# Plot
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t_out, y_out, 'steelblue', linewidth=2.2,
        label=f'PID  Parameter_A={Parameter_A}, Parameter_B={Parameter_B}, Parameter_C={Parameter_C}')
ax.axhline(1.0,  color='k',    linestyle='--', linewidth=1.0, label='Reference = 1')
ax.axhline(1.02, color='gray', linestyle=':',  linewidth=0.9)
ax.axhline(0.98, color='gray', linestyle=':',  linewidth=0.9, label='±2% band')

ax.set_title(f'Unit Step Response\n'
             f'Overshoot={OS:.1f}%   Rise Time={t_rise:.3f}s   Settling Time={t_settle:.3f}s',
             fontsize=12)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Output')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.35)
ax.set_ylim(-0.05, 1.6)
plt.tight_layout()
plt.savefig('pid_step.png', dpi=150)
plt.show()

print(f"\n  Parameter_A = {Parameter_A},  Parameter_B = {Parameter_B},  Parameter_C = {Parameter_C}")
print(f"  Overshoot    : {OS:.2f} %")
print(f"  Rise Time    : {t_rise:.3f} s")
print(f"  Settling Time: {t_settle:.3f} s")