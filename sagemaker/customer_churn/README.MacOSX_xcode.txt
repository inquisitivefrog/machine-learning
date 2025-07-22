
tim@Tims-MBP ~ % xcode-select --install
xcode-select: error: command line tools are already installed, use "Software Update" in System Settings to install updates
tim@Tims-MBP ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /usr/sbin/chown -R tim:admin /usr/local/Homebrew
==> Downloading and installing Homebrew...
remote: Enumerating objects: 912, done.
remote: Counting objects: 100% (386/386), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 912 (delta 371), reused 371 (delta 362), pack-reused 526 (from 3)
==> Updating Homebrew...
==> Downloading https://ghcr.io/v2/homebrew/portable-ruby/portable-ruby/blobs/sha256:45cea656cc5b5f5b53a9d4fc9e6c88d3a29b3aac862d1a55f1c70df534df5636
######################################################################### 100.0%
==> Pouring portable-ruby-3.4.4.el_capitan.bottle.tar.gz
Updated 4 taps (heroku/brew, hashicorp/tap, homebrew/core and homebrew/cask).
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these commands in your terminal to add Homebrew to your PATH:
    echo >> /Users/tim/.zprofile
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> /Users/tim/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh

tim@Tims-MBP ~ % brew install libomp
libomp  is already installed but outdated (so it will be upgraded).
==> Downloading https://ghcr.io/v2/homebrew/core/libomp/manifests/20.1.5
######################################################################### 100.0%
==> Fetching libomp
==> Downloading https://ghcr.io/v2/homebrew/core/libomp/blobs/sha256:9972ac42bb9
######################################################################### 100.0%
==> Pouring libomp--20.1.5.ventura.bottle.tar.gz
==> Caveats
libomp is keg-only, which means it was not symlinked into /usr/local,
because it can override GCC headers and result in broken builds.

For compilers to find libomp you may need to set:
  export LDFLAGS="-L/usr/local/opt/libomp/lib"
  export CPPFLAGS="-I/usr/local/opt/libomp/include"
==> Summary
🍺  /usr/local/Cellar/libomp/20.1.5: 9 files, 1.7MB
==> Running `brew cleanup libomp`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
Removing: /usr/local/Cellar/libomp/20.1.3... (9 files, 1.7MB)
Removing: /Users/tim/Library/Caches/Homebrew/libomp_bottle_manifest--20.1.3... (12.1KB)
Removing: /Users/tim/Library/Caches/Homebrew/libomp--20.1.3... (574.3KB)
tim@Tims-MBP ~ % 
`
