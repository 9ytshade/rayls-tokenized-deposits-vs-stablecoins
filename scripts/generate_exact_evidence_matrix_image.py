#!/usr/bin/env python3
"""
generate_exact_evidence_matrix_image.py
Generates the Complete 20-Row Evidence Boundary Matrix Infographic
Matches 100% identically with Section 6 of TOKENIZED_DEPOSITS_VS_STABLECOINS_INVESTIGATION.md
Canvas: 1920 x 1750 (High-Resolution Long Infographic)
Palette: Noir Ventures Rayls Brand Guide (Purple to Yellow gradient, deep dark card, color-coded status badges)
"""

import os
from PIL import Image, ImageDraw, ImageFont

C_BLACK = (17, 17, 17, 255)         # #111111
C_WHITE = (255, 255, 255, 255)       # #FFFFFF
C_YELLOW = (236, 251, 62, 255)       # #ECFB3E Primary Accent
C_PURPLE = (180, 154, 255, 255)      # #B49AFF Primary Accent
C_GREEN = (140, 247, 139, 255)       # #8CF78B Secondary Accent
C_CARD_BG = (24, 24, 28, 248)
C_CARD_BORDER = (55, 55, 65, 255)
C_HEADER_ROW = (18, 18, 22, 255)
C_TEXT_MUTED = (160, 160, 175, 255)

FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_REG = "C:/Windows/Fonts/segoeui.ttf"

LOGO_BLACK_PATH = "c:/Users/9ytshade/Desktop/Rayls/Brand_Guide/Rayls_Logo_Pack/PNG/Rayls_Logo_Black.png"
OUTPUT_DIR = r"c:\Users\9ytshade\Desktop\Rayls\Week_4_Tokenized_Deposits_vs_Stablecoins\diagrams"

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

def paste_official_logo(img, x, y, target_h=46):
    if os.path.exists(LOGO_BLACK_PATH):
        logo = Image.open(LOGO_BLACK_PATH).convert("RGBA")
        lw, lh = logo.size
        tw = int(lw * (target_h / lh))
        logo = logo.resize((tw, target_h), Image.Resampling.LANCZOS)
        img.paste(logo, (x, y), logo)

def main():
    w, h = 1920, 1750
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    paste_official_logo(img, x=1680, y=45, target_h=46)
    draw = ImageDraw.Draw(img)

    f_pill = ImageFont.truetype(FONT_BOLD, 15)
    f_title = ImageFont.truetype(FONT_BOLD, 36)
    f_sub = ImageFont.truetype(FONT_REG, 19)
    f_th = ImageFont.truetype(FONT_BOLD, 15)
    f_td_comp = ImageFont.truetype(FONT_BOLD, 13)
    f_td_claim = ImageFont.truetype(FONT_REG, 13)
    f_td_status = ImageFont.truetype(FONT_BOLD, 11)
    f_td_source = ImageFont.truetype(FONT_REG, 13)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Header
    draw.rounded_rectangle([70, 42, 330, 78], radius=6, fill=C_BLACK)
    draw.text((82, 49), "VERIFICATION STANDARD", font=f_pill, fill=C_YELLOW)

    draw.text((70, 92), "Section 6: Complete Evidence Boundary Matrix", font=f_title, fill=C_BLACK)
    draw.text((70, 138), "Rigorous classification of on-chain telemetry, empirical simulations, documented architecture, and statutory authorities", font=f_sub, fill=C_BLACK)

    # Main Card Container for All 20 Rows
    card_x = 70
    card_y = 175
    card_w = 1780
    card_h = 1500
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

    # All 20 Exact Rows Matching the Markdown Article 1:1
    rows = [
        ("Public Chain Head Height", "Block #13,185,707+ (Chain ID: 72957)", "Verified On-Chain", C_GREEN, "Live eth_blockNumber via mainnet-rpc.rayls.com (Chain ID 72957)"),
        ("Node Client Software", "Reth / Axyl v1.4.1 (Commit: 6909618b)", "Verified On-Chain", C_GREEN, "web3_clientVersion querying node software identity"),
        ("Canonical Block Gas Limit", "500,000,000 gas (16.6x Ethereum L1)", "Verified On-Chain", C_GREEN, "Header inspection (0x1dcd6500) of canonical blocks"),
        ("Empirical Block Cadence", "1.3103 seconds (std: 0.4626s)", "Verified On-Chain", C_GREEN, "Batch query of 30 consecutive blocks (#13,185,677 to #13,185,707)"),
        ("FeeAggregator Proxy State", "Implementation at 0x9bd6...1fd2", "Verified On-Chain", C_GREEN, "EIP-1967 storage slot query (0x3608...2bbc) on contract 0x07E1...17E2"),
        ("FeeAggregator Balance", "0.000000 USDr (Pass-Through)", "Verified On-Chain", C_GREEN, "eth_getBalance querying contract 0x07E17e17e17e17E17E17E17e17E17e17e17e17E2"),
        ("EVM Precompile Execution", "0x01 through 0x08 Active", "Verified On-Chain", C_GREEN, "Direct eth_call queries to precompiles on Paradigm Reth"),
        ("Identity Gate Revert", "Reverts with 0xd3b34208", "Empirically Simulated", C_YELLOW, "test_permissioned_transfer_gates.py (Test 2: Non-whitelisted address)"),
        ("Sanctions Gate Revert", "Reverts with 0x78a1bc40", "Empirically Simulated", C_YELLOW, "test_permissioned_transfer_gates.py (Test 4: Country code 643)"),
        ("Overspend Revert", "Reverts with 0x78a1bc40", "Empirically Simulated", C_YELLOW, "test_permissioned_transfer_gates.py (Test 3: $15M from $9M balance)"),
        ("Public vs. Subnet Gas Cost", "$4.55 (Eth L1) vs $0.000045 (Subnet)", "Empirically Simulated", C_YELLOW, "benchmark_settlement_cost_and_gas.py economic model"),
        ("Private Subnet Deposit State", "Encrypted State in MDBX / Zero Leakage", "Documented Architecture", C_PURPLE, "Rayls Core Whitepaper v2.0 & Drex Pilot Architecture"),
        ("Privacy Hub ZK Verification", "alt_bn128 proof verification", "Documented Architecture", C_PURPLE, "Rayls Enygma Cryptographic Specifications"),
        ("Target Design Cadence", "~697 ms (Sub-second target)", "Documented Architecture", C_PURPLE, "Rayls Benchmark Documentation (Live parameter is 1.31s)"),
        ("Singleness of Money Principle", "Par exchangeability ($1.00 = $1.00)", "Statutory / Authority", C_WHITE, "BIS Bulletin No. 73 (Garratt & Shin, April 2023)"),
        ("Interbank Tokenized Deposits", "Shared programmable ledger model", "Statutory / Authority", C_WHITE, "BIS Project Agora Interim Reports (2024-2026)"),
        ("Deposit Exclusion from MiCA", "Credit institution deposits exempt", "Statutory / Authority", C_WHITE, "Regulation (EU) 2023/1114 (MiCA), Article 2(2)(b) & Recital 12"),
        ("US Bank Deposit Definition", "Commercial bank deposit liabilities", "Statutory / Authority", C_WHITE, "Federal Deposit Insurance Act (FDI Act), 12 U.S.C. Section 1813(l)"),
        ("US RLN Shared Ledger Feasibility", "Feasible within existing US law", "Statutory / Authority", C_WHITE, "Federal Reserve Bank of New York (NYIC) RLN Report (2023)"),
        ("Brazilian Banking Secrecy Law", "Confidentiality of financial ops", "Statutory / Authority", C_WHITE, "Brazil Complementary Law No. 105 (Lei Complementar 105/2001)")
    ]

    y_row = 230
    row_h = 58
    row_gap = 6
    for idx, (comp, claim, status, status_color, source) in enumerate(rows):
        row_bg = (30, 30, 36, 230) if idx % 2 == 0 else (24, 24, 28, 230)
        draw.rounded_rectangle([card_x + 10, y_row, card_x + card_w - 10, y_row + row_h], radius=6, fill=row_bg)
        
        # Col 1: Component
        draw.text((col_x[0] + 10, y_row + 18), comp, font=f_td_comp, fill=C_WHITE)
        # Col 2: Claim
        draw.text((col_x[1] + 10, y_row + 18), claim, font=f_td_claim, fill=C_WHITE)
        # Col 3: Status Badge
        badge_w = 190
        badge_h = 28
        draw.rounded_rectangle([col_x[2] + 10, y_row + 14, col_x[2] + 10 + badge_w, y_row + 14 + badge_h], radius=4, fill=(18, 18, 22, 255), outline=status_color, width=1)
        draw.text((col_x[2] + 20, y_row + 19), status, font=f_td_status, fill=status_color)
        # Col 4: Source (Cleaned and matched 1:1)
        draw.text((col_x[3] + 10, y_row + 18), source, font=f_td_source, fill=C_TEXT_MUTED)
        
        y_row += row_h + row_gap

    # Table Footer
    draw.text((card_x + 20, card_y + card_h - 40), "Strict Categorization: Zero Assumptions | Public Chain (72957) vs. Private Sovereign Subnet Separation", font=f_foot, fill=C_YELLOW)

    out = os.path.join(OUTPUT_DIR, "evidence_boundary_matrix_table.png")
    img.save(out)
    print("Regenerated Complete 20-Row Evidence Matrix Table:", out)

if __name__ == "__main__":
    main()
