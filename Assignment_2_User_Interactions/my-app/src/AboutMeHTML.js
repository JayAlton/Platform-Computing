import React, { useState, useEffect } from 'react';

const AboutMeHTML = () => {
    // Initialize state to track the number of clicks
  const [numClicks, setNumClicks] = useState(0);

  // Function to handle button click
  const handleButtonClick = () => {
    setNumClicks(prevNumClicks => prevNumClicks + 1);
  };

  // Expose numClicks to global scope on component mount
  useEffect(() => {
    window.numClicks = numClicks;
  }, [numClicks]);
  return (
    
        <body>
            <header class='masthead'>
                
                
            </header>
            <button id="scrollToBottomButton" onClick={handleButtonClick}>Scroll to Bottom</button>
            <section class="introduction-section">
                
                <p class='masthead-intro'>About Me</p>
                <h1 class='masthead-heading'>Jayden Alton</h1>
                <h1>Introduction</h1>
                <p>I am a college student attending CSUSB for Computer Systems with a Game Development Concentration. </p>
                <p>I love game development, technology, and building useful and well-maintained software.</p>
            </section>
            <section class="location-section">
                <h1>Where I'm From</h1>
                <p>I'm originally from Oceanside, California. </p>
            </section>
            <section class="questions-section">
                <h1>More About Me</h1>
                <h2>What are your favorite hobbies?</h2>
                <p>I like to play guitar, watch hockey and play video games.</p>
                <h2>What's your dream job?</h2>
                <p>My dream job is to work for a game development studio. </p>
                <h2>Where do you live?</h2>
                <p>I live in Oceanside and San Bernardino when I'm at school.</p>
                <h2>Why do you want to be a web developer?</h2>
                <p>I think web development is an essential skill for anyone looking to further their career in software development and engineering.</p>
            </section>
            
            <footer class="content-footer">
                <p>Other Links: </p>
                <ul class="social">
                    <li><a class="css-is-deranged" href="https://github.com/JayAlton">GitHub</a></li>
                    <li><a class="css-is-deranged" href="https://www.ob-games.com">OBGames</a></li>
                </ul>
                
            </footer>
            <script src="example.js"></script>
        </body>
 
  )
}

export default AboutMeHTML;