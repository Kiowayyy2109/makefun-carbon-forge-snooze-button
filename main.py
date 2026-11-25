#!/usr/bin/env python3
"""Snooze Button Roast — roasting the snooze button."""
import os

LINE = "The snooze button doesn't wake you up. It just reschedules your regret in nine-minute increments."
assert len(LINE) == 97, "entry must be exactly 97 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
