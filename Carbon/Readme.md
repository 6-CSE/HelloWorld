Setup and run Google's new c++ alternative, using these 5 simple steps.

### Step 1:
Install homebrew using this [link.](http://how-to-install-homebrew-on-mac-linux-windows/)

### Step 2:
Install Bazel
`brew install bazelisk`

### Step 3:
Install LLVM
`brew install llvm` <br />
Export it using `export PATH="$(brew --prefix llvm)/bin:${PATH}"`

### Step 4:
Clone Carbon
`git clone https://github.com/carbon-language/carbon-lang`

### Step 5:
Cd into carbon folder `cd carbon-lang`<br />
Run hello world `bazel run //explorer -- ./explorer/testdata/print/format_only.carbon`
