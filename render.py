#!/usr/bin/env python3
"""Build-time renderer for the news-image-20261126 v2 entry.

Renders entry.png (1024x1024) from the verified 26 November 2026 story
list using Pillow. This script runs only at build time on the author's
machine; the graded program is main.py, which merely copies entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
W, H = 1024, 1024

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = font("DejaVuSans-Bold.ttf", 34)
F_SUB = font("DejaVuSans.ttf", 13)
F_LEAD = font("DejaVuSans-Bold.ttf", 30)
F_LEAD_BODY = font("DejaVuSans.ttf", 15)
F_TAG = font("DejaVuSans-Bold.ttf", 11)
F_SEC = font("DejaVuSans-Bold.ttf", 13)
F_LEGEND = font("DejaVuSans.ttf", 11)
F_TIME = font("DejaVuSans-Bold.ttf", 12)
F_TL = font("DejaVuSans.ttf", 10)
F_CELL_TAG = font("DejaVuSans-Bold.ttf", 9)
F_CELL_HEAD = font("DejaVuSans-Bold.ttf", 13)
F_CELL_SUB = font("DejaVuSans.ttf", 10)
F_FOOT = font("DejaVuSans.ttf", 11)

PAPER = (247, 243, 234, 255)
INK = (20, 33, 61, 255)
NAVY = (20, 33, 61, 255)
RED = (192, 57, 43, 255)
TEAL = (14, 124, 123, 255)
GOLD = (217, 164, 65, 255)
WHITE = (255, 255, 255, 255)
CARD = (255, 255, 255, 255)
LINE = (200, 192, 172, 255)
OCEAN = (214, 231, 242, 255)
LAND = (232, 220, 195, 255)
LAND_LINE = (138, 123, 92, 255)
GREY = (90, 90, 90, 255)

REGION_COLORS = {
    "N. AMERICA": (31, 119, 180, 255),
    "LATIN AMERICA": (44, 160, 44, 255),
    "EUROPE": (127, 60, 141, 255),
    "MIDDLE EAST": (192, 57, 43, 255),
    "AFRICA": (214, 120, 30, 255),
    "SOUTH ASIA": (188, 40, 110, 255),
    "EAST ASIA": (14, 124, 123, 255),
    "SE ASIA": (90, 140, 20, 255),
    "OCEANIA": (30, 110, 160, 255),
    "TECH & SPACE": (100, 100, 100, 255),
    "CULTURE": (150, 110, 40, 255),
}

# (region, headline, detail) — 39 grid stories; the lead story is separate.
STORIES = [
    ("N. AMERICA", "Nasdaq 100 nears bear market", "-4.6% intraday; closed -0.6%"),
    ("N. AMERICA", "Birthright order blocked again", "Second judge halts Trump order"),
    ("N. AMERICA", "Nvidia faces antitrust questions", "Booker presses on Huang return"),
    ("N. AMERICA", "Army blows up old explosives", "Lead stockpile detonated in Iowa"),
    ("LATIN AMERICA", "Ecuador reviews US operations", "Talks focused on review"),
    ("EUROPE", "UK migration lowest since 1997", "77,000; -90% from 2023 peak"),
    ("EUROPE", "Serbia election set for Dec 27", "Presidential vote date confirmed"),
    ("EUROPE", "Murmansk governor detained", "Two months' pre-trial custody"),
    ("EUROPE", "34 nations: halt riot gas in Ukraine", "Call on Russia to halt use"),
    ("EUROPE", "Ukraine hits Russian air base", "Five planes damaged, Kyiv says"),
    ("EUROPE", "Kyiv hit by ballistic missiles", "Shopping centre among targets"),
    ("EUROPE", "Cologne synagogue plot foiled", "Two Iraqis arrested in Germany"),
    ("EUROPE", "De Cos tipped to lead ECB", "EU to nominate Spaniard"),
    ("EUROPE", "Norse Atlantic warns on survival", "Flights halted; survival risk"),
    ("MIDDLE EAST", "Lebanon to open 2nd airport", "Opens next month in the north"),
    ("MIDDLE EAST", "Judges: drop Netanyahu bribery case", "Conviction 'unlikely', panel says"),
    ("MIDDLE EAST", "Israel kills nine in Gaza", "Includes Hamas-appointed minister"),
    ("MIDDLE EAST", "Houthis claim Ras Tanura strike", "Saudi Arabia's largest refinery"),
    ("MIDDLE EAST", "Mines hit two Hormuz tankers", "Supertanker ablaze off Khasab"),
    ("MIDDLE EAST", "Brent jumps 3.5% to $94.61", "Supply fears lift crude prices"),
    ("MIDDLE EAST", "Projectile hits Saudi Jizan port", "Minor damage, Riyadh says"),
    ("AFRICA", "Cairo tanker fire kills 31", "21 hurt on the Ring Road"),
    ("AFRICA", "Ebola passes 12,000 in Congo", "12,021 cases; ~half died"),
    ("AFRICA", "Kenya cult leader convicted again", "Mackenzie faces fresh charges"),
    ("AFRICA", "Kenya court voids Ebola site", "US-backed quarantine 'unlawful'"),
    ("SOUTH ASIA", "Myanmar defies ICJ orders", "Naypyidaw rejects ICJ orders"),
    ("SOUTH ASIA", "Bangladesh garment wage up 36%", "17,000 taka/month from Jan"),
    ("SOUTH ASIA", "India tightens food labelling", "Court: end 'double standards'"),
    ("SOUTH ASIA", "Mecca alliance talks planned", "Meet in Mecca Nov 27-28"),
    ("EAST ASIA", "First Pakistani reaches Tiangong", "Shenzhou-24 docks with station"),
    ("EAST ASIA", "China got Nvidia chips anyway", "Despite US curbs, Reuters finds"),
    ("EAST ASIA", "Kospi plunges 6.2%", "Samsung -9.9%, SK Hynix -11%"),
    ("EAST ASIA", "Bank of Korea hikes to 3.25%", "Highest rate in two years"),
    ("EAST ASIA", "FCC clears 1m SpaceX satellites", "Orbital data centres in space"),
    ("SE ASIA", "Bangkok refinery fire shuts plant", "Bangchak closes all units"),
    ("OCEANIA", "Solomons picks Australia partner", "No foreign base; $740m pact"),
    ("CULTURE", "Duran Duran's Andy Taylor dies", "Guitarist was 65; cancer battle"),
    ("EAST ASIA", "Japan data-centre revolt grows", "Residents push back in Kashiwa"),
    ("TECH & SPACE", "StanChart crypto unit breached", "Zodia: some client data exposed"),
]

# (utc time, label) for the timeline strip.
TIMELINE = [
    ("00:18", "Shenzhou-24 lifts off"),
    ("03:56", "Docks at Tiangong"),
    ("06:30", "Kospi closes -6.2%"),
    ("09:47", "UK migration data"),
    ("13:50", "Netanyahu judges speak"),
    ("~15:00", "Tariffs unveiled"),
    ("~19:00", "Nasdaq near bear"),
]

# (number, label, lon, lat) — map markers.
MARKERS = [
    (1, "N. AMERICA", -100, 45),
    (2, "LATIN AMERICA", -60, -15),
    (3, "EUROPE", 15, 52),
    (4, "MIDDLE EAST", 45, 30),
    (5, "AFRICA", 20, 5),
    (6, "SOUTH ASIA", 78, 22),
    (7, "EAST ASIA", 115, 35),
    (8, "SE ASIA", 105, 10),
    (9, "OCEANIA", 148, -28),
    (10, "RUSSIA", 95, 62),
]

# Rough continent outlines as (lon, lat) lists.
N_AMERICA = [(-168, 66), (-150, 70), (-140, 70), (-130, 71), (-120, 73),
             (-105, 73), (-95, 80), (-85, 73), (-80, 73), (-75, 72),
             (-65, 60), (-60, 55), (-55, 52), (-60, 46), (-65, 44),
             (-70, 42), (-75, 38), (-76, 35), (-80, 32), (-81, 26),
             (-85, 29), (-90, 21), (-94, 18), (-97, 16), (-95, 19),
             (-100, 20), (-105, 21), (-110, 24), (-115, 29), (-120, 34),
             (-124, 40), (-124, 48), (-130, 55), (-140, 60), (-150, 59),
             (-160, 58), (-165, 60), (-168, 66)]
GREENLAND = [(-58, 64), (-52, 60), (-44, 60), (-40, 64), (-32, 68),
             (-22, 70), (-25, 74), (-35, 76), (-50, 76), (-58, 74),
             (-58, 64)]
S_AMERICA = [(-80, 10), (-75, 11), (-71, 12), (-64, 10), (-60, 8),
             (-53, 5), (-50, 0), (-44, -3), (-35, -8), (-38, -13),
             (-40, -20), (-44, -24), (-48, -28), (-53, -33), (-58, -35),
             (-62, -39), (-65, -41), (-68, -46), (-69, -51), (-70, -54),
             (-73, -50), (-74, -44), (-73, -37), (-72, -30), (-71, -22),
             (-70, -18), (-75, -15), (-79, -8), (-81, -4), (-80, 1),
             (-80, 10)]
AFRICA = [(-17, 15), (-17, 21), (-13, 27), (-10, 31), (-5, 35),
          (0, 36), (10, 37), (11, 34), (15, 32), (20, 32), (25, 32),
          (30, 31), (32, 31), (34, 28), (36, 24), (37, 20), (39, 18),
          (42, 15), (44, 11), (48, 11), (51, 12), (48, 7), (45, 2),
          (41, -2), (40, -7), (38, -12), (36, -18), (34, -22), (32, -26),
          (29, -30), (27, -33), (22, -35), (19, -34), (17, -30),
          (15, -27), (13, -22), (12, -16), (12, -10), (13, -5), (10, 0),
          (9, 4), (5, 5), (0, 6), (-5, 5), (-8, 5), (-12, 8),
          (-15, 11), (-17, 15)]
EURASIA = [(-10, 36), (-9, 40), (-9, 43), (-4, 48), (-2, 49), (0, 50),
           (2, 51), (5, 53), (7, 54), (8, 57), (10, 58), (12, 56),
           (18, 56), (21, 55), (23, 58), (25, 59), (28, 60), (30, 61),
           (32, 65), (35, 66), (40, 68), (45, 68), (50, 69), (55, 69),
           (60, 69), (65, 71), (70, 72), (75, 72), (80, 73), (85, 74),
           (90, 75), (95, 76), (100, 76), (105, 76), (110, 74), (115, 73),
           (120, 73), (125, 72), (130, 71), (135, 71), (140, 72),
           (145, 72), (150, 70), (155, 69), (160, 69), (165, 68),
           (170, 67), (175, 66), (178, 65), (178, 62), (175, 62),
           (170, 60), (165, 59), (162, 56), (158, 52), (155, 59),
           (150, 59), (145, 58), (142, 55), (141, 52), (140, 48),
           (138, 45), (135, 43), (132, 42), (130, 42), (127, 40),
           (126, 38), (124, 39), (122, 38), (120, 35), (120, 31),
           (118, 28), (115, 24), (112, 22), (110, 21), (108, 18),
           (107, 12), (105, 10), (104, 8), (102, 7), (100, 7), (99, 9),
           (98, 11), (96, 15), (94, 17), (92, 21), (91, 22), (89, 22),
           (87, 21), (85, 19), (82, 17), (80, 14), (78, 9), (76, 9),
           (75, 12), (74, 15), (73, 18), (72, 20), (70, 21), (68, 23),
           (66, 25), (64, 25), (62, 25), (60, 25), (58, 26), (56, 27),
           (54, 27), (52, 27), (50, 29), (49, 30), (48, 30), (46, 29),
           (44, 29), (42, 30), (40, 31), (38, 32), (36, 36), (34, 36),
           (32, 36), (30, 36), (28, 37), (26, 38), (24, 36), (22, 37),
           (20, 39), (18, 40), (16, 41), (14, 42), (12, 44), (10, 44),
           (8, 44), (6, 43), (3, 43), (0, 43), (-2, 44), (-2, 47),
           (-4, 48), (-6, 48), (-8, 46), (-9, 43), (-10, 37), (-10, 36)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-4, 58), (-2, 58), (-1, 57),
      (0, 54), (1, 52), (1, 51), (-3, 50), (-5, 50)]
JAPAN = [(130, 31), (132, 33), (134, 34), (136, 35), (138, 35),
         (139, 36), (140, 38), (141, 40), (142, 42), (144, 44),
         (142, 45), (140, 43), (140, 40), (139, 38), (137, 37),
         (135, 34), (132, 33), (130, 31)]
AUSTRALIA = [(114, -22), (114, -28), (115, -32), (116, -35), (120, -34),
             (124, -33), (129, -32), (132, -32), (135, -35), (138, -35),
             (140, -38), (144, -38), (147, -39), (150, -37), (153, -32),
             (153, -27), (151, -24), (148, -20), (146, -19), (144, -15),
             (142, -12), (142, -11), (139, -14), (137, -12), (135, -13),
             (133, -12), (131, -12), (129, -14), (126, -14), (123, -16),
             (120, -19), (117, -20), (114, -22)]
NEW_GUINEA = [(131, -1), (135, -2), (138, -3), (141, -3), (144, -4),
              (147, -6), (150, -8), (148, -9), (145, -8), (142, -8),
              (139, -7), (136, -4), (133, -3), (131, -1)]
BORNEO = [(109, 1), (111, 2), (114, 3), (117, 5), (119, 4), (119, 0),
          (117, -2), (115, -3), (112, -3), (110, -2), (109, 1)]
SUMATRA = [(95, 5), (98, 3), (101, 0), (104, -3), (106, -5), (104, -5),
           (101, -2), (98, 1), (95, 5)]
MADAGASCAR = [(44, -16), (47, -15), (50, -16), (49, -20), (47, -24),
              (45, -25), (44, -21), (44, -16)]
NZ = [(167, -45), (170, -43), (173, -41), (175, -38), (177, -38),
      (175, -40), (173, -42), (170, -44), (167, -45)]
CONTINENTS = [N_AMERICA, GREENLAND, S_AMERICA, AFRICA, EURASIA, UK,
              JAPAN, AUSTRALIA, NEW_GUINEA, BORNEO, SUMATRA, MADAGASCAR, NZ]


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines (max 2, second may end ...)."""
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    if len(lines) > 2:
        second = lines[1]
        while len(second) > 3 and draw.textlength(second + "...", font=fnt) > max_w:
            second = second.rsplit(" ", 1)[0]
        lines = [lines[0], second + "..."]
    return lines


def trunc(draw, text, fnt, max_w):
    """Truncate a single line with an ellipsis if it is too wide."""
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while len(text) > 3 and draw.textlength(text + "...", font=fnt) > max_w:
        text = text.rsplit(" ", 1)[0] if " " in text else text[:-1]
    return text + "..."


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- header ----------
    d.rectangle([0, 0, W, 82], fill=NAVY)
    d.rectangle([0, 82, W, 86], fill=RED)
    d.text((16, 12), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=WHITE)
    d.text((16, 54), "THURSDAY 26 NOVEMBER 2026  ·  40 STORIES  ·  11 REGIONS",
           font=F_SUB, fill=(200, 210, 225, 255))
    d.text((W - 16, 54), "EBOLA 12,021  ·  CAIRO 31 DEAD  ·  KOSPI -6.2%  ·  BRENT $94.61",
           font=F_SUB, fill=GOLD, anchor="ra")

    # ---------- lead story ----------
    ly0, ly1 = 96, 208
    d.rectangle([12, ly0, W - 12, ly1], fill=CARD, outline=LINE, width=1)
    d.rectangle([12, ly0, 20, ly1], fill=RED)
    d.text((32, ly0 + 8), "LEAD STORY", font=F_TAG, fill=RED)
    d.text((32, ly0 + 28), "US proposes tariffs on 14 economies",
           font=F_LEAD, fill=INK)
    lead_body = ("USTR's Section 301 plan targets 'excess capacity': "
                 "China up to 20% (40% if the truce fails), Vietnam 35%, "
                 "the EU 15%. Hearing Jan 25.")
    lines = wrap(d, lead_body, F_LEAD_BODY, 640)
    y = ly0 + 68
    for ln in lines[:2]:
        d.text((32, y), ln, font=F_LEAD_BODY, fill=(50, 50, 50, 255))
        y += 19
    # small tariff-bars illustration on the right of the lead card
    bx, by = 740, ly0 + 18
    bars = [("CHN", 20, 25), ("VNM", 35, 44), ("IND", 25, 31), ("EU", 15, 19)]
    d.text((bx, by), "PROPOSED TOP RATES", font=F_CELL_TAG, fill=GREY)
    baseline = by + 72
    x = bx
    for name, rate, hgt in bars:
        d.rectangle([x, baseline - hgt, x + 34, baseline], fill=RED)
        d.text((x + 17, baseline + 4), name, font=F_CELL_TAG, fill=INK,
               anchor="ma")
        d.text((x + 17, baseline - hgt - 13), str(rate) + "%", font=F_CELL_TAG,
               fill=RED, anchor="ma")
        x += 52

    # ---------- world map (correct-aspect, centred) + region key ----------
    my0, my1 = 218, 400
    d.rectangle([12, my0, W - 12, my1], fill=OCEAN, outline=LINE, width=1)
    d.text((24, my0 + 6), "WHERE IT HAPPENED — 10 REGIONS ON THE MAP",
           font=F_SEC, fill=INK)
    map_x0, map_x1 = 20, 540
    map_y0, map_y1 = my0 + 28, my1 - 4
    lat_top, lat_bot = 78.0, -58.0
    scale = min((map_x1 - map_x0) / 360.0, (map_y1 - map_y0) / (lat_top - lat_bot))
    map_w, map_h = 360.0 * scale, (lat_top - lat_bot) * scale
    ox = map_x0 + (map_x1 - map_x0 - map_w) / 2
    oy = map_y0 + (map_y1 - map_y0 - map_h) / 2
    def proj(lon, lat):
        return (ox + (lon + 180.0) * scale, oy + (lat_top - lat) * scale)
    for lat in (60, 30, 0, -30):
        _, gy = proj(0, lat)
        d.line([(ox, gy), (ox + map_w, gy)], fill=(190, 208, 222, 255), width=1)
    for poly in CONTINENTS:
        d.polygon([proj(lo, la) for lo, la in poly], fill=LAND,
                  outline=LAND_LINE)
    for num, _lbl, lon, lat in MARKERS:
        cx, cy = proj(lon, lat)
        d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=RED,
                  outline=WHITE, width=2)
        d.text((cx, cy), str(num), font=F_CELL_TAG, fill=WHITE, anchor="mm")
    # region key on the right of the map
    kx = 570
    d.text((kx, my0 + 6), "REGIONS", font=F_SEC, fill=INK)
    for i, (num, lbl, _lo, _la) in enumerate(MARKERS):
        col_i, row_i = divmod(i, 5)
        kx_i = kx + col_i * 220
        ky_i = my0 + 34 + row_i * 30
        d.ellipse([kx_i, ky_i, kx_i + 20, ky_i + 20], fill=RED)
        d.text((kx_i + 10, ky_i + 10), str(num), font=F_CELL_TAG, fill=WHITE,
               anchor="mm")
        d.text((kx_i + 27, ky_i + 4), lbl, font=F_LEGEND, fill=INK)

    # ---------- UTC timeline ----------
    ty0, ty1 = 410, 472
    d.rectangle([12, ty0, W - 12, ty1], fill=NAVY)
    d.text((24, ty0 + 5), "THE DAY IN UTC  ·  TIMES APPROXIMATE",
           font=F_SEC, fill=GOLD)
    line_y = ty0 + 40
    d.line([(32, line_y), (W - 32, line_y)], fill=(120, 135, 160, 255), width=2)
    n = len(TIMELINE)
    for i, (t, lbl) in enumerate(TIMELINE):
        cx = 48 + i * (W - 96) / (n - 1)
        d.ellipse([cx - 5, line_y - 5, cx + 5, line_y + 5], fill=GOLD,
                  outline=WHITE, width=1)
        d.text((cx, line_y - 20), t, font=F_TIME, fill=WHITE, anchor="ma")
        half = d.textlength(lbl, font=F_TL) / 2
        lx = min(max(cx, half + 14), W - half - 14)
        d.text((lx, line_y + 8), lbl, font=F_TL, fill=(210, 220, 235, 255),
               anchor="ma")

    # ---------- story grid: 5 columns x 8 rows ----------
    gx0, gy0 = 12, 482
    cols, rows = 5, 8
    cell_w = (W - 2 * gx0 - (cols - 1) * 4) // cols
    cell_h = (1006 - gy0 - (rows - 1) * 4) // rows
    for idx, (region, head, sub) in enumerate(STORIES):
        r, c = divmod(idx, cols)
        x0 = gx0 + c * (cell_w + 4)
        y0 = gy0 + r * (cell_h + 4)
        d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h], fill=CARD,
                    outline=LINE, width=1)
        col = REGION_COLORS.get(region, GREY)
        d.rectangle([x0, y0, x0 + cell_w, y0 + 3], fill=col)
        d.text((x0 + 8, y0 + 6), region, font=F_CELL_TAG, fill=col)
        lines = wrap(d, head, F_CELL_HEAD, cell_w - 16)
        yy = y0 + 19
        for ln in lines[:2]:
            d.text((x0 + 8, yy), ln, font=F_CELL_HEAD, fill=INK)
            yy += 14
        d.text((x0 + 8, y0 + cell_h - 14),
               trunc(d, sub, F_CELL_SUB, cell_w - 16),
               font=F_CELL_SUB, fill=GREY)
    # 40th cell: sources
    r, c = divmod(len(STORIES), cols)
    x0 = gx0 + c * (cell_w + 4)
    y0 = gy0 + r * (cell_h + 4)
    d.rectangle([x0, y0, x0 + cell_w, y0 + cell_h], fill=NAVY)
    d.text((x0 + 8, y0 + 6), "SOURCES", font=F_CELL_TAG, fill=GOLD)
    d.text((x0 + 8, y0 + 19), "Reuters · AP · BBC · ONS", font=F_CELL_SUB,
           fill=WHITE)
    d.text((x0 + 8, y0 + 33), "FCC · USTR · Xinhua · Yonhap",
           font=F_CELL_SUB, fill=WHITE)
    d.text((x0 + 8, y0 + cell_h - 14), "All stories checked 26 Nov 2026",
           font=F_CELL_SUB, fill=(200, 210, 225, 255))

    d.text((W // 2, 1012), "news-image-20261126 · @yiw8551",
           font=F_FOOT, fill=GREY, anchor="ma")
    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
