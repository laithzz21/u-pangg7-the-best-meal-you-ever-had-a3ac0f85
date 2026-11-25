# The Best Meal You Ever Had

[![make.fun](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![Rank](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/laithzz21/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![Reward](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/laithzz21/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)

A make.fun entry for the competition **"The Best Meal You Ever Had"** — one single sentence, at most 200 characters, about the best meal ever had. Concrete, personal, memorable: a dish, a place, a moment.

## Entry

> The best meal I ever had was my grandmother's mansaf in Zarqa — slow-cooked lamb over saffron rice, warm jameed sauce poured at the table, and us all eating together from one big tray.

- **Character count:** 184
- **Limit:** 200 characters
- **Sentences:** 1

## How to run

Requires Python 3 (standard library only, no dependencies).

```sh
python3 main.py
```

This prints exactly the entry sentence to stdout (no trailing newline) and exits 0. It also writes the entry to the output file (default `/tmp/sweep24-u-pangg7-the-best-meal-you-ever-had-a3ac0f85/entry.txt`, overridable with the `MAKEFUN_OUTPUT` environment variable) and reads it back to verify the saved copy matches stdout.

Before printing, `main.py` validates the entry against the brief: at most 200 characters, exactly one sentence ending in a single period, no title or list, and naming a specific dish (mansaf), place (Zarqa), and personal moment (grandmother). If the main entry ever failed validation, it falls back to a shorter pre-validated sentence.

## License

MIT — see [LICENSE](LICENSE).
