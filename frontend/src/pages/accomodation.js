import { useEffect, useState, useContext } from "react";
import { toast } from "react-toastify";
import "./accomodation.css";

import useAxios from "../context/context_useAxios";
import { backendURL } from "../backendURL";
import AuthContext from "../context/AuthContext";

import logo from "../assets/homePage/logo.png";

import FadeIn from "../components/fadein";
import { Navigate } from "react-router-dom";

export default function Accommodation() {
    useEffect(() => {
        const navBarEle = document.getElementById("navbar");
        navBarEle.style.opacity = 1;
        // document.body.style.overflow = "hidden";
    }, []);

    return (
        <FadeIn duration={1000}>
            <div id="acc-container">
                <div id="acc-title">
                    <div id="acc-title-text">
                        Accommodation In <span>Prometeo</span>
                    </div>
                </div>
                <div className="acc-content">
                    <div className="acc-content-title">
                        About Us
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-left text-justify">
                            Indian Institute of Technology Jodhpur was
                            established in 2008, to foster technology,
                            education, and research in India. The Institute is
                            committed to pursuing technological advancements in
                            the process of the economic develop ment of India.
                            It functions from its sprawling residential
                            Permanent Campus of 852 acres, with the campus plan
                            being awarded a 5-star rating by GRIHA Coun cili The
                            institute's infrastructure is vividly unique while
                            optimizing all resources to become a
                            near-zero-emission campus. The Institute is
                            committed to a mul tidisciplinary approach to
                            technological development and it has established
                            MoUs with six international universities, two
                            international agencies, and three national
                            institutes and universities for academic cooperation
                            and research, The big breakthroughs in the research
                            field include A1 intelligent gloves equipped with
                            speech to facilitate specially-abled people.
                        </span>
                        <span className="acc-content-desc-left">
                            Hope to see you at Prometeo 2022-23.
                        </span>
                        <span className="acc-content-desc-left">
                            Please visit the Freqently Asked Questions (FAQ)
                            section to get most of your queries resolved.
                        </span>
                    </div>
                </div>
                <div className="acc-content">
                    <div className="acc-content-title">
                        Accommodation Guidelines
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-right">
                            <ol>
                                <li>
                                    Every participant shall at all times be in
                                    possession of a current, government-issued
                                    photo ID. The student participants must
                                    always carry a valid photo ID issued by
                                    their college. If a visitor cannot present
                                    their identification card, they will not be
                                    permitted to enter the Prometeo '23 campus.
                                </li>
                                <li>
                                    Alcohol, drugs, illegal substances, sharp
                                    objects, and any kind of explosives are
                                    absolutely prohibited on campus. Anything
                                    else that is deemed hazardous is prohibited.
                                    The Security and Prometeo '23 team's
                                    decision shall be final if there are any
                                    disputes.
                                </li>
                                <li>
                                    Throughout the fest of Prometeo '23, no
                                    outside vehicles will be permitted on
                                    campus.
                                </li>
                                <li>
                                    All participants are expected to maintain
                                    the campus's decorum and cleanliness as well
                                    as to diligently and consistently abide by
                                    its rules and regulations.
                                </li>
                                <li>
                                    IIT Jodhpur and its students disclaim all
                                    liability for any accidents that may or may
                                    not happen during the course of Prometeo
                                    '23.
                                </li>
                                <li>
                                    To prevent any unauthorized activities on
                                    campus, random checks would be conducted.
                                </li>
                                <li>
                                    Any commodities issued to the guests would
                                    have to be returned in sound condition to
                                    the organizers during check-out.
                                </li>
                                <li>
                                    Anyone found visiting a hostel other than
                                    the one that is designated will be penalized
                                    and appropriate action will be taken against
                                    them.
                                </li>
                                <li>
                                    Hostel guests must take care to prevent
                                    damage to the institute's property and
                                    facilities, since those found guilty of such
                                    behavior will be responsible for covering
                                    any necessary repairs.
                                </li>
                                <li>
                                    The administration will not be held liable
                                    for any damage or loss of property or
                                    valuables of the participants stored in
                                    places of lodging.
                                </li>
                                <li>
                                    Participants are requested to refrain from
                                    causing any disruptions to their other
                                    participants.
                                </li>
                                <li>
                                    Institute will provide the{" "}
                                    <strong>pickup and drop facility</strong> to
                                    the participants between bus/railway
                                    stations and campus during the dates and
                                    times listed below:
                                </li>
                            </ol>
                        </span>
                    </div>
                </div>

                {/* <div className="acc-content">
                    <div className="acc-content-title">
                        Instructions
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-right">
                            <ol>
                                <li>
                                    {" "}
                                    All guests carrying electronic items of any
                                    kind will have to declare them at the IIT
                                    Jodhpur main gate through a ‘Gate Pass'. The
                                    belongings will also be checked on the way
                                    out of IIT Jodhpur along with the ‘Gate
                                    Pass', failing to do so will result in the
                                    belongings being impounded.
                                </li>
                                <li>
                                    All guests will be provided with mattress.
                                    Prometeo will not provide mattress cover,
                                    blankets or pillows. The guests are
                                    encouraged to arrange them on their own (if
                                    required), since the weather might get cold
                                    during the night.
                                </li>
                                <li>
                                    {" "}
                                    Any commodities issued to the guests would
                                    have to be returned in sound condition to
                                    the organisers during check-out
                                </li>
                                <li>
                                    {" "}
                                    Random checks would be made to avoid any
                                    illegal stay at the campus. Any team failing
                                    to produce their electronic/physical
                                    receipts of accommodation would be heavily
                                    fined and disqualified.
                                </li>
                                <li>
                                    Entry will be only through the 'Main Gate'
                                    of IIT Jodhpur. All other gates will be
                                    closed for entry.
                                </li>
                                <li>
                                    All guests are required to carry their valid
                                    government photo id proofs at all times. In
                                    addition, the student participants are also
                                    required to carry their valid College photo
                                    id card. Any guest failing to produce their
                                    id card will not be permitted inside the
                                    campus during Prometeo 2023.
                                </li>
                                <li>
                                    Alcohol, drugs, sharp objects and explosives
                                    of any kind are strictly prohibited inside
                                    the campus. Any other item if deemed unsafe
                                    will be prohibited. The decision of Security
                                    and Prometeo team will be final in case of
                                    any disputes.
                                </li>
                                <li>
                                    No outside vehicles will be allowed into the
                                    campus during the Prometeo 2023."
                                </li>
                                <li>
                                    {" "}
                                    All guests are required to maintain the
                                    decorum and cleanliness of the campus, and
                                    follow the rules of the campus at all times.
                                </li>
                                <br></br>
                            </ol>
                            Prometeo 2023 and IIT Jodhpur will not be
                            responsible for any mishaps that occur through the
                            duration of stay for Prometeo 2023
                        </span>
                    </div>
                </div> */}

                <div className="acc-content">
                    <div className="acc-content-title">
                        FAQ's
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-right">
                            <ol className="acc-plain-list acc-faq">
                                <li>
                                    <span>
                                        <strong>Q.</strong> What are the
                                        accommodation charges?
                                    </span>
                                    <span>
                                        <strong>A.</strong> The accommodation
                                        charges and other important details will
                                        be available on the website or will be
                                        notified by the PR team soon.
                                    </span>
                                </li>
                                <li>
                                    <span>
                                        <strong>Q.</strong> Will all the team
                                        members be given accommodation at the
                                        same place?
                                    </span>
                                    <span>
                                        <strong>A.</strong> We will try but
                                        there is no surety of the same.
                                    </span>
                                </li>
                                <li>
                                    <span>
                                        <strong>Q.</strong> What kind of
                                        accommodation will be provided?
                                    </span>
                                    <span>
                                        <strong>A.</strong> Accommodation will be provided on a
                                        shared basis inside campus hostels or
                                        outside hotels. One mattress, and enough
                                        space for keeping luggage, and other
                                        essential commodities will be provided.
                                        Girls and boys will be accommodated
                                        separately. Number of participants in a
                                        room will be decided by Techfest and
                                        will be allotted by the Prometeo '23
                                        team.
                                    </span>
                                </li>
                                <li>
                                    <span>
                                        <strong>Q.</strong> Does the
                                        accommodation charges include food
                                        facilities too?
                                    </span>
                                    <span>
                                        <strong>A.</strong> No, food facilities
                                        are not included in the accommodation
                                        charges. Participants can purchase their
                                        meals from food court, Shamiyana -
                                        Institute Cafe or Hostel mess. There are
                                        two hostel messes: one veg & one
                                        non-veg.
                                    </span>
                                </li>
                                <li>
                                    <span>
                                        <strong>Q.</strong> Can I enter the
                                        IIT-J Campus anytime?
                                    </span>
                                    <span>
                                        <strong>A.</strong> You can enter IIT
                                        Main gate anytime by showing valid photo
                                        ID proof during 6am to 10pm.
                                    </span>
                                </li>
                            </ol>
                        </span>
                    </div>
                </div>

                {/* <div className="acc-content">
                    <div className="acc-content-title">
                        Contact Us
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-right">
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit, sed do eiusmod tempor incididunt ut labore et
                            dolore magna aliqua. Ut enim ad minim veniam, quis
                            nostrud exercitation ullamco laboris nisi ut aliquip
                            ex ea commodo consequat. Duis aute irure dolor in
                            reprehenderit in voluptate velit esse cillum dolore
                            eu fugiat nulla pariatur. Excepteur sint occaecat
                            cupidatat non proident, sunt in culpa qui officia
                            deserunt mollit anim id est laborum
                            <br></br>
                            Duis aute irure dolor in reprehenderit in voluptate
                            velit esse cillum dolore eu fugiat nulla pariatur.
                            Excepteur sint occaecat cupidatat non proident, sunt
                            in culpa qui officia deserunt mollit anim id est
                            laborum.
                            <br></br>
                        </span>
                    </div>
                </div> */}
                {/* <div className="ca-content">
                    <div className="ca-content-title">INCENTIVES</div>
                    <div className="ca-content-text ca-incentive">
                        <div className="ca-content-incentive">
                            <div className="ca-content-incentive-title silver">
                                SILVER <span>Campus Ambassador</span>
                                <div>15+ Registrations</div>
                            </div>
                            <div className="ca-content-incentive-desc">
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="white-shadow2"
                                        src={concert}
                                        alt="concert"
                                    />
                                    Free Accommodation and Pronite Pass
                                </div>
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="yellow-shadow2"
                                        src={certificate}
                                        alt="certificate"
                                    />
                                    Certificate
                                </div>
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="blue-shadow2"
                                        src={goodies}
                                        alt="goodies"
                                    />
                                    Goodies (T-shirt)
                                </div>
                            </div>
                        </div>
                        <div className="ca-content-incentive">
                            <div className="ca-content-incentive-title gold">
                                GOLD <span>Campus Ambassador</span>
                                <div>25+ Registrations</div>
                            </div>
                            <div className="ca-content-incentive-desc">
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="white-shadow2"
                                        src={concert}
                                        alt="concert"
                                    />
                                    Free Accommodation and Pronite Pass
                                </div>
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="yellow-shadow2"
                                        src={certificate}
                                        alt="certificate"
                                    />
                                    Certificate
                                </div>
                                <div className="ca-content-incentive-desc-item">
                                    <img src={goodies} alt="goodies" />
                                    Goodies (Hoodie, Vouchers)
                                </div>
                                <div className="ca-content-incentive-desc-item">
                                    <img
                                        className="yellow-shadow2"
                                        src={tickets}
                                        alt="workshop"
                                    />
                                    Free Entry to 1 Workshop
                                </div>
                            </div>
                        </div>
                    </div>
                </div> */}

                {/* <div className="acc-content">
                    <div className="acc-content-title">
                        REGISTRATION
                    </div>
                    <div className="acc-content-text">
                        <span className="acc-content-desc-left acc-register">
                            So, grab the opportunity and register ASAP!
                            <button
                                id="acc-register-button"
                                className="acc-button-48"
                                // onClick={handleSubmit}
                            >
                                <span className="button-text">
                                    Register Now !
                                </span>
                            </button>
                        </span> */}
                        {/* <img
                            className="acc-content-img blue-shadow acc-pr-logo"
                            src={logo}
                            alt="social-media"
                        /> */}
                    {/* </div> */}
                {/* </div> */}
            </div>
        </FadeIn>
    );
}
