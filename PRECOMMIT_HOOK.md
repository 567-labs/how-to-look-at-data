# Pre-commit Hook for Slidev PDF Generation

This repository includes a pre-commit hook that automatically builds Slidev slides to PDF when any files in the `slidev/` directory are modified.

## How it Works

The pre-commit hook (`.git/hooks/pre-commit`) performs the following steps:

1. **Detects Changes**: Checks if any files in the `slidev/` directory are staged for commit
2. **Installs Dependencies**: Ensures `node_modules` and `playwright-chromium` are installed
3. **Builds PDF**: Runs `npm run export` to generate `slides-export.pdf`
4. **Adds to Commit**: Automatically stages the generated PDF file to be included in the commit

## Setup

The hook is already configured and executable. No additional setup is required.

## What Gets Generated

When you modify any file in `slidev/` and commit, the hook will:
- Generate `slidev/slides-export.pdf` 
- Add it to your commit automatically
- Display progress messages during the build process

## Manual PDF Generation

You can also generate the PDF manually:

```bash
cd slidev
npm run export
```

## Dependencies

The hook automatically installs required dependencies:
- Node.js packages via `npm install`
- `playwright-chromium` for PDF export functionality

## Troubleshooting

If the hook fails:
1. Check that you're in the root directory when committing
2. Ensure the `slidev/` directory contains valid Slidev slides
3. Check that Node.js and npm are properly installed
4. The hook will display error messages to help debug issues 