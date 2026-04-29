"""
Generate all visualizations for the LLM Course README.
"""
import os
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# ── Global Style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'Segoe UI',
    'font.size': 12,
    'axes.facecolor': '#0d1117',
    'figure.facecolor': '#0d1117',
    'text.color': '#e6edf3',
    'axes.labelcolor': '#e6edf3',
    'xtick.color': '#8b949e',
    'ytick.color': '#8b949e',
})

# Google-inspired colors
GOOGLE_BLUE = '#4285F4'
GOOGLE_RED = '#EA4335'
GOOGLE_YELLOW = '#FBBC04'
GOOGLE_GREEN = '#34A853'
DARK_BG = '#0d1117'
CARD_BG = '#161b22'
BORDER = '#30363d'
TEXT_PRIMARY = '#e6edf3'
TEXT_SECONDARY = '#8b949e'

PALETTE = ['#4285F4', '#34A853', '#FBBC04', '#EA4335',
           '#A142F4', '#FF6D01', '#46BDC6', '#E8710A', '#1A73E8']

os.makedirs('assets', exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 1: Course Learning Journey (Progression Arc)
# ═══════════════════════════════════════════════════════════════════════════════


def plot_learning_journey():
    fig, ax = plt.subplots(figsize=(16, 7))

    sessions = [
        ('Session 1\nAPI\nFundamentals', 1),
        ('Session 2\nPrompt\nEngineering', 2),
        ('Session 3\nStructured\nOutputs', 3),
        ('Session 4\nEmbeddings &\nSemantic Search', 4.5),
        ('Session 5\nRAG', 5.5),
        ('Session 6\nFunction\nCalling', 7),
        ('Session 7\nBuilding\nAgents', 8),
        ('Session 8\nAdvanced\nPatterns', 9),
        ('Session 9\nCapstone\nProject', 10),
    ]

    x = np.arange(len(sessions))
    complexity = np.array([s[1] for s in sessions])

    # Smooth curve
    from scipy.interpolate import make_interp_spline
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, complexity, k=3)
    y_smooth = spl(x_smooth)

    # Gradient fill
    for i in range(len(x_smooth) - 1):
        progress = i / len(x_smooth)
        color = plt.cm.cool(progress * 0.8 + 0.1)
        ax.fill_between(x_smooth[i:i+2], 0,
                        y_smooth[i:i+2], alpha=0.15, color=color)

    # Main line with glow
    ax.plot(x_smooth, y_smooth, color=GOOGLE_BLUE, linewidth=3, zorder=3,
            path_effects=[pe.withStroke(linewidth=8, foreground=GOOGLE_BLUE + '40')])

    # Phase backgrounds
    phases = [
        ((-0.5, 2.5), 'Foundation', GOOGLE_BLUE),
        ((2.5, 5.5), 'Knowledge & Data', GOOGLE_GREEN),
        ((5.5, 7.5), 'Autonomy & Tools', GOOGLE_YELLOW),
        ((7.5, 8.5), 'Production', GOOGLE_RED),
    ]

    for (x0, x1), label, color in phases:
        ax.axvspan(x0, x1, alpha=0.06, color=color)
        ax.text((x0 + x1) / 2, 10.6, label, ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=color, alpha=0.9)

    # Session dots
    for i, (label, comp) in enumerate(sessions):
        color = PALETTE[i]
        ax.scatter(i, comp, s=200, color=color, zorder=5,
                   edgecolors='white', linewidth=2)
        ax.text(i, comp + 0.55, label, ha='center', va='bottom',
                fontsize=8, fontweight='bold', color=TEXT_PRIMARY, linespacing=1.2)

    ax.set_xlim(-0.7, 8.7)
    ax.set_ylim(0, 11.5)
    ax.set_ylabel('Complexity & Depth', fontsize=13, fontweight='bold')
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color(BORDER)
    ax.yaxis.set_ticks([])

    # Title
    fig.text(0.5, 0.97, 'LEARNING JOURNEY — FROM FUNDAMENTALS TO PRODUCTION',
             ha='center', va='top', fontsize=16, fontweight='bold', color=TEXT_PRIMARY,
             path_effects=[pe.withStroke(linewidth=3, foreground=DARK_BG)])

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig('assets/learning_journey.png', dpi=180, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close()
    print("✓ learning_journey.png")


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 2: Skills Radar Chart
# ═══════════════════════════════════════════════════════════════════════════════
def plot_skills_radar():
    categories = [
        'API Mastery',
        'Prompt\nEngineering',
        'Data\nStructuring',
        'Embeddings &\nVector Search',
        'RAG\nPipelines',
        'Tool\nIntegration',
        'Agent\nArchitecture',
        'Production\nPatterns',
    ]

    # Skill levels after course completion
    values = [95, 90, 88, 85, 92, 88, 85, 82]

    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
    ax.set_facecolor(DARK_BG)

    # Grid
    for level in [20, 40, 60, 80, 100]:
        ax.plot(angles, [level] * (N + 1), color=BORDER,
                linewidth=0.5, linestyle='--', alpha=0.4)

    # Fill
    ax.fill(angles, values, color=GOOGLE_BLUE, alpha=0.15)
    ax.plot(angles, values, color=GOOGLE_BLUE, linewidth=2.5,
            path_effects=[pe.withStroke(linewidth=6, foreground=GOOGLE_BLUE + '30')])

    # Points
    for i in range(N):
        ax.scatter(angles[i], values[i], s=100, color=PALETTE[i],
                   zorder=5, edgecolors='white', linewidth=1.5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10,
                       fontweight='bold', color=TEXT_PRIMARY)
    ax.set_ylim(0, 105)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'],
                       fontsize=8, color=TEXT_SECONDARY)
    ax.spines['polar'].set_color(BORDER)
    ax.grid(color=BORDER, alpha=0.3)

    fig.text(0.5, 0.98, 'COMPETENCY MAP — SKILLS ACQUIRED',
             ha='center', va='top', fontsize=15, fontweight='bold', color=TEXT_PRIMARY)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('assets/skills_radar.png', dpi=180, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close()
    print("✓ skills_radar.png")


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 3: Technology Stack Breakdown
# ═══════════════════════════════════════════════════════════════════════════════
def plot_tech_stack():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))

    # APIs
    apis = ['Chat\nCompletions', 'Embeddings',
            'Function\nCalling', 'Streaming']
    api_sessions = [9, 4, 3, 2]
    axes[0].barh(apis, api_sessions, color=[GOOGLE_BLUE, GOOGLE_GREEN, GOOGLE_YELLOW, GOOGLE_RED],
                 height=0.6, edgecolor='white', linewidth=0.5)
    axes[0].set_title('OpenAI APIs Used', fontsize=13,
                      fontweight='bold', color=TEXT_PRIMARY, pad=15)
    axes[0].set_xlabel('Sessions Using API', fontsize=10, color=TEXT_SECONDARY)
    axes[0].set_xlim(0, 10)
    for i, v in enumerate(api_sessions):
        axes[0].text(v + 0.2, i, str(v), va='center', fontsize=11,
                     fontweight='bold', color=TEXT_PRIMARY)

    # Patterns
    patterns = ['RAG', 'Agent Loop', 'Chaining', 'Guardrails', 'Evaluation']
    pattern_complexity = [92, 95, 78, 85, 80]
    colors2 = [GOOGLE_GREEN, GOOGLE_BLUE, GOOGLE_YELLOW, GOOGLE_RED, '#A142F4']
    bars = axes[1].bar(patterns, pattern_complexity, color=colors2, width=0.6,
                       edgecolor='white', linewidth=0.5)
    axes[1].set_title('Architecture Patterns', fontsize=13,
                      fontweight='bold', color=TEXT_PRIMARY, pad=15)
    axes[1].set_ylabel('Coverage Depth %', fontsize=10, color=TEXT_SECONDARY)
    axes[1].set_ylim(0, 110)
    for bar, v in zip(bars, pattern_complexity):
        axes[1].text(bar.get_x() + bar.get_width()/2, v + 2, f'{v}%',
                     ha='center', fontsize=10, fontweight='bold', color=TEXT_PRIMARY)
    axes[1].tick_params(axis='x', rotation=25)

    # Libraries
    libs = ['openai', 'numpy', 'json', 'dotenv', 'math']
    lib_usage = [9, 4, 5, 9, 3]
    axes[2].barh(libs, lib_usage, color=[PALETTE[i] for i in range(5)],
                 height=0.6, edgecolor='white', linewidth=0.5)
    axes[2].set_title('Python Libraries', fontsize=13,
                      fontweight='bold', color=TEXT_PRIMARY, pad=15)
    axes[2].set_xlabel('Sessions Used', fontsize=10, color=TEXT_SECONDARY)
    axes[2].set_xlim(0, 10)
    for i, v in enumerate(lib_usage):
        axes[2].text(v + 0.2, i, str(v), va='center', fontsize=11,
                     fontweight='bold', color=TEXT_PRIMARY)

    for ax in axes:
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(BORDER)

    fig.suptitle('TECHNOLOGY ECOSYSTEM', fontsize=16, fontweight='bold',
                 color=TEXT_PRIMARY, y=1.02)
    plt.tight_layout()
    plt.savefig('assets/tech_stack.png', dpi=180, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close()
    print("✓ tech_stack.png")


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 4: Course Architecture (Capstone Integration)
# ═══════════════════════════════════════════════════════════════════════════════
def plot_architecture():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    def draw_box(x, y, w, h, label, color, sublabel=None):
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                             facecolor=color + '25', edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2 + (0.15 if sublabel else 0), label,
                ha='center', va='center', fontsize=11, fontweight='bold', color=color)
        if sublabel:
            ax.text(x + w/2, y + h/2 - 0.25, sublabel,
                    ha='center', va='center', fontsize=8, color=TEXT_SECONDARY)

    def draw_arrow(x1, y1, x2, y2, color=TEXT_SECONDARY):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5, connectionstyle='arc3,rad=0.1'))

    # Title
    ax.text(7, 7.5, 'CAPSTONE APPLICATION ARCHITECTURE', ha='center', va='center',
            fontsize=16, fontweight='bold', color=TEXT_PRIMARY)
    ax.text(7, 7.1, 'Session 9: Integration of All Course Components', ha='center', va='center',
            fontsize=10, color=TEXT_SECONDARY)

    # User Input
    draw_box(0.5, 5.5, 2.5, 1, 'USER INPUT', GOOGLE_BLUE)

    # Guardrails
    draw_box(4, 5.5, 2.8, 1, 'GUARDRAILS', GOOGLE_RED, 'Session 8')

    # Agent Loop
    draw_box(4, 3, 6.5, 2, 'AGENT LOOP', GOOGLE_BLUE, 'Session 7')
    ax.text(7.25, 4.5, 'Observe  >  Think  >  Act  >  Repeat', ha='center', va='center',
            fontsize=9, color=GOOGLE_BLUE, style='italic')

    # Tools inside agent
    draw_box(4.5, 3.2, 1.8, 1, 'TOOLS', GOOGLE_YELLOW, 'Session 6')
    draw_box(6.8, 3.2, 1.8, 1, 'RAG', GOOGLE_GREEN, 'Session 5')
    draw_box(9, 3.2, 1.8, 1, 'CALC', '#A142F4', 'Session 3')

    # Embeddings
    draw_box(0.5, 2.5, 2.5, 1.3, 'EMBEDDINGS', GOOGLE_GREEN, 'Session 4')

    # LLM Core
    draw_box(4, 1, 6.5, 1.3, 'LLM CORE  -  Chat Completions API',
             GOOGLE_BLUE, 'Sessions 1 & 2')

    # Output
    draw_box(11.5, 5.5, 2, 1, 'RESPONSE', GOOGLE_GREEN)

    # Memory
    draw_box(11.5, 3, 2, 1.2, 'MEMORY', '#A142F4', 'Session 7')

    # Arrows
    draw_arrow(3, 6, 4, 6, GOOGLE_BLUE)
    draw_arrow(6.8, 5.5, 7.25, 5, GOOGLE_RED)
    draw_arrow(7.25, 3, 7.25, 2.3, GOOGLE_BLUE)
    draw_arrow(3, 3.5, 4.5, 3.7, GOOGLE_GREEN)
    draw_arrow(10.5, 4, 11.5, 4, '#A142F4')
    draw_arrow(10.5, 5.5, 11.5, 5.5, GOOGLE_GREEN)

    plt.savefig('assets/architecture.png', dpi=180, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close()
    print("✓ architecture.png")


# ═══════════════════════════════════════════════════════════════════════════════
# PLOT 5: Session Coverage Heatmap
# ═══════════════════════════════════════════════════════════════════════════════
def plot_heatmap():
    fig, ax = plt.subplots(figsize=(14, 6))

    concepts = ['API Calls', 'Prompting', 'JSON/Schema', 'Embeddings',
                'RAG', 'Tool Use', 'Agent Loop', 'Guardrails', 'Evaluation']
    sessions = [f'S{i}' for i in range(1, 10)]

    # Intensity matrix (how much each concept is used in each session)
    data = np.array([
        [10, 8, 8, 6, 7, 8, 8, 7, 9],   # API Calls
        [4, 10, 6, 3, 4, 3, 4, 5, 5],    # Prompting
        [2, 2, 10, 2, 2, 8, 6, 4, 7],    # JSON/Schema
        [0, 0, 0, 10, 9, 0, 2, 0, 8],    # Embeddings
        [0, 0, 0, 3, 10, 0, 2, 0, 9],    # RAG
        [0, 0, 0, 0, 0, 10, 9, 2, 9],    # Tool Use
        [0, 0, 0, 0, 0, 0, 10, 2, 9],    # Agent Loop
        [0, 0, 0, 0, 0, 0, 0, 10, 8],    # Guardrails
        [0, 0, 0, 0, 0, 0, 0, 8, 6],     # Evaluation
    ])

    # Custom colormap
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('google',
                                             [(0, '#161b22'), (0.3, '#1a3a5c'), (0.6, '#2a6cb7'), (1.0, '#4285F4')])

    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=10)

    ax.set_xticks(range(len(sessions)))
    ax.set_xticklabels(sessions, fontsize=11, fontweight='bold')
    ax.set_yticks(range(len(concepts)))
    ax.set_yticklabels(concepts, fontsize=11, fontweight='bold')

    # Annotate
    for i in range(len(concepts)):
        for j in range(len(sessions)):
            val = data[i, j]
            if val > 0:
                color = 'white' if val > 5 else TEXT_SECONDARY
                ax.text(j, i, str(val), ha='center', va='center',
                        fontsize=10, fontweight='bold', color=color)

    ax.set_title('CONCEPT COVERAGE ACROSS SESSIONS', fontsize=15,
                 fontweight='bold', color=TEXT_PRIMARY, pad=20)

    cbar = plt.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label('Coverage Intensity', fontsize=10, color=TEXT_SECONDARY)
    cbar.ax.yaxis.set_tick_params(color=TEXT_SECONDARY)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=TEXT_SECONDARY)

    for spine in ax.spines.values():
        spine.set_color(BORDER)

    plt.tight_layout()
    plt.savefig('assets/heatmap.png', dpi=180, bbox_inches='tight',
                facecolor=DARK_BG, edgecolor='none')
    plt.close()
    print("✓ heatmap.png")


# ═══════════════════════════════════════════════════════════════════════════════
# RUN ALL
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating course visualizations...")
    plot_learning_journey()
    plot_skills_radar()
    plot_tech_stack()
    plot_architecture()
    plot_heatmap()
    print("\n✅ All plots generated in assets/")
