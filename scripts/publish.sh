./scripts/clean.sh

# Build project
py setup.py bdist_wheel
twine upload dist/*
