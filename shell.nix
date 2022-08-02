{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/22.05") {}
}:

pkgs.mkShell {
  nativeBuildInputs = [
    pkgs.python39Full
    pkgs.python39Packages.pygame
  ];

  shellHook = ''
    LOCALE_ARCHIVE="$(nix-build --no-out-link '<nixpkgs>' -A glibcLocales)/lib/locale/locale-archive"

    export LANG=en_GB.UTF-8
  '';
}
