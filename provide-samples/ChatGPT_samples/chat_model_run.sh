#!/usr/bin/bash

OPENAI_KEY=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
cd /home/angelcore/Python-Projects/ChatGPT

source .chatenv/bin/activate

echo "Chat Env activated"

python3 chat_model.py $OPENAI_KEY
deactivate
