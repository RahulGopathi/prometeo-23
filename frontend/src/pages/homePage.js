import { useState, useEffect } from 'react';

import './homePage.css'

import PrometeoLogo from '../assets/homePage/logo.png'
import loading1 from '../assets/loading/big_bang.mp4';
import spinner from '../assets/loading/loading_new.gif';

import solarSystem from "./solarsystem";
import FadeIn from '../components/fadein';

export default function HomePage(props) {
    const [isLoading, setIsLoading] = useState(true);
    
    const handleLoading = () => {
        // console.log("loading over");
        setIsLoading(false);
        document.body.style.backgroundColor = "#fff"
        // console.log(props.bb);
        // console.log("changed body colour");
    }
  
    const fadeScreenToHomePage = () => {
        // console.log("proceeding to home page");
        props.bbFunc(false);
        // const vid = document.getElementById("my_video");
        // vid.remove();
        // document.getElementById("LoadingAnimation").remove();
        
        document.body.style.background = "rgb(16,28,39)"
        document.body.style.background = "radial-gradient(circle, rgba(16,28,39,1) 10%, rgba(0,0,0,1) 90%)"
    
        const homePageEle = document.getElementById("homepage");
        homePageEle.style.opacity = 1;
        const navBarEle = document.getElementById("navbar")
        navBarEle.style.opacity = 1;
    
        solarSystem();
  
    }

    useEffect(  // when the component has rendered then add the event listener to it
    () => {
        // const navBarEle = document.getElementById("navbar")
        // console.log("bigBang: ", props.bb, ", loading: ", isLoading);
        // navBarEle.style.opacity = 0;
        document.body.style.overflow = "hidden";

        if (props.bb) {
            // console.log("ok big bang done");
            const vid = document.getElementById("my_video");
            vid.addEventListener("canplay", handleLoading);
            vid.addEventListener("ended", fadeScreenToHomePage);
        }
        // }
        else {
            // console.log("skipping big bang");
            fadeScreenToHomePage();
        }
      },[]
    )
    return (
		<FadeIn duration={500}>
            <div>            
                {
                    props.bb && isLoading && 
                    (
                        <div className="spinner">
                            <img src={spinner} alt="Loading..." />
                        </div>
                    )
                }
                {
                    props.bb &&
                    (
                    <div id="LoadingAnimation">
                        <video id="my_video" autoPlay={true} muted>
                            <source src={loading1} type="video/mp4" />
                        </video>
                    </div>
                    )
                }
                <div id="homepage">
                    <div id="about-prometeo">
                        <div id="about-prometeo-logo">
                            <img id="about-prometeo-logo-img" src={PrometeoLogo} alt="Prometeo Logo" />
                        </div>
                        <div id="about-prometeo-text">
                        Prometeo 2023 is the third edition of IIT Jodhpur's National Technical + Entrepreneurial Festival. Prometeo derives its name from the Greek word for forethinker, and celebrates disruptive technologies through talks, workshops, and competitions.
                        </div>
                    </div>
                </div>
            </div>
        </FadeIn>
    )
}