import React from 'react';

function About() {
  return (
    <div className="about">
      <h2>About</h2>
      <p>This React template includes:</p>
      <ul>
        <li>⚡ Vite for fast development</li>
        <li>🧭 React Router for navigation</li>
        <li>🧪 Vitest for testing</li>
        <li>🎨 CSS modules support</li>
        <li>📏 ESLint for code quality</li>
        <li>💅 Prettier for formatting</li>
      </ul>
      
      <h3>Getting Started</h3>
      <ol>
        <li>Run <code>npm install</code></li>
        <li>Run <code>npm run dev</code></li>
        <li>Start building your app!</li>
      </ol>
    </div>
  );
}

export default About;