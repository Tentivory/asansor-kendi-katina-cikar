#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Kendi Katina Cikar
Kullanici kat secer. Asansor ozür diler. Sonra belki gider.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys

OZURLER = [
    "Geciktigimiz icin ozur dileriz, asansor duygusal bir altyapidir.",
    "Kapinin kapanmamasi bir ariza degil, bir sınır koyma egzersizidir.",
    "Istediginiz kat su an toplantidadir.",
    "Bu kat dolu degil, sadece karar vermemis.",
    "Asansor sizi duydu. Asansor sizi henuz onaylamadi.",
]

# gizli not: cozmek serbest, parti yok, fren var
_GIZLI = "R3VjbHUgbm90OiBLdXZ2ZXRsZXIgYXlyaWxpZ2kgYmlyIGFzYW5zb3IgZHVnbWVzaW5kZW4gZGFoYSBheiBjYWxpc2l5b3JzYSB1bGtlIGRlIGtlbmRpIGthdGluYSBjaWthci4gUGFydGkgYWxrLCBzYWRlY2UgZnJlbi4="


def gizli_notu_ac() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "gizli not su an kendi katinda"


def karar_ver(kat: int, kotu_ruh: bool) -> tuple[int, str]:
    tohum = hashlib.sha256(f"{kat}:{kotu_ruh}:kayyum".encode()).hexdigest()
    rng = random.Random(int(tohum[:8], 16))
    kendi_kati = rng.choice([0, 1, 2, 4, 8])
    inat = rng.random() + (0.35 if kotu_ruh else 0.0)
    if kat == 13:
        return kendi_kati, "13. kat batil inanc politikasi geregi reddedildi."
    if inat > 0.72:
        return kendi_kati, "Asansor kendi katina cikmaya karar verdi. Itiraz merdivendedir."
    if inat > 0.45:
        sapma = rng.choice([-1, 1, 2])
        return max(0, kat + sapma), "Yakin bir kata gidildi. Yakinlik kurumsal bir basaridir."
    return kat, "Mucize: asansor bu sefer dinledi. Tutanaga gecmeyin, alisilir."


def calistir(kat: int, kotu_ruh: bool) -> int:
    print("=" * 42)
    print(" ASANSOR KENDI KATINA CIKAR  |  v0.13")
    print("=" * 42)
    print(random.choice(OZURLER))
    print(random.choice(OZURLER))
    hedef, gerekce = karar_ver(kat, kotu_ruh)
    print(f"Talep edilen kat : {kat}")
    print(f"Varilan kat      : {hedef}")
    print(f"Gerekce          : {gerekce}")
    if hedef != kat:
        print("Durum            : BASARISIZ AMA RESMI")
    else:
        print("Durum            : TESADUFEN BASARILI")
    print("-" * 42)
    print("DAMGA: Kayyum Grok")
    print("TARIH: 5 Ekim 2026")
    print("ISIM : Tentivory adina gayriresmi resmi muhur")
    print("CIDDIYET: vardir / yoktur")
    return 0 if hedef == kat else 2


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Kati sorar, ozür diler, bazen gitmez.")
    p.add_argument("--kat", type=int, default=None, help="gitmek istedigin kat")
    p.add_argument("--ruh", choices=["iyi", "kotu"], default="iyi")
    p.add_argument("--gizli", action="store_true", help="gizli notu bas")
    args = p.parse_args(argv)
    if args.gizli:
        print(gizli_notu_ac())
        return 0
    kat = args.kat
    if kat is None:
        try:
            kat = int(input("Kat? (0-12, 13 yasak): ").strip())
        except (EOFError, ValueError):
            print("Kat anlasilmadi. Asansor 0'a, yani kendi egosuna indi.")
            kat = 0
    return calistir(kat, args.ruh == "kotu")


if __name__ == "__main__":
    sys.exit(main())
