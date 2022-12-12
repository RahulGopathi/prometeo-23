import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "./homePage.css";

import PrometeoLogo from "../assets/homePage/logo.png";
import loading1 from "../assets/loading/big_bang.mp4";
import spinner from "../assets/loading/logo.gif";
import scrollGif from "../assets/homePage/scrolldown.gif";

import { loadTextures, createScene } from "./solarsystem";
import NewSolarSystem from "./newSolarSystem";
import FadeIn from "../components/fadein";

import LandingSection from "../components/landingSection";
import Introduction from "../components/intro";
import Theme from "../components/Theme";
import InitiativeHome from "../components/initiativeHome";
import EventHome from "../components/eventHome";
import StatsHome from "../components/statsHome";


export default function HomePage() {
  const [isLoading, setIsLoading] = useState(true);
  const [showContent, setShowContent] = useState(false);

  // useEffect(() => {
  //   loadTextures(isLoading, setIsLoading);
  // }, []);

  useEffect(() => {
    console.log("isLoading: ", isLoading);
    if (!isLoading) {
      const navBarEle = document.getElementById("navbar");
      navBarEle.style.opacity = 1;
      const homePageEle = document.getElementById("homepage-solarSystem");
      homePageEle.style.opacity = 1;
      
      // createScene();
      setShowContent(true);
    }
  }, [isLoading]);

  return (
    <div id="homepage">
      <NewSolarSystem setIsLoading={setIsLoading} onLoad />
      {
        !showContent ?
        // isLoading &&
        (
          <div className="spinner">
            <img src={spinner} id = "loader-gif" alt="Loading..." />
          </div>
        ) :
      // }
      // {
      //   showContent &&
        (
          <FadeIn duration={500}>
              {/* <div id="scroll-down">
                <img src={scrollGif} alt="Scroll Down" id="scroll-down-gif" />
              </div> */}
              <div id="homepage-content">
                <LandingSection />
                {/* <Introduction />
                <Theme />
                <InitiativeHome />
                <div id="black-filler"></div>
                <EventHome />
                <div id="purple-filler"></div>
                <StatsHome /> */}
              </div>
          </FadeIn>
        )
      }
    </div>
  );


  // return isLoading ? 
  //     (
  //       <div className="spinner">
  //         <img src={spinner} id = "loader-gif" alt="Loading..." />
  //       </div>
  //     ) : (
  //       // <FadeIn duration={500}>
  //         <div>
  //           <div id="homepage">
  //             {/* <div id="scroll-down">
  //               <img src={scrollGif} alt="Scroll Down" id="scroll-down-gif" />
  //             </div> */}
  //             <div id="homepage-content">
  //               <LandingSection />
  //               {/* <Introduction />
  //               <Theme />
  //               <InitiativeHome />
  //               <div id="black-filler"></div>
  //               <EventHome />
  //               <div id="purple-filler"></div>
  //               <GalleryHome /> */}
  //             </div>
  //           </div>
  //         </div>
  //       // </FadeIn>  
  //     );
}
