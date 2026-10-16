# MeeTang (น้องมีตัง) — GrabScale merchant prototype

Clickable prototype of the Grab case solution: MeeTang, a lucky-cat assistant that brings help to merchants before they look for it, and teaches them in short lessons built into their day.

Open `index.html` in any browser (no build step). On a laptop it shows a phone frame with presenter notes; on a phone it runs full-screen.

## Screens

| Tab | What it shows | Try |
| --- | --- | --- |
| Home screen | Home-screen widget (today's sales, MeeTang tip) and the "Sales dipped today" push | Tap the notification, **Fix in 1 tap**, or **Ask MeeTang** |
| Sales alert | Right-moment alert, voice message in the merchant's dialect, ready-made dish photos | Press play, switch dialect (Central / Isan / Northern / Southern), tap a photo to skip it, **Use these photos** |
| Learn | Learn while you work: 3-question check-up goal, 10-second lessons, feedback loop | Open each lesson, **Try it now**, thumbs up/down, **Learn something else** |

Deep links: `index.html#home`, `#alert`, `#learn`.

Voice playback uses the browser's Thai text-to-speech voice when one is installed (Safari/iOS, Chrome on most systems); otherwise the waveform animates without sound.

Food photos and the mascot in `assets/` are cropped from the team's UI mockup.
