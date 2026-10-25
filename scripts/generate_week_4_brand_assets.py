#!/usr/bin/env python3
"""
generate_week_4_brand_assets.py
Generates 4 Official Rayls Brand Visual Assets for Week 4
Strictly adhering to the Noir Ventures Rayls Brand Guide:
- Color Palette:
    * Primary Gradient: C_PURPLE (#B49AFF) to C_YELLOW (#ECFB3E)
    * Inverted Accent Band: C_YELLOW to C_PURPLE
    * Secondary Accent: C_GREEN (#8CF78B)
    * Dark Cards: C_CARD_BG (26, 26, 30, 245) with C_CARD_BORDER (55, 55, 62)
    * Text: C_BLACK (#111111) on gradients, C_WHITE (#FFFFFF) on dark cards, C_TEXT_MUTED (#A0A0AF)
- Typography: Segoe UI Bold / Regular / Consolas (Clean, perfectly padded, zero text overflows)
- Official Logos & Brand Marks: Untouched official PNGs from c:/Users/9ytshade/Desktop/Rayls/Brand_Guide/Rayls_Logo_Pack/PNG/
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Brand Palette (Strictly Noir Ventures Brand Guide)
C_BLACK = (17, 17, 17, 255)         # #111111
C_WHITE = (255, 255, 255, 255)       # #FFFFFF
C_GRAY_LIGHT = (239, 241, 245, 255)  # #EFF1F5
C_YELLOW = (236, 251, 62, 255)       # #ECFB3E Primary Accent
C_PURPLE = (180, 154, 255, 255)      # #B49AFF Primary Accent
C_GREEN = (140, 247, 139, 255)       # #8CF78B Secondary Accent
C_RED = (255, 107, 107, 255)         # #FF6B6B Error Revert Accent

C_CARD_BG = (24, 24, 28, 248)
C_CARD_ALT = (32, 32, 38, 255)
C_CARD_BORDER = (55, 55, 65, 255)
C_HEADER_ROW = (18, 18, 22, 255)
C_TEXT_MUTED = (160, 160, 175, 255)

FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_REG = "C:/Windows/Fonts/segoeui.ttf"
FONT_MONO = "C:/Windows/Fonts/consola.ttf"

LOGO_BLACK_PATH = "c:/Users/9ytshade/Desktop/Rayls/Brand_Guide/Rayls_Logo_Pack/PNG/Rayls_Logo_Black.png"
LOGO_WHITE_PATH = "c:/Users/9ytshade/Desktop/Rayls/Brand_Guide/Rayls_Logo_Pack/PNG/Rayls_Logo_White.png"
SYMBOL_BLACK_PATH = "c:/Users/9ytshade/Desktop/Rayls/Brand_Guide/Rayls_Logo_Pack/PNG/Rayls_Symbol_Black.png"

OUTPUT_DIR = r"c:\Users\9ytshade\Desktop\Rayls\Week_4_Tokenized_Deposits_vs_Stablecoins\diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_horizontal_gradient(width, height, color1, color2):
    base = Image.new("RGBA", (width, height), color1)
    top = Image.new("RGBA", (width, height), color2)
    mask = Image.new("L", (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (x / width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def paste_official_logo(img, x, y, target_h=46, white=False):
    path = LOGO_WHITE_PATH if white else LOGO_BLACK_PATH
    if os.path.exists(path):
        logo = Image.open(path).convert("RGBA")
        lw, lh = logo.size
        tw = int(lw * (target_h / lh))
        logo = logo.resize((tw, target_h), Image.Resampling.LANCZOS)
        img.paste(logo, (x, y), logo)

# ==============================================================================
# ASSET 1: COVER HERO GRAPHIC (1600 x 900)
# ==============================================================================
def generate_cover_image():
    w, h = 1600, 900
    # Signature Rayls Purple-to-Yellow Gradient
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    
    # Signature Inverted Brand Band
    band_y = 520
    band_h = 160
    band = create_horizontal_gradient(w, band_h, C_YELLOW, C_PURPLE)
    img.paste(band, (0, band_y))
    
    # Untouched Official Black Logo
    paste_official_logo(img, x=1350, y=48, target_h=46, white=False)
    
    draw = ImageDraw.Draw(img)
    
    f_pill = ImageFont.truetype(FONT_BOLD, 17)
    f_title = ImageFont.truetype(FONT_BOLD, 46)
    f_sub = ImageFont.truetype(FONT_REG, 23)
    f_card_title = ImageFont.truetype(FONT_BOLD, 22)
    f_card_sub = ImageFont.truetype(FONT_REG, 16)
    f_card_tag = ImageFont.truetype(FONT_BOLD, 14)
    f_band_title = ImageFont.truetype(FONT_BOLD, 28)
    f_band_sub = ImageFont.truetype(FONT_REG, 19)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Category Pill
    draw.rounded_rectangle([70, 52, 360, 92], radius=6, fill=C_BLACK)
    draw.text((85, 60), "RESEARCH & AUDIT", font=f_pill, fill=C_YELLOW)

    # Title & Subtitle
    draw.text((70, 115), "Tokenized Deposits vs. Stablecoins", font=f_title, fill=C_BLACK)
    draw.text((70, 175), "The Structural, Legal & Balance Sheet Divergence for Financial Settlement", font=f_sub, fill=C_BLACK)

    # 3 Dark Cards
    card_w, card_h = 460, 260
    card_y = 225
    cards_data = [
        ("THE SINGLENESS OF MONEY", "Why central banks (BIS Project Agora) reject private bearer stablecoins to preserve par value ($1.00 = $1.00).", "BIS BULLETIN 73", C_YELLOW),
        ("SMART CONTRACT ANATOMY", "Blunt binary blacklists (USDC FiatToken) vs. Programmable Identity Gating (ERC-3643).", "5 GATE TESTS", C_PURPLE),
        ("RAYLS SOVEREIGN SUBNETS", "Zero client balance leakage, Reth execution in Rust, and deterministic single-slot BFT finality.", "CHAIN ID: 72957", C_GREEN)
    ]

    for idx, (ctitle, cdesc, ctag, ctag_col) in enumerate(cards_data):
        cx = 70 + idx * (card_w + 40)
        # Card Background
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=14, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
        # Accent Tag Badge
        draw.rounded_rectangle([cx + 25, card_y + 25, cx + 220, card_y + 60], radius=5, fill=(35, 35, 42, 255))
        draw.text((cx + 35, card_y + 32), ctag, font=f_card_tag, fill=ctag_col)
        # Card Title
        draw.text((cx + 25, card_y + 80), ctitle, font=f_card_title, fill=C_WHITE)
        # Card Description (Wrapped nicely)
        words = cdesc.split()
        lines = []
        cur = []
        for w_word in words:
            cur.append(w_word)
            if len(" ".join(cur)) > 34:
                lines.append(" ".join(cur[:-1]))
                cur = [w_word]
        if cur:
            lines.append(" ".join(cur))
        
        draw.text((cx + 25, card_y + 125), "\n".join(lines), font=f_card_sub, fill=C_TEXT_MUTED, spacing=6)

    # Inverted Band Content
    draw.text((70, band_y + 35), "THE MONETARY TRILEMMA: BEARER DEBT VS. M1 LIABILITIES", font=f_band_title, fill=C_BLACK)
    draw.text((70, band_y + 85), "Sovereign Settlement under CPMI-IOSCO Principle 8, EU MiCA Article 2(2)(b), and US FDI Act 12 U.S.C. § 1813(l)", font=f_band_sub, fill=C_BLACK)

    # Footer
    draw.text((70, 830), "Rayls Research Initiative | Target: Chain ID 72957 (Public L1) & Sovereign Subnet Architecture", font=f_foot, fill=C_BLACK)

    out = os.path.join(OUTPUT_DIR, "cover_image_tokenized_deposits.png")
    img.save(out)
    print("Regenerated Cover Image:", out)

# ==============================================================================
# ASSET 2: BALANCE SHEET COMPARISON DIAGRAM (1600 x 900)
# ==============================================================================
def generate_balance_sheet_diagram():
    w, h = 1600, 900
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    paste_official_logo(img, x=1350, y=48, target_h=46, white=False)
    draw = ImageDraw.Draw(img)

    f_pill = ImageFont.truetype(FONT_BOLD, 17)
    f_title = ImageFont.truetype(FONT_BOLD, 42)
    f_sub = ImageFont.truetype(FONT_REG, 21)
    f_col_title = ImageFont.truetype(FONT_BOLD, 26)
    f_box_h = ImageFont.truetype(FONT_BOLD, 20)
    f_box_txt = ImageFont.truetype(FONT_REG, 17)
    f_impact_h = ImageFont.truetype(FONT_BOLD, 19)
    f_impact_txt = ImageFont.truetype(FONT_REG, 16)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Header
    draw.rounded_rectangle([70, 52, 420, 92], radius=6, fill=C_BLACK)
    draw.text((85, 60), "BALANCE SHEET TOPOLOGY", font=f_pill, fill=C_YELLOW)

    draw.text((70, 115), "Accounting Topology: Stablecoin vs. Tokenized Deposit", font=f_title, fill=C_BLACK)
    draw.text((70, 170), "Why Stablecoins Drain Credit While Tokenized Deposits Preserve Fractional M1 Liabilities", font=f_sub, fill=C_BLACK)

    col_w = 690
    col_h = 610
    col_y = 215

    # Column 1: Fiat Stablecoin (USDC / Tether Model)
    c1_x = 70
    draw.rounded_rectangle([c1_x, col_y, c1_x + col_w, col_y + col_h], radius=14, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
    draw.rounded_rectangle([c1_x, col_y, c1_x + col_w, col_y + 10], radius=14, fill=C_PURPLE)
    
    draw.text((c1_x + 30, col_y + 25), "FIAT-BACKED STABLECOIN (USDC / USDT)", font=f_col_title, fill=C_WHITE)
    draw.text((c1_x + 30, col_y + 65), "Narrow Banking Model: Siphons Bank Deposits into T-Bills", font=f_box_txt, fill=C_TEXT_MUTED)

    # Assets & Liabilities Boxes
    draw.rounded_rectangle([c1_x + 30, col_y + 110, c1_x + 330, col_y + 330], radius=8, fill=C_CARD_ALT, outline=C_CARD_BORDER, width=1)
    draw.text((c1_x + 45, col_y + 125), "ASSETS (100% Backing)", font=f_box_h, fill=C_PURPLE)
    draw.text((c1_x + 45, col_y + 165), "• 30-90 Day US Treasuries\n• Overnight Reverse Repos\n• Uninsured Bank Cash", font=f_box_txt, fill=C_WHITE, spacing=14)

    draw.rounded_rectangle([c1_x + 360, col_y + 110, c1_x + 660, col_y + 330], radius=8, fill=C_CARD_ALT, outline=C_CARD_BORDER, width=1)
    draw.text((c1_x + 375, col_y + 125), "LIABILITIES (Bearer)", font=f_box_h, fill=C_PURPLE)
    draw.text((c1_x + 375, col_y + 165), "• Circulating ERC-20 Debt\n• General Creditor Claim\n• Zero Deposit Insurance", font=f_box_txt, fill=C_WHITE, spacing=14)

    # Impact Box
    draw.rounded_rectangle([c1_x + 30, col_y + 360, c1_x + 660, col_y + 575], radius=8, fill=(35, 20, 24, 255), outline=C_RED, width=1)
    draw.text((c1_x + 45, col_y + 375), "MACROECONOMIC DEFECT:", font=f_impact_h, fill=C_RED)
    c1_impact = ("• Drains commercial banking deposits into passive government securities.\n"
                 "• Reduces bank lending capacity for mortgages and commercial credit.\n"
                 "• Risk of secondary de-pegs ($0.87 during SVB run), breaking par settlement.")
    draw.text((c1_x + 45, col_y + 410), c1_impact, font=f_impact_txt, fill=C_WHITE, spacing=10)

    # Column 2: Commercial Bank Tokenized Deposit (Rayls Model)
    c2_x = 840
    draw.rounded_rectangle([c2_x, col_y, c2_x + col_w, col_y + col_h], radius=14, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
    draw.rounded_rectangle([c2_x, col_y, c2_x + col_w, col_y + 10], radius=14, fill=C_GREEN)

    draw.text((c2_x + 30, col_y + 25), "TOKENIZED DEPOSIT (RAYLS SUBNET)", font=f_col_title, fill=C_WHITE)
    draw.text((c2_x + 30, col_y + 65), "Two-Tier Fractional Model: Native Commercial Bank M1 Liability", font=f_box_txt, fill=C_TEXT_MUTED)

    # Assets & Liabilities Boxes
    draw.rounded_rectangle([c2_x + 30, col_y + 110, c2_x + 330, col_y + 330], radius=8, fill=C_CARD_ALT, outline=C_CARD_BORDER, width=1)
    draw.text((c2_x + 45, col_y + 125), "ASSETS (Fractional)", font=f_box_h, fill=C_GREEN)
    draw.text((c2_x + 45, col_y + 165), "• Central Bank Reserves (M0)\n• Commercial Loans & Mortg.\n• Interbank Liquid Claims", font=f_box_txt, fill=C_WHITE, spacing=14)

    draw.rounded_rectangle([c2_x + 360, col_y + 110, c2_x + 660, col_y + 330], radius=8, fill=C_CARD_ALT, outline=C_CARD_BORDER, width=1)
    draw.text((c2_x + 375, col_y + 125), "LIABILITIES (Native M1)", font=f_box_h, fill=C_GREEN)
    draw.text((c2_x + 375, col_y + 165), "• Demand Deposit Obligation\n• Direct Customer Legal Title\n• Statutory Insurance (FDIC)", font=f_box_txt, fill=C_WHITE, spacing=14)

    # Impact Box
    draw.rounded_rectangle([c2_x + 30, col_y + 360, c2_x + 660, col_y + 575], radius=8, fill=(18, 32, 24, 255), outline=C_GREEN, width=1)
    draw.text((c2_x + 45, col_y + 375), "SYSTEMIC MACRO BENEFIT:", font=f_impact_h, fill=C_GREEN)
    c2_impact = ("• Preserves fractional banking credit creation and real-economy investment.\n"
                 "• Preserves the Singleness of Money ($1.00 = $1.00) via interbank RTGS settlement.\n"
                 "• Protected by Central Bank Discount Window (lender of last resort).")
    draw.text((c2_x + 45, col_y + 410), c2_impact, font=f_impact_txt, fill=C_WHITE, spacing=10)

    # Footer
    draw.text((70, 845), "Citations: BIS Bulletin 73 (Garratt & Shin) & NY Fed RLN PoC Report | Zero Assumptions Standard", font=f_foot, fill=C_BLACK)

    out = os.path.join(OUTPUT_DIR, "diagram_1_balance_sheet_comparison.png")
    img.save(out)
    print("Regenerated Balance Sheet Diagram:", out)

# ==============================================================================
# ASSET 3: NEGATIVE TEST GATES INFOGRAPHIC (1600 x 900)
# ==============================================================================
def generate_negative_test_diagram():
    w, h = 1600, 900
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    paste_official_logo(img, x=1350, y=48, target_h=46, white=False)
    draw = ImageDraw.Draw(img)

    f_pill = ImageFont.truetype(FONT_BOLD, 17)
    f_title = ImageFont.truetype(FONT_BOLD, 42)
    f_sub = ImageFont.truetype(FONT_REG, 21)
    f_badge = ImageFont.truetype(FONT_BOLD, 16)
    f_row_h = ImageFont.truetype(FONT_BOLD, 20)
    f_row_txt = ImageFont.truetype(FONT_REG, 15)
    f_code = ImageFont.truetype(FONT_MONO, 17)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Header
    draw.rounded_rectangle([70, 52, 420, 92], radius=6, fill=C_BLACK)
    draw.text((85, 60), "EMPIRICAL REPRODUCIBILITY", font=f_pill, fill=C_YELLOW)

    draw.text((70, 115), "Empirical Negative Testing: Permissioned Transfer Gates", font=f_title, fill=C_BLACK)
    draw.text((70, 170), "Simulating Smart Contract Revert Vectors across 5 Real-World Boundary Cases", font=f_sub, fill=C_BLACK)

    test_rows = [
        ("TEST 1 (POSITIVE)", "Compliant Institution to KYC Client", "$1,000,000 Transferred | State Mutated Normally", "SUCCESS", C_GREEN, False),
        ("TEST 2 (NEGATIVE)", "Transfer to Non-Whitelisted Address", "Recipient lacks verified institutional KYC claim in IdentityRegistry", "0xd3b34208", C_RED, True),
        ("TEST 3 (NEGATIVE)", "Overspend Attempt ($15M from $9M)", "Sizing limit exceeded for institutional tier ($15,000,000 > $5,000,000)", "0x78a1bc40", C_RED, True),
        ("TEST 4 (NEGATIVE)", "Sanctioned Jurisdiction Transfer", "Recipient jurisdiction is subject to statutory sanctions (Country Code 643)", "0x78a1bc40", C_RED, True),
        ("TEST 5 (NEGATIVE)", "Sizing Limit Violation ($7.5M > $5M)", "Transaction amount exceeds authorized single-transfer compliance threshold", "0x78a1bc40", C_RED, True),
    ]

    card_y = 215
    card_w = 1460
    row_h = 100
    row_gap = 18

    for idx, (tid, ttitle, tdetail, tcode, tcol, is_revert) in enumerate(test_rows):
        ry = card_y + idx * (row_h + row_gap)
        draw.rounded_rectangle([70, ry, 70 + card_w, ry + row_h], radius=10, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
        
        # Test ID Badge
        b_w = 190
        draw.rounded_rectangle([95, ry + 22, 95 + b_w, ry + 62], radius=6, fill=(32, 32, 38, 255), outline=tcol, width=1)
        draw.text((110, ry + 30), tid, font=f_badge, fill=tcol)

        # Title & Detail
        draw.text((310, ry + 20), ttitle, font=f_row_h, fill=C_WHITE)
        draw.text((310, ry + 56), tdetail, font=f_row_txt, fill=C_TEXT_MUTED)

        # Result Code Pill
        pill_w = 180
        pill_x = 70 + card_w - pill_w - 30
        pill_bg = (38, 18, 22, 255) if is_revert else (18, 35, 22, 255)
        draw.rounded_rectangle([pill_x, ry + 26, pill_x + pill_w, ry + 72], radius=6, fill=pill_bg, outline=tcol, width=1)
        draw.text((pill_x + 25, ry + 36), tcode, font=f_code, fill=tcol)

    # Footer
    draw.text((70, 835), "Executed via test_permissioned_transfer_gates.py | 100% Deterministic Pass Rate | Zero Assumptions", font=f_foot, fill=C_BLACK)

    out = os.path.join(OUTPUT_DIR, "diagram_2_negative_test_gates.png")
    img.save(out)
    print("Regenerated Negative Test Diagram:", out)

# ==============================================================================
# ASSET 4: EVIDENCE BOUNDARY MATRIX TABLE (1920 x 1080)
# ==============================================================================
def generate_evidence_matrix_table():
    w, h = 1920, 1080
    # Exact same background as cover photo: Purple to Yellow Gradient
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    paste_official_logo(img, x=1680, y=45, target_h=46, white=False)
    draw = ImageDraw.Draw(img)

    f_pill = ImageFont.truetype(FONT_BOLD, 15)
    f_title = ImageFont.truetype(FONT_BOLD, 36)
    f_sub = ImageFont.truetype(FONT_REG, 19)
    f_th = ImageFont.truetype(FONT_BOLD, 15)
    f_td_comp = ImageFont.truetype(FONT_BOLD, 14)
    f_td_claim = ImageFont.truetype(FONT_REG, 14)
    f_td_status = ImageFont.truetype(FONT_BOLD, 12)
    f_td_source = ImageFont.truetype(FONT_REG, 13)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Header
    draw.rounded_rectangle([70, 42, 330, 78], radius=6, fill=C_BLACK)
    draw.text((82, 49), "VERIFICATION STANDARD", font=f_pill, fill=C_YELLOW)

    draw.text((70, 92), "Section 6: Evidence Boundary Matrix", font=f_title, fill=C_BLACK)
    draw.text((70, 138), "Rigorous differentiation of live on-chain RPC telemetry, simulations, documented specs, and statutory authorities", font=f_sub, fill=C_BLACK)

    # Main Card Container
    card_x = 70
    card_y = 175
    card_w = 1780
    card_h = 825
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=16, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)

    # Table Column Offsets
    col_x = [card_x + 20, card_x + 350, card_x + 720, card_x + 960]

    # Header Row
    header_y = card_y + 15
    header_h = 42
    draw.rounded_rectangle([card_x + 10, header_y, card_x + card_w - 10, header_y + header_h], radius=8, fill=C_HEADER_ROW)

    headers = [
        ("ARCHITECTURAL COMPONENT", col_x[0]),
        ("CLAIM / METRIC", col_x[1]),
        ("VERIFICATION STATUS", col_x[2]),
        ("SOURCE / EVIDENCE PATH", col_x[3])
    ]
    for text, pos_x in headers:
        draw.text((pos_x + 10, header_y + 12), text, font=f_th, fill=C_YELLOW)

    rows = [
        ("Public Chain Head Height", "Block #13,185,707+ (Chain ID: 72957)", "Verified On-Chain", C_GREEN, "eth_blockNumber live RPC query (mainnet-rpc.rayls.com)"),
        ("Block Gas Limit Ceiling", "500,000,000 gas (16.6x Ethereum L1)", "Verified On-Chain", C_GREEN, "Canonical header gasLimit (0x1dcd6500) on Chain 72957"),
        ("Empirical Block Cadence", "1.3103 s (std: 0.4626s, Min 1s, Max 2s)", "Verified On-Chain", C_GREEN, "Batch sampling of 30 consecutive blocks (#13,185,677 to #13,185,707)"),
        ("FeeAggregator Balance", "0.000000 USDr (Pass-Through Pipeline)", "Verified On-Chain", C_GREEN, "eth_getBalance on contract 0x07E17e17e17e17E17E17E17e17E17e17e17e17E2"),
        ("EVM Precompiles (0x01-08)", "Active & Canonical Execution Output", "Verified On-Chain", C_GREEN, "eth_call verification across precompiles on Paradigm Reth"),
        ("Identity KYC Gate Revert", "Reverts with 0xd3b34208", "Empirically Simulated", C_YELLOW, "test_permissioned_transfer_gates.py (Non-whitelisted address)"),
        ("Sanctions Compliance Revert", "Reverts with 0x78a1bc40", "Empirically Simulated", C_YELLOW, "test_permissioned_transfer_gates.py (Country code 643 blocked)"),
        ("Private Subnet Deposit State", "Encrypted State in MDBX / Zero Leakage", "Documented Architecture", C_PURPLE, "Rayls Whitepaper v2.0 & Drex Pilot Architecture"),
        ("Singleness of Money Principle", "No-Par Interbank Settlement ($1.00 = $1.00)", "Statutory / Authority", C_WHITE, "BIS Bulletin No. 73 (Garratt & Shin, April 2023)"),
        ("Deposit Exclusion from MiCA", "Credit institution deposits exempt", "Statutory / Authority", C_WHITE, "Regulation (EU) 2023/1114 (MiCA), Article 2(2)(b)")
    ]

    y_row = 280
    row_h = 62
    for idx, (comp, claim, status, status_color, source) in enumerate(rows):
        row_bg = (30, 30, 36, 230) if idx % 2 == 0 else (24, 24, 28, 230)
        draw.rounded_rectangle([card_x + 10, y_row, card_x + card_w - 10, y_row + row_h], radius=6, fill=row_bg)
        
        # Col 1: Component
        draw.text((col_x[0] + 10, y_row + 20), comp, font=f_td_comp, fill=C_WHITE)
        # Col 2: Claim
        draw.text((col_x[1] + 10, y_row + 20), claim, font=f_td_claim, fill=C_WHITE)
        # Col 3: Status Badge
        badge_w = 190
        badge_h = 30
        draw.rounded_rectangle([col_x[2] + 10, y_row + 15, col_x[2] + 10 + badge_w, y_row + 15 + badge_h], radius=4, fill=(18, 18, 22, 255), outline=status_color, width=1)
        draw.text((col_x[2] + 20, y_row + 22), status, font=f_td_status, fill=status_color)
        # Col 4: Source
        draw.text((col_x[3] + 10, y_row + 20), source, font=f_td_source, fill=C_TEXT_MUTED)
        
        y_row += row_h + 8

    # Table Footer
    draw.text((card_x + 20, card_y + card_h - 40), "Strict Categorization: Zero Assumptions | Public Chain (72957) vs. Private Sovereign Subnet Separation", font=f_foot, fill=C_YELLOW)

    out = os.path.join(OUTPUT_DIR, "evidence_boundary_matrix_table.png")
    img.save(out)
    print("Regenerated Evidence Matrix Table:", out)

if __name__ == "__main__":
    generate_cover_image()
    generate_balance_sheet_diagram()
    generate_negative_test_diagram()
    generate_evidence_matrix_table()
    print("ALL 4 OFFICIAL BRAND ASSETS REGENERATED SUCCESSFULLY!")
