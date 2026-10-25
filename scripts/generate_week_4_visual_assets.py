#!/usr/bin/env python3
"""
generate_week_4_visual_assets.py
Generates 4 High-Contrast, Mobile-First Visual Assets for Week 4 Investigation
Format: 1920x1080 (16:9), Large Bold Typography (32pt - 64pt), Institutional Rayls Branding
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"c:\Users\9ytshade\Desktop\Rayls\Week_4_Tokenized_Deposits_vs_Stablecoins\diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

# Brand Color Palette
BG_DARK = "#0a0d14"
SURFACE_CARD = "#121722"
SURFACE_BORDER = "#1f293d"
ACCENT_CYAN = "#00f2fe"
ACCENT_GREEN = "#10b981"
ACCENT_PURPLE = "#8b5cf6"
ACCENT_AMBER = "#f59e0b"
ACCENT_RED = "#ef4444"
TEXT_WHITE = "#ffffff"
TEXT_MUTED = "#94a3b8"
TEXT_SUB = "#cbd5e1"

def get_font(size, bold=False):
    name = "segoeuib.ttf" if bold else "segoeui.ttf"
    try:
        return ImageFont.truetype(name, size)
    except:
        return ImageFont.truetype("arial.ttf", size)

def draw_header(draw, title, subtitle, tag_text="INDEPENDENT RESEARCH"):
    # Decorative Top Banner
    draw.rectangle([0, 0, 1920, 10], fill=ACCENT_CYAN)
    
    # Tag Pill
    draw.rounded_rectangle([80, 50, 360, 95], radius=8, fill="#1e293b", outline=ACCENT_CYAN, width=2)
    draw.text((105, 58), tag_text, font=get_font(22, bold=True), fill=ACCENT_CYAN)
    
    # Main Title & Subtitle
    draw.text((80, 115), title, font=get_font(48, bold=True), fill=TEXT_WHITE)
    draw.text((80, 175), subtitle, font=get_font(24), fill=TEXT_MUTED)
    
    # Dividing Line
    draw.line([80, 220, 1840, 220], fill=SURFACE_BORDER, width=2)

def draw_footer(draw, note="Target: Rayls Public Chain (72957) & Sovereign Subnet Architecture | Zero Assumptions Standard"):
    draw.line([80, 1000, 1840, 1000], fill=SURFACE_BORDER, width=2)
    draw.text((80, 1018), "RAYLS RESEARCH INITIATIVE", font=get_font(20, bold=True), fill=ACCENT_CYAN)
    draw.text((450, 1018), note, font=get_font(18), fill=TEXT_MUTED)

# ==============================================================================
# ASSET 1: COVER IMAGE
# ==============================================================================
def create_cover_image():
    img = Image.new("RGB", (1920, 1080), color=BG_DARK)
    draw = ImageDraw.Draw(img)

    # Accent Top Line
    draw.rectangle([0, 0, 1920, 12], fill=ACCENT_CYAN)
    
    # Header Tag
    draw.rounded_rectangle([100, 80, 480, 130], radius=8, fill="#1e293b", outline=ACCENT_CYAN, width=2)
    draw.text((125, 90), "INSTITUTIONAL SETTLEMENT AUDIT", font=get_font(22, bold=True), fill=ACCENT_CYAN)

    # Main Headline
    draw.text((100, 160), "Tokenized Deposits vs. Stablecoins", font=get_font(64, bold=True), fill=TEXT_WHITE)
    draw.text((100, 245), "The Structural, Legal & Balance Sheet Divergence in Banking", font=get_font(36), fill=ACCENT_CYAN)

    # Subtitle Paragraph
    sub = ("Deconstructing the Singleness of Money, Bearer Debt vs. M1 Bank Liabilities,\n"
           "ERC-3643 Permissioned Transfer Gates, and Rayls Sovereign Subnet Settlement.")
    draw.text((100, 315), sub, font=get_font(24), fill=TEXT_SUB, spacing=8)

    # 3 Institutional Feature Cards
    cards = [
        {
            "title": "The Monetary Trilemma",
            "desc": "Why central banks (BIS Project Agora) reject private bearer stablecoins to preserve par value ($1.00 = $1.00).",
            "color": ACCENT_PURPLE,
            "metric": "BIS Bulletin 73"
        },
        {
            "title": "Smart Contract Anatomy",
            "desc": "Blunt binary blacklists (USDC) vs. Programmable Identity & Compliance Gates (ERC-3643).",
            "color": ACCENT_CYAN,
            "metric": "5 Gate Tests"
        },
        {
            "title": "Rayls Sovereign Subnets",
            "desc": "Zero customer balance leakage, Paradigm Reth execution, and deterministic single-slot BFT finality.",
            "color": ACCENT_GREEN,
            "metric": "Chain 72957 Audit"
        }
    ]

    card_w, card_h = 540, 420
    for idx, c in enumerate(cards):
        x = 100 + idx * (card_w + 35)
        y = 440
        # Card Background
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=16, fill=SURFACE_CARD, outline=SURFACE_BORDER, width=2)
        # Accent Header Bar
        draw.rounded_rectangle([x, y, x + card_w, y + 10], radius=16, fill=c["color"])
        # Badge
        draw.rounded_rectangle([x + 30, y + 35, x + 240, y + 75], radius=6, fill="#1e293b", outline=c["color"], width=1)
        draw.text((x + 45, y + 42), c["metric"], font=get_font(18, bold=True), fill=c["color"])
        # Title & Text
        draw.text((x + 30, y + 105), c["title"], font=get_font(30, bold=True), fill=TEXT_WHITE)
        draw.text((x + 30, y + 165), c["desc"], font=get_font(22), fill=TEXT_SUB, spacing=8)

    # Footer
    draw.line([100, 930, 1820, 930], fill=SURFACE_BORDER, width=2)
    draw.text((100, 960), "AUTHOR: Independent On-Chain Systems Investigation", font=get_font(20, bold=True), fill=TEXT_WHITE)
    draw.text((800, 960), "Citations: BIS Project Agora, NY Fed RLN, CPMI-IOSCO Principle 8, EU MiCA", font=get_font(20), fill=TEXT_MUTED)

    out = os.path.join(OUT_DIR, "cover_image_tokenized_deposits.png")
    img.save(out)
    print("Generated Cover Image:", out)

# ==============================================================================
# ASSET 2: BALANCE SHEET COMPARISON DIAGRAM
# ==============================================================================
def create_balance_sheet_diagram():
    img = Image.new("RGB", (1920, 1080), color=BG_DARK)
    draw = ImageDraw.Draw(img)

    draw_header(draw, "The Balance Sheet Topology: Stablecoin vs. Tokenized Deposit",
                "Why Stablecoins Drain Credit from the Economy While Tokenized Deposits Preserve M1 Liabilities",
                "MACROECONOMIC ARCHITECTURE")

    # Column 1: Fiat-Backed Stablecoin Issuer
    draw.rounded_rectangle([80, 260, 920, 960], radius=16, fill=SURFACE_CARD, outline=ACCENT_PURPLE, width=2)
    draw.text((115, 290), "FIAT-BACKED STABLECOIN ISSUER", font=get_font(32, bold=True), fill=ACCENT_PURPLE)
    draw.text((115, 335), "Narrow Banking Model (Circle / Tether)", font=get_font(22), fill=TEXT_MUTED)

    # Assets Box
    draw.rounded_rectangle([115, 380, 480, 680], radius=10, fill="#182030", outline=SURFACE_BORDER, width=1)
    draw.text((135, 400), "ASSETS (100% Backing)", font=get_font(22, bold=True), fill=ACCENT_CYAN)
    draw.text((135, 450), "• 30-90 Day US Treasuries\n• Overnight Reverse Repo\n• Uninsured Bank Cash", font=get_font(20), fill=TEXT_SUB, spacing=14)

    # Liabilities Box
    draw.rounded_rectangle([520, 380, 885, 680], radius=10, fill="#182030", outline=SURFACE_BORDER, width=1)
    draw.text((540, 400), "LIABILITIES (Bearer Debt)", font=get_font(22, bold=True), fill=ACCENT_PURPLE)
    draw.text((540, 450), "• Circulating ERC-20 Tokens\n• Contractual Redemption Claim\n• Zero Deposit Insurance (No FDIC)", font=get_font(20), fill=TEXT_SUB, spacing=14)

    # Impact Box
    draw.rounded_rectangle([115, 710, 885, 930], radius=10, fill="#231828", outline=ACCENT_RED, width=1)
    draw.text((135, 730), "SYSTEMIC MACRO IMPACT:", font=get_font(22, bold=True), fill=ACCENT_RED)
    draw.text((135, 775), "• Capital Drain: Siphons commercial bank deposits into passive government T-bills.\n"
                          "• Disintermediates Credit: Halts commercial and consumer loan generation.\n"
                          "• Par Deviation Risk: Trades at discount under liquidity stress ($0.87 in SVB panic).",
              font=get_font(20), fill=TEXT_SUB, spacing=10)

    # Column 2: Commercial Bank Tokenized Deposit
    draw.rounded_rectangle([1000, 260, 1840, 960], radius=16, fill=SURFACE_CARD, outline=ACCENT_GREEN, width=2)
    draw.text((1035, 290), "COMMERCIAL BANK TOKENIZED DEPOSIT", font=get_font(32, bold=True), fill=ACCENT_GREEN)
    draw.text((1035, 335), "Two-Tier Fractional Banking (Rayls Sovereign Subnet)", font=get_font(22), fill=TEXT_MUTED)

    # Assets Box
    draw.rounded_rectangle([1035, 380, 1400, 680], radius=10, fill="#182030", outline=SURFACE_BORDER, width=1)
    draw.text((1055, 400), "ASSETS (Fractional Reserves)", font=get_font(22, bold=True), fill=ACCENT_CYAN)
    draw.text((1055, 450), "• Central Bank Reserves (M0)\n• Commercial Loans & Mortgages\n• Interbank Liquid Claims", font=get_font(20), fill=TEXT_SUB, spacing=14)

    # Liabilities Box
    draw.rounded_rectangle([1440, 380, 1805, 680], radius=10, fill="#182030", outline=SURFACE_BORDER, width=1)
    draw.text((1460, 400), "LIABILITIES (Native M1)", font=get_font(22, bold=True), fill=ACCENT_GREEN)
    draw.text((1460, 450), "• Demand Deposit Obligation\n• Direct Customer Legal Title\n• Statutory Deposit Insurance", font=get_font(20), fill=TEXT_SUB, spacing=14)

    # Impact Box
    draw.rounded_rectangle([1035, 710, 1805, 930], radius=10, fill="#122a22", outline=ACCENT_GREEN, width=1)
    draw.text((1055, 730), "SYSTEMIC MACRO BENEFIT:", font=get_font(22, bold=True), fill=ACCENT_GREEN)
    draw.text((1055, 775), "• Multiplies Economic Credit: Preserves fractional banking loan extension.\n"
                          "• Preserves Singleness of Money: Settles interbank in central bank money at par.\n"
                          "• Lender-of-Last-Resort Access: Backed by Central Bank Discount Window.",
              font=get_font(20), fill=TEXT_SUB, spacing=10)

    draw_footer(draw, "Primary Citations: BIS Bulletin No. 73 (Garratt & Shin) & Federal Reserve RLN Report")

    out = os.path.join(OUT_DIR, "diagram_1_balance_sheet_comparison.png")
    img.save(out)
    print("Generated Balance Sheet Diagram:", out)

# ==============================================================================
# ASSET 3: NEGATIVE TEST GATES INFOGRAPHIC
# ==============================================================================
def create_negative_test_diagram():
    img = Image.new("RGB", (1920, 1080), color=BG_DARK)
    draw = ImageDraw.Draw(img)

    draw_header(draw, "Empirical Negative Testing: Permissioned Transfer Gates",
                "Demonstrating Deterministic Reverts across 5 Real-World Regulatory & Sizing Boundary Cases",
                "EMPIRICAL REPRODUCIBILITY")

    test_rows = [
        {
            "id": "TEST 1",
            "name": "Compliant Institution to KYC Client",
            "type": "POSITIVE",
            "code": "SUCCESS",
            "detail": "$1,000,000.00 Transferred | State Mutated Normally",
            "color": ACCENT_GREEN
        },
        {
            "id": "TEST 2",
            "name": "Transfer to Non-Whitelisted Address",
            "type": "NEGATIVE",
            "code": "0xd3b34208",
            "detail": "REVERT: RecipientNotIdentityVerified (Unverified account blocked)",
            "color": ACCENT_RED
        },
        {
            "id": "TEST 3",
            "name": "Overspend Attempt ($15M from $9M)",
            "type": "NEGATIVE",
            "code": "0x78a1bc40",
            "detail": "REVERT: ComplianceRuleViolation (Tier limit exceeded)",
            "color": ACCENT_RED
        },
        {
            "id": "TEST 4",
            "name": "Sanctioned Jurisdiction Transfer",
            "type": "NEGATIVE",
            "code": "0x78a1bc40",
            "detail": "REVERT: ComplianceRuleViolation (Country Code 643 blocked)",
            "color": ACCENT_RED
        },
        {
            "id": "TEST 5",
            "name": "Sizing Limit Violation ($7.5M > $5M)",
            "type": "NEGATIVE",
            "code": "0x78a1bc40",
            "detail": "REVERT: ComplianceRuleViolation (Institutional tier cap exceeded)",
            "color": ACCENT_RED
        }
    ]

    y_start = 260
    row_h = 130
    for idx, r in enumerate(test_rows):
        y = y_start + idx * (row_h + 15)
        # Card
        draw.rounded_rectangle([80, y, 1840, y + row_h], radius=12, fill=SURFACE_CARD, outline=SURFACE_BORDER, width=2)
        # Badge
        draw.rounded_rectangle([110, y + 25, 250, y + 75], radius=6, fill="#1e293b", outline=r["color"], width=2)
        draw.text((130, y + 35), r["id"], font=get_font(24, bold=True), fill=r["color"])
        # Scenario Name
        draw.text((280, y + 25), r["name"], font=get_font(26, bold=True), fill=TEXT_WHITE)
        draw.text((280, y + 70), r["detail"], font=get_font(20), fill=TEXT_SUB)
        # Result Pill
        pill_color = "#122a22" if r["type"] == "POSITIVE" else "#2a151b"
        draw.rounded_rectangle([1500, y + 35, 1800, y + 95], radius=8, fill=pill_color, outline=r["color"], width=2)
        draw.text((1530, y + 48), r["code"], font=get_font(22, bold=True), fill=r["color"])

    draw_footer(draw, "Executed via test_permissioned_transfer_gates.py | 100% Deterministic Pass Rate")

    out = os.path.join(OUT_DIR, "diagram_2_negative_test_gates.png")
    img.save(out)
    print("Generated Negative Test Diagram:", out)

# ==============================================================================
# ASSET 4: EVIDENCE BOUNDARY MATRIX TABLE
# ==============================================================================
def create_evidence_matrix_table():
    img = Image.new("RGB", (1920, 1080), color=BG_DARK)
    draw = ImageDraw.Draw(img)

    draw_header(draw, "The Evidence Boundary Matrix: Zero Assumptions Standard",
                "Explicit Classification of Verified On-Chain State, Simulations, Documented Specs, and Authorities",
                "AUDIT INTEGRITY MATRIX")

    # Table Header
    headers = [("ARCHITECTURAL COMPONENT", 420), ("CLAIM / VERIFIED METRIC", 420), ("STATUS", 280), ("SOURCE / EVIDENCE PATH", 640)]
    x_offset = 80
    y_header = 250
    draw.rounded_rectangle([80, y_header, 1840, y_header + 55], radius=8, fill="#1e293b")
    
    cur_x = 100
    for h, w in headers:
        draw.text((cur_x, y_header + 15), h, font=get_font(20, bold=True), fill=ACCENT_CYAN)
        cur_x += w

    matrix_rows = [
        ("Public Chain Head Height", "Block #13,031,708+ (Chain ID: 72957)", "Verified On-Chain", ACCENT_GREEN, "eth_blockNumber live RPC query"),
        ("Block Gas Limit Ceiling", "500,000,000 gas (16.6x Ethereum L1)", "Verified On-Chain", ACCENT_GREEN, "Canonical header gasLimit (0x1dcd6500)"),
        ("Empirical Block Cadence", "1.3448 s (std: 0.4753s, Min 1s, Max 2s)", "Verified On-Chain", ACCENT_GREEN, "Batch sampling of 30 consecutive blocks"),
        ("FeeAggregator Balance", "0.000000 USDr (Pass-Through Pipeline)", "Verified On-Chain", ACCENT_GREEN, "eth_getBalance on contract 0x07E1...17E2"),
        ("EVM Precompiles (0x01-08)", "Active & Canonical Execution Output", "Verified On-Chain", ACCENT_GREEN, "eth_call verification on Paradigm Reth"),
        ("Identity KYC Gate Revert", "Reverts with 0xd3b34208", "Empirically Simulated", ACCENT_AMBER, "test_permissioned_transfer_gates.py"),
        ("Sanctions Compliance Revert", "Reverts with 0x78a1bc40", "Empirically Simulated", ACCENT_AMBER, "test_permissioned_transfer_gates.py"),
        ("Private Subnet Deposit State", "Encrypted State in MDBX / Zero Leakage", "Documented Architecture", ACCENT_PURPLE, "Rayls Whitepaper v2.0 & Drex Pilot Specs"),
        ("Singleness of Money Principle", "No-Par Interbank Settlement ($1.00 = $1.00)", "Statutory / Authority", ACCENT_CYAN, "BIS Bulletin No. 73 (Garratt & Shin)"),
        ("Deposit Exclusion from MiCA", "Credit institution deposits exempt", "Statutory / Authority", ACCENT_CYAN, "EU Regulation 2023/1114, Art. 2(2)(b)")
    ]

    y_row = 320
    row_height = 62
    for r in matrix_rows:
        draw.rounded_rectangle([80, y_row, 1840, y_row + row_height], radius=6, fill=SURFACE_CARD, outline=SURFACE_BORDER, width=1)
        # Col 1
        draw.text((100, y_row + 18), r[0], font=get_font(20, bold=True), fill=TEXT_WHITE)
        # Col 2
        draw.text((520, y_row + 18), r[1], font=get_font(19), fill=TEXT_SUB)
        # Col 3 (Pill)
        draw.rounded_rectangle([940, y_row + 12, 1180, y_row + 50], radius=6, fill="#1c2433", outline=r[3], width=1)
        draw.text((955, y_row + 18), r[2], font=get_font(17, bold=True), fill=r[3])
        # Col 4
        draw.text((1220, y_row + 18), r[4], font=get_font(19), fill=TEXT_MUTED)
        
        y_row += row_height + 6

    draw_footer(draw, "Strict Categorization: Zero Assumptions | Public Chain (72957) vs. Private Subnet")

    out = os.path.join(OUT_DIR, "evidence_boundary_matrix_table.png")
    img.save(out)
    print("Generated Evidence Matrix Table:", out)

if __name__ == "__main__":
    create_cover_image()
    create_balance_sheet_diagram()
    create_negative_test_diagram()
    create_evidence_matrix_table()
    print("ALL 4 VISUAL ASSETS GENERATED SUCCESSFULLY!")
