#!/usr/bin/env python3
"""
generate_adjusted_cover.py
Generates the Cover Image in multiple optimized aspect ratios:
1. Standard 16:9 (1600x900) - Tightened content with generous 120px top/bottom safety padding
2. 2:1 Wide Cover (1600x800) - Standard X/Twitter Article Header
3. 1200x630 (1.91:1) - Standard OpenGraph / Social Share Header
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

def paste_official_logo(img, x, y, target_h=44):
    if os.path.exists(LOGO_BLACK_PATH):
        logo = Image.open(LOGO_BLACK_PATH).convert("RGBA")
        lw, lh = logo.size
        tw = int(lw * (target_h / lh))
        logo = logo.resize((tw, target_h), Image.Resampling.LANCZOS)
        img.paste(logo, (x, y), logo)

def generate_cover_1600x900_safe():
    w, h = 1600, 900
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    
    # Inverted band positioned with plenty of breathing room at bottom
    band_y = 500
    band_h = 135
    band = create_horizontal_gradient(w, band_h, C_YELLOW, C_PURPLE)
    img.paste(band, (0, band_y))
    
    paste_official_logo(img, x=1350, y=45, target_h=44)
    draw = ImageDraw.Draw(img)
    
    f_pill = ImageFont.truetype(FONT_BOLD, 16)
    f_title = ImageFont.truetype(FONT_BOLD, 44)
    f_sub = ImageFont.truetype(FONT_REG, 22)
    f_card_title = ImageFont.truetype(FONT_BOLD, 20)
    f_card_sub = ImageFont.truetype(FONT_REG, 15)
    f_card_tag = ImageFont.truetype(FONT_BOLD, 13)
    f_band_title = ImageFont.truetype(FONT_BOLD, 25)
    f_band_sub = ImageFont.truetype(FONT_REG, 18)
    f_foot = ImageFont.truetype(FONT_REG, 15)

    # Category Pill
    draw.rounded_rectangle([70, 48, 340, 88], radius=6, fill=C_BLACK)
    draw.text((85, 56), "RESEARCH & AUDIT", font=f_pill, fill=C_YELLOW)

    # Title & Subtitle
    draw.text((70, 105), "Tokenized Deposits vs. Stablecoins", font=f_title, fill=C_BLACK)
    draw.text((70, 162), "The Structural, Legal & Balance Sheet Divergence in Banking", font=f_sub, fill=C_BLACK)

    # 3 Dark Cards (Compacted height from 260px -> 230px to prevent bottom cut-off)
    card_w, card_h = 460, 230
    card_y = 220
    cards_data = [
        ("THE SINGLENESS OF MONEY", "Why central banks (BIS Project Agora) reject private bearer stablecoins to preserve par value ($1.00 = $1.00).", "BIS BULLETIN 73", C_YELLOW),
        ("SMART CONTRACT ANATOMY", "Blunt binary blacklists (USDC FiatToken) vs. Programmable Identity Gating (ERC-3643).", "5 GATE TESTS", C_PURPLE),
        ("RAYLS SOVEREIGN SUBNETS", "Zero client balance leakage, Reth execution in Rust, and deterministic single-slot BFT finality.", "CHAIN ID: 72957", C_GREEN)
    ]

    for idx, (ctitle, cdesc, ctag, ctag_col) in enumerate(cards_data):
        cx = 70 + idx * (card_w + 40)
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=12, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
        draw.rounded_rectangle([cx + 25, card_y + 20, cx + 205, card_y + 52], radius=5, fill=(35, 35, 42, 255))
        draw.text((cx + 35, card_y + 26), ctag, font=f_card_tag, fill=ctag_col)
        draw.text((cx + 25, card_y + 68), ctitle, font=f_card_title, fill=C_WHITE)
        
        # Wrapped text
        words = cdesc.split()
        lines, cur = [], []
        for w_word in words:
            cur.append(w_word)
            if len(" ".join(cur)) > 35:
                lines.append(" ".join(cur[:-1]))
                cur = [w_word]
        if cur: lines.append(" ".join(cur))
        draw.text((cx + 25, card_y + 105), "\n".join(lines), font=f_card_sub, fill=C_TEXT_MUTED, spacing=5)

    # Inverted Band Content (Compact & Centered)
    draw.text((70, band_y + 25), "THE MONETARY TRILEMMA: BEARER DEBT VS. M1 LIABILITIES", font=f_band_title, fill=C_BLACK)
    draw.text((70, band_y + 70), "Sovereign Settlement under CPMI-IOSCO Principle 8, EU MiCA Article 2(2)(b), and US FDI Act 12 U.S.C. § 1813(l)", font=f_band_sub, fill=C_BLACK)

    # Footer (Shifted UP to y=720 with safe bottom margin!)
    draw.text((70, 715), "Rayls Research Initiative | Target: Chain ID 72957 (Public L1) & Sovereign Subnet Architecture", font=f_foot, fill=C_BLACK)
    draw.text((70, 745), "Zero Assumptions Standard | Source Repository: github.com/9ytshade/rayls-tokenized-deposits-vs-stablecoins", font=f_foot, fill=C_BLACK)

    out = os.path.join(OUTPUT_DIR, "cover_image_tokenized_deposits.png")
    img.save(out)
    print("Regenerated 1600x900 Safe Cover:", out)

def generate_cover_1600x800_x_article():
    # Dedicated 2:1 ratio for X Articles and Web Headers
    w, h = 1600, 800
    img = create_horizontal_gradient(w, h, C_PURPLE, C_YELLOW)
    paste_official_logo(img, x=1350, y=40, target_h=42)
    draw = ImageDraw.Draw(img)

    f_pill = ImageFont.truetype(FONT_BOLD, 15)
    f_title = ImageFont.truetype(FONT_BOLD, 40)
    f_sub = ImageFont.truetype(FONT_REG, 20)
    f_card_title = ImageFont.truetype(FONT_BOLD, 18)
    f_card_sub = ImageFont.truetype(FONT_REG, 14)
    f_card_tag = ImageFont.truetype(FONT_BOLD, 12)
    f_foot = ImageFont.truetype(FONT_REG, 14)

    draw.rounded_rectangle([70, 42, 320, 78], radius=6, fill=C_BLACK)
    draw.text((85, 49), "RESEARCH & AUDIT", font=f_pill, fill=C_YELLOW)

    draw.text((70, 95), "Tokenized Deposits vs. Stablecoins", font=f_title, fill=C_BLACK)
    draw.text((70, 148), "The Structural, Legal & Balance Sheet Divergence in Banking", font=f_sub, fill=C_BLACK)

    card_w, card_h = 460, 205
    card_y = 195
    cards_data = [
        ("THE SINGLENESS OF MONEY", "Why central banks (BIS Project Agora) reject private bearer stablecoins to preserve par value ($1.00 = $1.00).", "BIS BULLETIN 73", C_YELLOW),
        ("SMART CONTRACT ANATOMY", "Blunt binary blacklists (USDC FiatToken) vs. Programmable Identity Gating (ERC-3643).", "5 GATE TESTS", C_PURPLE),
        ("RAYLS SOVEREIGN SUBNETS", "Zero client balance leakage, Reth execution in Rust, and deterministic single-slot BFT finality.", "CHAIN ID: 72957", C_GREEN)
    ]

    for idx, (ctitle, cdesc, ctag, ctag_col) in enumerate(cards_data):
        cx = 70 + idx * (card_w + 40)
        draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=10, fill=C_CARD_BG, outline=C_CARD_BORDER, width=2)
        draw.rounded_rectangle([cx + 20, card_y + 18, cx + 180, card_y + 46], radius=4, fill=(35, 35, 42, 255))
        draw.text((cx + 30, card_y + 24), ctag, font=f_card_tag, fill=ctag_col)
        draw.text((cx + 20, card_y + 60), ctitle, font=f_card_title, fill=C_WHITE)
        
        words = cdesc.split()
        lines, cur = [], []
        for w_word in words:
            cur.append(w_word)
            if len(" ".join(cur)) > 36:
                lines.append(" ".join(cur[:-1]))
                cur = [w_word]
        if cur: lines.append(" ".join(cur))
        draw.text((cx + 20, card_y + 95), "\n".join(lines), font=f_card_sub, fill=C_TEXT_MUTED, spacing=4)

    # Inverted band
    band_y = 450
    band_h = 120
    band = create_horizontal_gradient(w, band_h, C_YELLOW, C_PURPLE)
    img.paste(band, (0, band_y))

    f_band_title = ImageFont.truetype(FONT_BOLD, 22)
    f_band_sub = ImageFont.truetype(FONT_REG, 16)
    draw.text((70, band_y + 20), "THE MONETARY TRILEMMA: BEARER DEBT VS. M1 LIABILITIES", font=f_band_title, fill=C_BLACK)
    draw.text((70, band_y + 60), "Sovereign Settlement under CPMI-IOSCO Principle 8, EU MiCA Article 2(2)(b), and US FDI Act 12 U.S.C. § 1813(l)", font=f_band_sub, fill=C_BLACK)

    draw.text((70, 630), "Rayls Research Initiative | Target: Chain ID 72957 (Public L1) & Sovereign Subnet Architecture", font=f_foot, fill=C_BLACK)
    draw.text((70, 660), "Zero Assumptions Standard | Source Repository: github.com/9ytshade/rayls-tokenized-deposits-vs-stablecoins", font=f_foot, fill=C_BLACK)

    out = os.path.join(OUTPUT_DIR, "cover_image_x_article_1600x800.png")
    img.save(out)
    print("Generated 1600x800 Cover:", out)

if __name__ == "__main__":
    generate_cover_1600x900_safe()
    generate_cover_1600x800_x_article()
