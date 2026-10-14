"""Pistas de fondo originales (sin derechos de terceros) para anuncios en video.

Cada preset imita la energía típica de un formato de anuncio (UGC, explicativo, emocional...).
Uso: ~/.venvs/voz/bin/python gen_music.py <preset> <segundos> <salida.wav>
"""
import sys

import numpy as np
import soundfile as sf

SR = 44100
# bpm, acordes (MIDI), arpegio (subdivisión por tiempo o 0), bombo ("4" = cada tiempo, "13" = 1 y 3, ""), shaker, pad, bajo pulsado
PRESETS = {
    "energetic": dict(bpm=117, chords=[[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]], arp=4, kick="4", hats=True, pad=0.04, bass8=True),
    "energetic108": dict(bpm=108, chords=[[50, 53, 57], [46, 50, 53], [53, 57, 60], [48, 52, 55]], arp=4, kick="4", hats=True, pad=0.04, bass8=True),
    "ugc": dict(bpm=110, chords=[[48, 52, 55], [55, 59, 62], [57, 60, 64], [53, 57, 60]], arp=1, kick="", hats=False, pad=0.03, bass8=False),
    "ambient": dict(bpm=68, chords=[[48, 52, 55, 59], [53, 57, 60, 64]], arp=0, kick="", hats=False, pad=0.07, bass8=False),
    "warm": dict(bpm=100, chords=[[53, 57, 60], [48, 52, 55], [55, 59, 62], [57, 60, 64]], arp=2, kick="13", hats=True, pad=0.05, bass8=False),
    "driving": dict(bpm=103, chords=[[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]], arp=2, kick="13", hats=True, pad=0.035, bass8=True),
    "tense": dict(bpm=85, chords=[[57, 60, 64], [50, 53, 57], [52, 55, 59], [57, 60, 64]], arp=2, kick="1", hats=False, pad=0.05, bass8=True),
    "cinematic": dict(bpm=80, chords=[[57, 60, 64], [53, 57, 60], [48, 52, 55], [52, 56, 59]], arp=0, kick="1", hats=False, pad=0.08, bass8=False),
}


def render(preset, dur):
    p = PRESETS[preset]
    beat = 60 / p["bpm"]
    bar = 4 * beat
    n = int(SR * (dur + 2))
    mix = np.zeros(n)
    rng = np.random.default_rng(7)  # fijo: la pista sale igual siempre

    def hz(m):
        return 440.0 * 2 ** ((m - 69) / 12)

    def add(sig, start):
        i = int(start * SR)
        j = min(n, i + len(sig))
        if i < n:
            mix[i:j] += sig[: j - i]

    def smooth(x, k):
        return np.convolve(x, np.ones(k) / k, mode="same")

    for b in range(int(dur / bar) + 2):
        chord = p["chords"][b % len(p["chords"])]
        t0 = b * bar
        tt = np.arange(int(bar * SR)) / SR
        env = np.minimum(1, tt / 0.5) * np.minimum(1, (bar - tt) / 0.6)
        pad = sum(np.sin(2 * np.pi * hz(m) * tt) + 0.3 * np.sin(2 * np.pi * hz(m) * 2.003 * tt) for m in chord)
        add(smooth(pad * env * p["pad"], 9), t0)
        if p["bass8"]:
            for k in range(8):
                bt = np.arange(int(beat / 2 * SR)) / SR
                add(np.sin(2 * np.pi * hz(chord[0] - 12) * bt) * np.exp(-bt * 6) * 0.09, t0 + k * beat / 2)
        else:
            add(np.sin(2 * np.pi * hz(chord[0] - 12) * tt) * np.minimum(1, tt / 0.03) * np.exp(-tt * 0.5) * 0.08, t0)
        if p["arp"]:
            steps = 4 * p["arp"]
            for k in range(steps):
                m = chord[k % len(chord)] + 12 + (12 if (k // len(chord)) % 2 else 0)
                pt = np.arange(int(0.5 * SR)) / SR
                pl = (np.sin(2 * np.pi * hz(m) * pt) + 0.3 * np.sin(2 * np.pi * hz(m) * 3 * pt)) * np.exp(-pt * 8)
                add(pl * 0.04, t0 + k * bar / steps)
        for k in range(4):
            if str(k + 1) in p["kick"] or p["kick"] == "4":
                kt = np.arange(int(0.4 * SR)) / SR
                freq = 110 * np.exp(-kt * 18) + 42
                add(np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-kt * 8) * 0.17, t0 + k * beat)
            if p["hats"]:
                for h in range(2):
                    ht = np.arange(int(0.07 * SR)) / SR
                    noise = rng.standard_normal(len(ht))
                    add((noise - smooth(noise, 6)) * np.exp(-ht * 50) * (0.02 if h else 0.012), t0 + k * beat + h * beat / 2)

    mix = mix[: int(SR * dur)]
    fade_in, fade_out = int(SR * 0.5), int(SR * 1.2)
    mix[:fade_in] *= np.linspace(0, 1, fade_in)
    mix[-fade_out:] *= np.linspace(1, 0, fade_out)
    return mix / (np.abs(mix).max() + 1e-9) * 0.8


if __name__ == "__main__":
    preset, dur, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    audio = render(preset, dur)
    sf.write(out, np.stack([audio, audio], axis=1), SR)
    print(out, preset, f"{dur:.1f}s")
