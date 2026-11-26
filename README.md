# 26 November 2026 — The World in One Image

Entry for the make.fun bounty **news-image-20261126**: one image summing up
the world's news of Thursday 26 November 2026.

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/yiw8551/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/yiw8551/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

## The image

40 stories across 11 regions, each checked against reporting from
26 November 2026 (Reuters, AP, BBC, ONS, FCC, USTR, Xinhua, Yonhap).
Lead story: the US proposes new tariffs on 14 trading partners, with a
chart of the proposed top rates. Also featured: the Cairo tanker fire
(31 dead), Ebola cases passing 12,000 in DR Congo, the Houthi strike on
Saudi Arabia's Ras Tanura refinery, mines hitting tankers in the Strait of
Hormuz, the FCC clearing SpaceX's million-satellite plan, the Kospi's 6.2%
plunge, the first Pakistani astronaut reaching Tiangong, and the Solomon
Islands–Australia security treaty. New in this version: a simplified world
map marking all 10 regions and a UTC timeline strip of the day's key
events, in a cleaner 5-column grid with shorter headlines.

## How it runs

`main.py` (Python 3.12+, standard library only) copies the pre-rendered
`entry.png` (1024x1024, under 1 MiB) to `<output-dir>/entry.png`, where the
output directory is `argv[1]`, `$MAKEFUN_OUTPUT_DIR`, or `/output`, in that
order. It verifies the copy byte-for-byte and exits non-zero if anything
is wrong. `render.py` is the build-time script that drew `entry.png`
(Pillow, run once on the author's machine); it is not needed at grading
time and is not imported by `main.py`.

```sh
python3 main.py /tmp/out   # writes /tmp/out/entry.png
```
