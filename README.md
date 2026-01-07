LaserFlow Automation - GitHub Pages
A modern web interface for laser cutting automation, now deployed as a static site on GitHub Pages.

Overview About
Web application interface developed for a metal fab laser flow automation. This is a Streamlit-based frontend application built with Vite and styled with Tailwind CSS. It displays a dashboard for monitoring laser cutting machines, jobs, and production status.

mock up web app design 

fields missing

backend folder not added because it crashes the code

Live Demo
Visit the site at: [https://special-chainsaw-v6q79r956p5rf6p4x-8501.app.github.dev/]

Features
Dashboard: Real-time overview of production status, active lasers, and job queue
Machines: Monitor laser machine status and current programs
Jobs: View and manage the job queue with filtering options
Responsive Design: Works on desktop and mobile devices
Local Development
Prerequisites
Node.js 20 or higher
npm
Installation
Clone the repository:
git clone https://github.com/john-fizer/github.io-laserautomation.git
cd github.io-laserautomation
Navigate to the frontend directory:
cd frontend
Install dependencies:
npm install
Start the development server:
npm run dev
Open your browser to http://localhost:3000
Building for Production
Build the static site:

npm run build
The built files will be in the dist/ directory.

Preview the production build:

npm run preview

Deployment

Technology Stack
Streamlit - UI framework
Vite - Build tool and dev server
Tailwind CSS - Utility-first CSS framework
React Router - Client-side routing
Project Structure
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Page components (Dashboard, Machines, Jobs)
│   ├── lib/            # Utilities and mock API
│   ├── App.jsx         # Main app component
│   └── main.jsx        # Entry point
├── public/             # Static assets
└── dist/               # Build output (generated)

Note on Backend
This is currently a static site using mock data. The original backend/Docker configuration has been disabled. If you need to integrate with a real backend API, modify frontend/src/lib/api.js to use axios or fetch instead of the mock data.

License
MIT

