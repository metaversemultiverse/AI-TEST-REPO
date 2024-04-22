{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "my-project";

  buildInputs = with pkgs; [
    python3
    python3Packages.:pip
    python3Packages.virtualenv
  ];

  shellHook = "
    # Create a Python virtual environment
    virtualenv venv
    source venv/bin/activate

    # Install project dependencies
    pip install -r requirements.txt
  ";
}