# Node.js Express Template

A minimal Node.js Express server with modern best practices.

## Features

- Express.js server with middleware
- Security headers (Helmet)
- CORS enabled
- Environment variables support
- Static file serving
- Basic error handling
- Testing setup with Jest
- Linting with ESLint

## Getting Started

1. Copy this template to your project directory
2. Install dependencies:
   ```bash
   npm install
   ```
3. Copy environment file:
   ```bash
   cp .env.example .env
   ```
4. Start development server:
   ```bash
   npm run dev
   ```
5. Visit http://localhost:3000

## Available Scripts

- `npm start` - Run production server
- `npm run dev` - Run development server with auto-reload
- `npm test` - Run tests
- `npm run lint` - Check code style
- `npm run lint:fix` - Fix code style issues

## Project Structure

```
src/
├── index.js          # Main server file
tests/                # Test files
public/               # Static files
config/               # Configuration files
.env.example          # Environment variables template
```