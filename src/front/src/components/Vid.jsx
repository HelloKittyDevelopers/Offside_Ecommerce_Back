import React from 'react';
import videoBg from '../assets/videoBg.mp4';

const Vid = () => {
    return (
      <div className="Vid">
        <video 
          src={videoBg} 
          autoPlay 
          loop 
          muted 
        />
        <div className="content">
          <h1>Offside</h1>
          <p>A Timeless Passion</p>
        </div>
      </div>
    );
  }
  
  export default Vid;