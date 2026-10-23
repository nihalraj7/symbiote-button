# Symbiote Button

A call-to-action button made of thick black liquid. It reaches for your cursor with viscous strands, stretches and snaps like ferrofluid, and when you click it, it turns into a daemon that eats the website.

**Live:** https://symbiote-button.vercel.app

| Page | What it does |
|---|---|
| [`/`](https://symbiote-button.vercel.app) | The daemon: the button swells into a spiked, grinning blob that devours the page piece by piece, then throws it back up on the next click |
| [`/eats`](https://symbiote-button.vercel.app/eats) | The button bursts into droplets that coat the page, then swallows it |
| [`/button`](https://symbiote-button.vercel.app/button) | The original standalone button |

Vanilla JS and a single `<canvas>`, no libraries. Every sound is synthesised with the Web Audio API.

## Controls

- **Click** the button to set it off; click again to get the page back
- **M** mute · **R** clean frame for screen recording · **D** tuning panel

## Run locally

```bash
python3 serve.py
```

Then open http://localhost:8080 (`/eats` and `/daemon` for the other versions).

## Build and deploy

`python3 build.py` writes the static site to `dist/`. Vercel runs it on every push to `main` (see `vercel.json`).

## Credit

Inspired by the liquid button from [@exteedesign](https://www.instagram.com/exteedesign/). Built on top of it by [Nihal](https://github.com/nihalraj7).
