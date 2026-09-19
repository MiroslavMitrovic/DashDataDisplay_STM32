#!/usr/bin/env sh
set -eu

rules_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/udev"
sudo install -m 0644 "$rules_dir/99-owon_psu_6205e.rules" /etc/udev/rules.d/99-owon_psu_6205e.rules
sudo install -m 0644 "$rules_dir/99-usb-serial-names.rules" /etc/udev/rules.d/99-usb-serial-names.rules
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=tty
