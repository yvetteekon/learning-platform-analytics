#!/bin/bash
# setup.sh - Minimal setup for Learning Platform Analytics

echo "Ì∫Ä Setting up Learning Platform Analytics..."

# Install dependencies
echo "Ì≥¶ Installing dependencies..."
uv sync --extra dev

# Initialize DVC
echo "Ì¥ß Initializing DVC..."
uv run dvc init --no-scm 2>/dev/null || true

# Track data with DVC
if [ -d "data" ] && [ ! -f "data.dvc" ]; then
    echo "Ì≥ä Adding data/ to DVC..."
    uv run dvc add data
fi

# Register Jupyter kernel
echo "Ì≥ì Registering Jupyter kernel..."
uv run python -m ipykernel install --user --name=learning-platform --display-name="Python (Learning Platform)"

echo ""
echo "‚úÖ Setup completed!"
echo ""
echo "Next steps:"
echo "   uv run dvc pull          # Pull raw data"
echo "   uv run jupyter lab       # Launch Jupyter"
echo ""
echo "‚ö†Ô∏è  Important: Select the kernel \"Python (Learning Platform)\" in Jupyter Lab."
