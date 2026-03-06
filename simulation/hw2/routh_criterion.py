def routh_hurwitz(coeffs):
    """
    Determine the stability of a linear system using the Routh-Hurwitz criterion.

    Args:
        coeffs (list): Coefficients of the characteristic polynomial, from highest
                       to lowest degree.
                       e.g. [5, 4, 3, 2, 1] represents 5s^4 + 4s^3 + 3s^2 + 2s + 1

    Returns:
        dict: A dictionary containing the analysis results:
              - is_stable     (bool): Whether the system is stable
              - routh_table   (list): The complete Routh array
              - first_column  (list): The first column of the Routh array
              - sign_changes  (int) : Number of sign changes (i.e. RHP poles count)
              - info          (str) : Detailed analysis message
    """
    n = len(coeffs)

    if n == 0:
        return {"is_stable": False, "info": "Error: coefficient list is empty"}

    # ── Necessary condition check: all coefficients must be positive ──────────
    if any(c < 0 for c in coeffs):
        neg = [c for c in coeffs if c < 0]
        return {
            "is_stable": False, "routh_table": [], "first_column": [],
            "sign_changes": -1,
            "info": f"Necessary condition not met: negative coefficient(s) found {neg}, "
                    f"system is necessarily unstable"
        }
    if any(c == 0 for c in coeffs):
        return {
            "is_stable": False, "routh_table": [], "first_column": [],
            "sign_changes": -1,
            "info": "Necessary condition not met: zero coefficient(s) found, "
                    "system is marginally stable or unstable"
        }

    if n == 1:
        return {
            "is_stable": True,
            "routh_table": [[float(coeffs[0])]],
            "first_column": [float(coeffs[0])],
            "sign_changes": 0,
            "info": "Zero-order system, stable"
        }

    degree = n - 1
    cols   = (n + 1) // 2
    EPSILON = 1e-10       # Small value used to replace a zero in the first column
    info_msgs = []

    # ToDo:  ── Build the first two rows of the Routh array ───────────────────────────
    row1 = [float(x) for x in coeffs[0::2]]   # Even-indexed coefficients
    row2 = [float(x) for x in coeffs[1::2]]   # Odd-indexed coefficients
    while len(row1) < cols: row1.append(0.0)
    while len(row2) < cols: row2.append(0.0)

    routh = [row1, row2]

    # ToDo:  ── Compute remaining rows iteratively ───────────────────────────────────
    for i in range(2, n):

        pass

    # ToDo:  ── Analyse sign changes in the first column ──────────────────────────────
    first_col    = [row[0] for row in routh]
    sign_changes = 0
    prev_sign    = None

    for val in first_col:

        pass

    is_stable = (sign_changes == 0)

    if is_stable:
        info_msgs.append(
            "System is stable: all first-column elements are positive, no sign changes"
        )
    else:
        info_msgs.append(
            f"System is unstable: {sign_changes} sign change(s) detected in the first column, "
            f"number of RHP poles = {sign_changes}"
        )

    return {
        "is_stable":    is_stable,
        "routh_table":  routh,
        "first_column": first_col,
        "sign_changes": sign_changes,
        "info":         "; ".join(info_msgs)
    }


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



def print_routh_result(coeffs):
    """Print the complete Routh-Hurwitz stability analysis for a given system."""
    result = routh_hurwitz(coeffs)
    degree = len(coeffs) - 1

    print("=" * 60)
    print(f"  Characteristic polynomial: {poly_to_str(coeffs)}")
    print("=" * 60)

    if result.get("routh_table"):
        print("\n  Routh Array:")
        print(f"  {'Power':<8}", end="")
        for j in range(len(result['routh_table'][0])):
            print(f"  {'Col '+str(j+1):>10}", end="")
        print()
        print("  " + "-" * 55)
        for i, row in enumerate(result["routh_table"]):
            power = degree - i
            print(f"  s^{power:<6}", end="")
            for val in row:
                print(f"  {val:>10.4f}", end="")
            print()

        print(f"\n  First column:  {[round(v, 6) for v in result['first_column']]}")
        print(f"  Sign changes:  {result['sign_changes']}")

    status = "✓ System is STABLE" if result["is_stable"] else "✗ System is UNSTABLE"
    print(f"\n  Conclusion: {status}")
    print(f"  Details:    {result['info']}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    #remind: please complete the todo part in the routh_hurwitz() function

    test_cases = [
        ([5, 4, 3, 2, 1],  "All positive coefficients, not necessarily stable"),
        ([1, 6, 11, 6],    "Stable third-order system"),
        ([1, 1, 2, 8],     "Unstable third-order system"),
    ]

    for coeffs, desc in test_cases:
        print(f"  [{desc}]")
        print_routh_result(coeffs)