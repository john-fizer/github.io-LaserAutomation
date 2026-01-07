FROM node:24-alpine

WORKDIR /app

# Copy package.json and lock file first for caching
COPY package*.json ./

# Install dependencies (since we didn't do it locally)
RUN npm install

# Copy source code
COPY . .

# Expose Vite dev port
EXPOSE 3000

# Start dev server with specific host to bind to Docker network
CMD ["npm", "run", "dev", "--", "--host"]
