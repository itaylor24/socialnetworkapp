import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { ShoutsComponent, ShoutDetailComponent,FeedComponent} from './shouts';
import { ProfileBadgeComponent } from './profiles';

const appEl = document.getElementById('root');
if(appEl){
  ReactDOM.createRoot(appEl).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}


const shoutsEl = document.getElementById('socialnetwork'); 
if(shoutsEl){
  
  ReactDOM.createRoot(shoutsEl).render(
      <ShoutsComponent data={shoutsEl.dataset}/>
  );


}

const feedEl = document.getElementById('socialnetwork-feed'); 
if(feedEl){
  
  ReactDOM.createRoot(feedEl).render(
      <FeedComponent data={feedEl.dataset}/>
  );


}


const shoutDetailElements = document.querySelectorAll('.shout-detail'); 
shoutDetailElements.forEach(container=>{
  console.log(container.dataset); 
  ReactDOM.createRoot(container).render(
    <ShoutDetailComponent data={container.dataset}/>
  );
})


const profileDetailElements = document.querySelectorAll('.profile-badge'); 
profileDetailElements.forEach(container=>{
  console.log(container.dataset); 
  ReactDOM.createRoot(container).render(
    <ProfileBadgeComponent data={container.dataset}/>
  );
})





// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
