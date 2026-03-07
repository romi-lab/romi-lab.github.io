import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────────────────────────────────────
def poly_to_str(coeffs):
    """Convert a coefficient list to a human-readable polynomial string."""
    degree = len(coeffs) - 1
    terms  = []
    for i, c in enumerate(coeffs):
        power = degree - i
        c_str = str(c) if c == int(c) else f"{c:.4g}"
        if   power == 0: terms.append(c_str)
        elif power == 1: terms.append(f"{c_str}s")
        else:            terms.append(f"{c_str}s^{power}")
    return " + ".join(terms)


# ─────────────────────────────────────────────────────────────────────────────
def compute_step_response(coeffs, t_end=20, num_points=2000):
    """
    Compute the unit step response of a system.

    Transfer function:
        G(s) = 1 / (coeffs[0]*s^n + ... + coeffs[-1])

    Args:
        coeffs     (list) : Denominator coefficients, highest degree first.
                            e.g. [1, 6, 11, 6]  →  s³ + 6s² + 11s + 6
        t_end      (float): Simulation end time.
        num_points (int)  : Number of time samples.

    Returns:
        t (ndarray): Time vector.
        y (ndarray): Step response values.
        sys (TransferFunction): The scipy transfer function object.
    """
    # ToDo: build your control plant via the given list
    denominator = None
    numerator   = None
    tf_sys = None

    # ToDo: obtain the step response of the system
    t = None
    t, y = None, None

    if t == None:
        print("please check and finish the above ToDo parts !")
        exit()

    return t, y, tf_sys


# ─────────────────────────────────────────────────────────────────────────────
def analyse_step_response(t, y, is_stable):
    """
    Compute common time-domain performance metrics for a step response.

    Returns:
        dict with keys: steady_state, rise_time, peak_value,
                        overshoot_pct, settling_time
    """
    metrics = {}
    if not is_stable:
        return metrics

    ss = y[-1]
    metrics["steady_state"] = ss

    # Rise time: 10 % → 90 %
    try:
        t10 = t[np.where(y >= 0.1 * ss)[0][0]]
        t90 = t[np.where(y >= 0.9 * ss)[0][0]]
        metrics["rise_time"] = t90 - t10
    except IndexError:
        metrics["rise_time"] = None

    # Peak value & overshoot
    peak = float(np.max(y))
    metrics["peak_value"]    = peak
    metrics["overshoot_pct"] = (peak - ss) / ss * 100 if ss != 0 else 0.0

    # Settling time (2 % criterion)
    try:
        outside = np.where(np.abs(y - ss) > 0.02 * abs(ss))[0]
        metrics["settling_time"] = float(t[outside[-1]]) if len(outside) > 0 else 0.0
    except Exception:
        metrics["settling_time"] = None

    return metrics


# ─────────────────────────────────────────────────────────────────────────────
def print_step_response(coeffs, desc=""):
    """
    Compute, print, and plot the step response for a system
    defined by its characteristic-polynomial denominator coefficients.
    """
    if desc:
        print(f"\n  [{desc}]")

    # ── System definition ────────────────────────────────────────────────────
    num_str = "1"
    den_str = poly_to_str(coeffs)

    print("=" * 62)
    print(f"  Transfer Function:  G(s) = {num_str} / ({den_str})")
    print("=" * 62)

    # ── Step response ────────────────────────────────────────────────────────
    poles     = np.roots(coeffs)
    is_stable = bool(np.all(np.real(poles) < 0))

    t, y, _ = compute_step_response(coeffs)
    metrics  = analyse_step_response(t, y, is_stable)

    if metrics:
        print("\n  Step Response Metrics:")
        print(f"    Steady-state value : {metrics['steady_state']:.4f}")
        if metrics.get("rise_time") is not None:
            print(f"    Rise time (10~90%) : {metrics['rise_time']:.4f} s")
        print(f"    Peak value         : {metrics['peak_value']:.4f}")
        print(f"    Overshoot          : {metrics['overshoot_pct']:.2f} %")
        if metrics.get("settling_time") is not None:
            print(f"    Settling time (2%) : {metrics['settling_time']:.4f} s")

    # ── Plot ─────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(t, y, color="royalblue", linewidth=2, label="Step response y(t)")

    if is_stable and metrics:
        ss = metrics["steady_state"]
        ax.axhline(ss, color="tomato", linestyle="--", linewidth=1.2,
                   label=f"Steady state = {ss:.4f}")

        # 2 % settling band
        ax.axhline(ss * 1.02, color="green", linestyle=":", linewidth=0.9, alpha=0.7,
                   label="±2 % band")
        ax.axhline(ss * 0.98, color="green", linestyle=":", linewidth=0.9, alpha=0.7)

    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_ylabel("Amplitude",  fontsize=12)
    ax.set_title(f"Unit Step Response\n"
                 f"G(s) = {num_str} / ({den_str})", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    plt.show()

    return t, y


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ([5, 4, 3, 2, 1], "Fourth-order system"),
        ([1, 6, 11, 6],   "Stable third-order system"),
        ([1, 1, 2, 8],    "Unstable third-order system"),
    ]

    for coeffs, desc in test_cases:
        print_step_response(coeffs, desc)