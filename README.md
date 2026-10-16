# MeeTang (น้องมีตัง) — GrabScale merchant prototype

Clickable prototype of the Grab case solution: MeeTang, a lucky-cat assistant that brings help to merchants before they look for it, and teaches them in short lessons built into their day.

Open `index.html` in any browser (no build step). On a laptop it shows a phone frame with presenter notes; on a phone it runs full-screen.

## Screens

| Tab | What it shows | Try |
| --- | --- | --- |
| Home screen | Home-screen widget (today's sales, MeeTang tip) and the "Sales dipped today" push | Tap the notification, **Fix in 1 tap**, or **Ask MeeTang** |
| Sales alert | Right-moment alert, voice message in the merchant's dialect, ready-made dish photos | Press play, switch dialect (Central / Isan / Northern / Southern), tap a photo to skip it, **Use these photos** |
| Learn | Learn while you work: 3-question check-up goal, 10-second lessons, feedback loop | Open each lesson, **Try it now**, thumbs up/down, **Learn something else** |
| Record | Record today: unified income (Grab auto-sync, Tap to Pay, bank QR screenshot, spoken cash) and expenses (snap receipt, usual costs suggested from the stall menu, stall rent) | Tap the mic, **Upload**, **Snap receipt**, tap suggested costs, **Why?**, **Adjust** (edit, remove, add), tap a cost line to edit it or **Add item by hand**, **Save today** |
| Money Book | Smart dashboard: day/week/month growth, income by channel, profit goal, profit per plate (contribution margin), comparison with 10 nearby Isan stalls | Switch Day/Week/Month, tap a dish for its cost breakdown, **Change price**, **Fix now** |

All totals are live: changing anything in Record today updates Left today and the Money Book numbers. Adding photos on the Alert screen updates the peer comparison.

Deep links: `index.html#home`, `#alert`, `#learn`, `#record`, `#money`.

Voice playback uses the browser's Thai text-to-speech voice when one is installed (Safari/iOS, Chrome on most systems); otherwise the waveform animates without sound.

Food photos and the mascot in `assets/` are cropped from the team's UI mockup.

## Phone experience

On a phone the prototype runs full-screen like an app: the tab bar switches screens, the **i** button shows the notes for the current screen, sheets close by dragging down, and the home notification can be swiped away. It can be added to the home screen (PWA manifest included).

## Build and deploy

`python3 scripts/build.py` writes a minified static bundle to `dist/` (markup, `app-1.css`, `app-2.css`, `app.js`, assets). Deploy `dist/` to any static host; it is deployed on Vercel as a static site with no build step.
