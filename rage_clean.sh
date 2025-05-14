  GNU nano 8.4                                                  rage_unicode.sh
#!/data/data/com.termux/files/usr/bin/bash

# Description: Realtime zero-width Unicode remover and detector.

clean_line() {
  perl -C -pe 's/[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{206F}]//g'
}

show_hidden() {
  perl -C -nE '
    use utf8;
    my @chars = split("", $_);
    my $i = 0;
    for my $char (@chars) {
      my $code = ord($char);
      if (
        ($code >= 0x200B && $code <= 0x200F) ||
        ($code >= 0x202A && $code <= 0x202E) ||
        ($code >= 0x2060 && $code <= 0x206F)
      ) {
        printf "  [pos %2d] U+%04X (zero-width)\n", $i, $code;
      }
      $i++;
    }
  '
}

clear

echo "[*] Type your text. Cleaned version will appear instantly (Ctrl+C to exit)."
echo "[*] Add '--show' to display hidden Unicode codepoints."
echo

while true; do
  printf "You: "
  IFS= read -r input

  if [[ "$input" == *"--show" ]]; then
    clean_input="${input/--show/}"
    echo "Original: $clean_input"
    echo "Clean   : $(echo "$clean_input" | clean_line)"
    echo "Hidden  :"
    echo "$clean_input" | show_hidden
  else
    echo "Clean   : $(echo "$input" | clean_line)"
  fi
done
