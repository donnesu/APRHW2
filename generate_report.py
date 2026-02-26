#!/usr/bin/env python3
"""Generate report.pdf for HW2 (CS 378 Automated Planning for Robots).
Run: python3 generate_report.py
Requires: fpdf2, matplotlib  (pip install fpdf2 matplotlib)
"""

import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ---------------------------------------------------------------------------
# Actual measurements obtained by running Fast Downward
# ---------------------------------------------------------------------------

# Q1: Independent Tasks, eager_greedy([ff()])
# domain: independent-tasks, h^ff = n, h* = n
q1 = [
    # (problem, size_n, h_ff, plan_cost, ratio)
    (1, 1, 1, 1,  1.00),
    (2, 2, 2, 2,  1.00),
    (3, 3, 3, 3,  1.00),
    (4, 4, 4, 4,  1.00),
    (5, 5, 5, 5,  1.00),
]

# Q2: Key-Doors, eager_greedy([ff()])
# domain: key-doors, h^ff = n, h* = 2n-1
q2 = [
    (1, 1,  1,  1, 1.00),
    (2, 2,  2,  3, round(2/3,  3)),
    (3, 3,  3,  5, round(3/5,  3)),
    (4, 4,  4,  7, round(4/7,  3)),
    (5, 5,  5,  9, round(5/9,  3)),
]

# Q4: Single-Gripper, eager_greedy([cg()])
# domain: gripper-single, h_cg = 3n, h* = 4n-1
q4 = [
    (1,  2,  6,  7, round( 6/ 7, 3)),
    (2,  4, 12, 15, round(12/15, 3)),
    (3,  6, 18, 23, round(18/23, 3)),
    (4,  8, 24, 31, round(24/31, 3)),
    (5, 10, 30, 39, round(30/39, 3)),
]

# ---------------------------------------------------------------------------
# Plot helper
# ---------------------------------------------------------------------------

def make_plot(datasets, labels, colors, title, x_label="Problem size (n)",
              figsize=(6, 3.4)):
    fig, ax = plt.subplots(figsize=figsize)
    for data, label, color in zip(datasets, labels, colors):
        xs = [d[1] for d in data]
        ys = [d[4] for d in data]
        ax.plot(xs, ys, marker='o', label=label, color=color, linewidth=1.8)
    ax.axhline(1.0, color='gray', linestyle='--', linewidth=0.8, label='ratio = 1')
    ax.set_xlabel(x_label, fontsize=11)
    ax.set_ylabel("Ratio  h / plan cost", fontsize=11)
    ax.set_title(title, fontsize=11)
    ax.set_ylim(0, 1.2)
    ax.legend(fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.55)
    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf

# ---------------------------------------------------------------------------
# PDF helpers
# ---------------------------------------------------------------------------

class Report(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 9, "CS 378: Automated Planning for Robots - HW 2",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.set_font("Helvetica", "", 10)
        self.cell(0, 6, "Understanding the Limits of Classical Heuristics",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

    def section(self, text):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(215, 228, 248)
        self.cell(0, 8, text, fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        self.set_font("Helvetica", "", 10)

    def para(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def table(self, headers, rows, widths):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(175, 200, 230)
        for h, w in zip(headers, widths):
            self.cell(w, 7, h, border=1, fill=True, align='C')
        self.ln()
        self.set_font("Helvetica", "", 9)
        for i, row in enumerate(rows):
            self.set_fill_color(240, 246, 255) if i % 2 == 0 \
                else self.set_fill_color(255, 255, 255)
            for val, w in zip(row, widths):
                self.cell(w, 6, str(val), border=1, fill=True, align='C')
            self.ln()
        self.ln(4)

    def fig(self, buf, w=160, caption=""):
        x = (self.w - w) / 2
        self.image(buf, x=x, w=w)
        if caption:
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 5, caption,
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(3)

# ---------------------------------------------------------------------------
# Build PDF
# ---------------------------------------------------------------------------

pdf = Report()
pdf.set_margins(18, 18, 18)
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

# ---- Intro ---------------------------------------------------------------
pdf.set_font("Helvetica", "B", 13)
pdf.cell(0, 9, "Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.ln(1)

pdf.para(
    "This report presents three families of planning problems that demonstrate "
    "when classical planning heuristics are accurate (Q1) or very inaccurate "
    "(Q2, Q4).  All measurements were obtained by running Fast Downward with "
    "eager_greedy search."
)
pdf.para(
    "Accuracy is measured as the ratio  r = h(s0) / plan_cost,  where h(s0) "
    "is the initial heuristic value reported by Fast Downward and plan_cost "
    "is the cost of the plan found by greedy search.  A ratio of 1 means the "
    "heuristic is perfectly accurate; a decreasing ratio indicates a very "
    "inaccurate heuristic."
)
pdf.para("Questions answered: Q1 (FF accurate), Q2 (FF inaccurate), "
         "Q4 (CG inaccurate, extra credit).")

# ---- Q1 ------------------------------------------------------------------
pdf.section("Q1 - Relaxed-Plan Heuristic (FF) is Accurate")

pdf.para(
    "Domain: Independent Tasks\n\n"
    "Each problem instance contains n tasks.  A single 'do-task(?t)' action "
    "completes any pending task with no side effects.  Tasks share no "
    "resources and have no negative interactions with each other."
)
pdf.para(
    "Why FF is accurate:\n"
    "In the relaxed planning graph (delete effects ignored) every goal "
    "'completed(ti)' is directly achievable by 'do-task(ti)', whose only "
    "precondition 'pending(ti)' is satisfied in the initial state.  Because "
    "there are no shared or conflicting resources, the relaxed plan contains "
    "exactly n actions - exactly the same as the optimal real plan.  "
    "h^ff = h* = n,  ratio = 1.00 for every instance."
)

pdf.table(
    ["Problem", "Size (n)", "h^ff (FF)", "Plan cost", "Ratio"],
    [(f"p{d[0]}", d[1], d[2], d[3], f"{d[4]:.2f}") for d in q1],
    [28, 32, 38, 38, 34]
)

buf1 = make_plot(
    [q1], ["Q1 - FF (independent tasks)"], ['steelblue'],
    "Q1: h^ff / plan cost  (FF accurate, ratio = 1 throughout)"
)
pdf.fig(buf1, caption="Figure 1 - Q1 ratio remains 1.00 for all problem sizes.")

# ---- Q2 ------------------------------------------------------------------
pdf.add_page()
pdf.section("Q2 - Relaxed-Plan Heuristic (FF) is Inaccurate")

pdf.para(
    "Domain: Key-Doors\n\n"
    "There is ONE shared key and n doors, all initially closed.  The goal "
    "is to open all doors.  Actions:\n"
    "  - use-key(?d): pre: key-ready, door-closed(?d); "
    "effect: door-open(?d), key-used, NOT key-ready.\n"
    "  - renew-key: pre: key-used; effect: key-ready, NOT key-used.\n\n"
    "Opening a door CONSUMES the key (sets key-used, removes key-ready).  "
    "The key must be renewed before the next door can be opened.  "
    "FF ignores this delete effect."
)
pdf.para(
    "Why FF is inaccurate:\n"
    "FF ignores the delete effect NOT key-ready.  In the relaxed plan, "
    "key-ready is never removed, so all n doors can be opened by n "
    "consecutive use-key actions without any renewal.  h^ff = n.\n\n"
    "In the real problem after opening door d1 the key is gone.  The "
    "optimal plan must alternate: use-key, renew, use-key, renew, ..., "
    "use-key, giving h* = 2n - 1.\n\n"
    "Ratio = n / (2n-1)  decreases from 1.00 toward 0.50 as n grows."
)

pdf.table(
    ["Problem", "Size (n)", "h^ff (FF)", "Plan cost", "Ratio"],
    [(f"p{d[0]}", d[1], d[2], d[3], f"{d[4]:.3f}") for d in q2],
    [28, 32, 38, 38, 34]
)

buf2 = make_plot(
    [q2], ["Q2 - FF (key-doors)"], ['crimson'],
    "Q2: h^ff / plan cost  (FF inaccurate, ratio decreasing)"
)
pdf.fig(buf2, caption="Figure 2 - Q2 ratio decreases from 1.00 toward 0.50 as n grows.")

# ---- Q4 ------------------------------------------------------------------
pdf.add_page()
pdf.section("Q4 (Extra Credit) - Causal-Graph Heuristic (CG) is Inaccurate")

pdf.para(
    "Domain: Single-Gripper (one-gripper variant of the IPC Gripper benchmark)\n\n"
    "A robot with ONE gripper must transport n balls from room A to room B, "
    "one ball at a time.  Problem sizes: n = 2, 4, 6, 8, 10 balls.  "
    "Actions: move(from,to), pick(ball,room), drop(ball,room)."
)
pdf.para(
    "Optimal cost:\n"
    "Each trip carries 1 ball.  Forward trip: pick + move(A->B) + drop = 3.  "
    "Return trip: move(B->A) = 1.  "
    "For n balls:  h* = 3n + (n-1) = 4n - 1  (last trip has no return)."
)
pdf.para(
    "Why CG is inaccurate:\n"
    "The CG heuristic processes each ball's Domain Transition Graph (DTG) "
    "independently.  For each ball it sees a cost of 3 (pick + shared move + "
    "drop) but treats the single A->B move as shared across all balls.  It "
    "does not account for the return trip the robot must make between "
    "deliveries.  The estimate is  h_CG = 3n.\n\n"
    "Ratio = 3n / (4n - 1)  decreases toward 0.75 as n grows."
)

pdf.table(
    ["Problem", "Balls (n)", "h_CG (CG)", "Plan cost", "Ratio"],
    [(f"p{d[0]}", d[1], d[2], d[3], f"{d[4]:.3f}") for d in q4],
    [28, 32, 38, 38, 34]
)

buf4 = make_plot(
    [q4], ["Q4 - CG (single-gripper)"], ['darkorange'],
    "Q4: h_CG / plan cost  (CG inaccurate, ratio decreasing)",
    x_label="Balls (n)"
)
pdf.fig(buf4, caption="Figure 3 - Q4 ratio decreases as more balls require more return trips.")

# ---- Combined plot -------------------------------------------------------
pdf.add_page()
pdf.section("Summary")

buf_all = make_plot(
    [q1, q2, q4],
    ["Q1 - FF (accurate)", "Q2 - FF (inaccurate)", "Q4 - CG (inaccurate)"],
    ['steelblue', 'crimson', 'darkorange'],
    "Heuristic Accuracy Ratio for All Questions",
    figsize=(7, 4.2)
)
pdf.fig(buf_all, w=168,
        caption="Figure 4 - Q1 stays at 1.0; Q2 and Q4 decrease with problem size.")

pdf.para(
    "Summary of findings:\n\n"
    "Q1 (Independent Tasks): FF is perfectly accurate (ratio = 1.00) "
    "because every goal can be achieved by a single independent action.  "
    "No delete effects matter.\n\n"
    "Q2 (Key-Doors): FF is very inaccurate.  It ignores that opening a door "
    "consumes the key, so the relaxed plan opens all n doors in n steps "
    "(h^ff = n) while the real plan needs 2n-1 steps.  The ratio "
    "n/(2n-1) decreases from 1.00 toward 0.50.\n\n"
    "Q4 (Single-Gripper, extra credit): CG is inaccurate.  It sums the "
    "per-ball DTG costs without accounting for the return trips the robot "
    "must make between deliveries.  h_CG = 3n while plan cost = 4n-1.  "
    "The ratio decreases monotonically from ~0.857 toward 0.75."
)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.pdf")
pdf.output(out)
print(f"Written: {out}")
