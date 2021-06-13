./scripts/clean.ps1

# Build project
py setup.py bdist_wheel
twine upload dist/*
