#!/data/data/com.termux/files/usr/bin/bash

# File: rage_clean.sh
# Description: Instantly cleans input from zero-width and invisible Unicode characters, line by line.

clean_line() {
  perl -C -pe 's/[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{206F}]//g'
}

echo "[*] Type your text. Cleaned version will appear instantly (press Ctrl+C to exit)."
echo

while true; do
  printf "You: "
  IFS= read -r input
  echo "Clean : $(echo "$input" | clean_line)"
done
