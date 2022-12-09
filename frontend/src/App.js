import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";

import { ToastContainer } from 'react-toastify';
import "react-toastify/dist/ReactToastify.css";
import "./components/toast.css"

import './App.css';

import Navbar from './components/navbar'
import HomePage from "./pages/homePage";
import Page_404 from "./pages/404";
import Speaker from "./pages/Speaker";
import Gallery from "./pages/Gallery";
import Theme from "./pages/Theme";
import Sponsors from "./pages/Sponsors";
import Events from "./pages/Event.js";
import Register from "./pages/Register.js";
import PreRegistration from "./pages/preRegistration";
import Login from "./pages/Login.js";
import EventDetails from "./pages/Event_details";


function App() {

  const [bigBang, setBigBang] = useState(true);

  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage bb={bigBang} bbFunc={setBigBang}/>} />
          
          <Route path="/past-speakers" element={<Speaker />} />
          <Route path="/gallery" element={<Gallery />} />
          <Route path="/past-sponsors" element={<Sponsors />} />
          <Route path="/past-events" element={<Events />} />
          <Route path="/theme" element={<Theme />} />
          <Route path="/register" element={<Register />} />
          <Route path="/pre-register" element={<PreRegistration />} />
          <Route path="/login" element={<Login />} />
          <Route path="/Event_details" element={<EventDetails />} />

          <Route path="/*" element={<Page_404 />} />
        </Routes>
        <ToastContainer 
          theme="dark"
        />
      </div>
    </Router>
  );
}

export default App;
