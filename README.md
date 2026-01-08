# LaserFlow Automation

A modern web interface for laser cutting automation with two deployment options.

## 🚀 Live Demos

This project provides two different web applications for the same laser automation dashboard:

1. **Streamlit App** (Python-based): [https://laserautomation.streamlit.app/](https://laserautomation.streamlit.app/)
   - Fully functional and live
   - Built with Streamlit framework

2. **React Frontend** (JavaScript-based): [https://john-fizer.github.io/github.io-LaserAutomation/](https://john-fizer.github.io/github.io-LaserAutomation/)
   - Static site deployed on GitHub Pages
   - Built with React, Vite, and Tailwind CSS
   - See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for deployment instructions

## Overview

Web application interface developed for a metal fab laser flow automation. It displays a dashboard for monitoring laser cutting machines, jobs, and production status.

## ✨ Features

- **Dashboard**: Real-time overview of production status, active lasers, and job queue
- **Machines**: Monitor laser machine status and current programs
- **Jobs**: View and manage the job queue with filtering options
- **Responsive Design**: Works on desktop and mobile devices

## 🛠 Technology Stack

### Streamlit Application
- **Streamlit** - Python UI framework
- **Pandas** - Data manipulation

### React Frontend
- **React** - UI library
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing

## 📦 Local Development

### Running the Streamlit App

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

### Running the React Frontend

**Prerequisites:**
- Node.js 20 or higher
- npm

**Installation:**

```bash
# Clone the repository
git clone https://github.com/john-fizer/github.io-laserautomation.git
cd github.io-laserautomation

# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

Open your browser to http://localhost:3000

### Building for Production

```bash
cd frontend

# Build the static site
npm run build

# Preview the production build
npm run preview
```

The built files will be in the `frontend/dist/` directory.

## 🚀 Deployment

### Streamlit Cloud
The Streamlit app is deployed at https://laserautomation.streamlit.app/

### GitHub Pages
The React frontend is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for detailed setup instructions.

## 📁 Project Structure

```
.
├── streamlit_app.py           # Streamlit application
├── requirements.txt           # Python dependencies
├── frontend/                  # React application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components (Dashboard, Machines, Jobs)
│   │   ├── lib/              # Utilities and mock API
│   │   ├── App.jsx           # Main app component
│   │   └── main.jsx          # Entry point
│   ├── public/               # Static assets
│   └── dist/                 # Build output (for GitHub Pages)
└── .github/
    └── workflows/
        └── deploy.yml        # GitHub Actions deployment workflow
```

## 📝 Note on Backend

Both applications currently use mock data for demonstration purposes. The original backend/Docker configuration has been disabled. 

To integrate with a real backend API:
- **Streamlit**: Modify the data functions in `streamlit_app.py`
- **React**: Modify `frontend/src/lib/api.js` to use axios or fetch instead of mock data

## 📄 License

MIT
