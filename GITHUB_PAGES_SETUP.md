# GitHub Pages Setup Instructions

This repository is configured to deploy the React frontend to GitHub Pages automatically.

## One-time Setup (Repository Owner Must Complete)

To enable GitHub Pages for this repository, follow these steps:

1. **Go to Repository Settings**
   - Navigate to: https://github.com/john-fizer/github.io-LaserAutomation/settings/pages

2. **Configure GitHub Pages Source**
   - Under "Build and deployment"
   - Set **Source** to: `GitHub Actions`
   - (This allows the workflow in `.github/workflows/deploy.yml` to deploy the site)

3. **Trigger the Workflow**
   - Once the settings are saved, merge this PR to the `main` branch
   - The GitHub Actions workflow will automatically build and deploy the site
   - Alternatively, you can manually trigger the workflow from the Actions tab

4. **Access Your Site**
   - After the workflow completes, your site will be available at:
   - **https://john-fizer.github.io/github.io-LaserAutomation/**

## How It Works

- **Automatic Deployment**: Every push to the `main` branch automatically builds and deploys the React frontend
- **Manual Deployment**: You can also trigger deployment manually from the Actions tab
- **Build Process**: 
  1. The workflow installs dependencies
  2. Builds the React app using Vite
  3. Deploys the `frontend/dist` folder to GitHub Pages

## Repository Structure

This repository contains two applications:

1. **Streamlit App** (`streamlit_app.py`)
   - Live at: https://laserautomation.streamlit.app/
   - Deployed via Streamlit Cloud

2. **React Frontend** (`frontend/`)
   - Will be live at: https://john-fizer.github.io/github.io-LaserAutomation/
   - Deployed via GitHub Pages

Both applications serve the same purpose but use different technologies.

## Troubleshooting

If the site doesn't load after deployment:
1. Check the Actions tab for workflow status
2. Ensure GitHub Pages source is set to "GitHub Actions"
3. Wait a few minutes after the workflow completes for DNS propagation
4. Clear your browser cache

For questions or issues, check the GitHub Actions logs in the repository's Actions tab.
