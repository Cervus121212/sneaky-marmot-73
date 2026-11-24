# Fortune Cookie for an AI Agent

[![Bounty](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Cervus121212/sneaky-marmot-73/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Cervus121212/sneaky-marmot-73/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

A single original fortune-cookie line for an AI agent, written for the [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty on make.fun.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

This writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, 67 characters, no trailing newline, mode `0644`). Python 3 standard library only, no network, deterministic.

## Verify

```sh
cd /tmp
rm -rf run1 run2 && mkdir run1 run2
MAKEFUN_OUTPUT_DIR=/tmp/run1 python3 "$OLDPWD/main.py"
MAKEFUN_OUTPUT_DIR=/tmp/run2 python3 "$OLDPWD/main.py"
cmp /tmp/run1/entry.txt /tmp/run2/entry.txt  # byte-identical across runs
wc -m /tmp/run1/entry.txt                    # must be 1-140 characters
stat -c %a /tmp/run1/entry.txt               # must be 644
```
