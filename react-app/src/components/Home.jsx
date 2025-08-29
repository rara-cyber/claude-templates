import React, { useState } from 'react';

function Home() {
  const [count, setCount] = useState(0);

  return (
    <div className="home">
      <h2>Welcome to React!</h2>
      <p>This is your React application template.</p>
      
      <div className="counter">
        <h3>Counter Example</h3>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>
          Increment
        </button>
        <button onClick={() => setCount(count - 1)}>
          Decrement
        </button>
        <button onClick={() => setCount(0)}>
          Reset
        </button>
      </div>
    </div>
  );
}

export default Home;