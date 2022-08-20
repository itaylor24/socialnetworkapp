import React, {useEffect, useState} from 'react'; 
import {ShoutsList} from './list'; 
import {ShoutCreateForm} from './create'; 
import {apiShoutDetail} from './lookup'; 
import {Shout} from './detail'; 
import {handleMouseEvents} from './handleEvents'; 
import { FeedList } from './feed';

export function ShoutsComponent(props){
    const canShout = props.data.canShout === 'false' ? false: true ; 
    const username = props.data.username; 
    const [newShouts, setNewShouts] = useState([]); 

    useEffect(() => {
        handleMouseEvents(); 
    }, []);


    const handleNewShout = (newShout) =>{
        let tempNewShouts = [...newShouts]; 
        tempNewShouts.unshift(newShout);
        setNewShouts(tempNewShouts); 
       
    }

    return <div className={props.className}>
            {canShout && <ShoutCreateForm didShout = {handleNewShout}/>}
            <ShoutsList didShout = {handleNewShout} newShouts={newShouts} filterUsername={username}/> 
            </div>
        
}

export function FeedComponent(props){
    const canShout = props.data.canShout === 'false' ? false: true ; 
    const username = props.data.username; 
    const [newShouts, setNewShouts] = useState([]); 

    useEffect(() => {
        handleMouseEvents(); 
    }, []);


    const handleNewShout = (newShout) =>{
        let tempNewShouts = [...newShouts]; 
        tempNewShouts.unshift(newShout);
        setNewShouts(tempNewShouts); 
       
    }

    return <div className={props.className}>
            {canShout && <ShoutCreateForm didShout = {handleNewShout}/>}
            <FeedList didShout = {handleNewShout} newShouts={newShouts} filterUsername={username}/> 
            </div>
        
}



export function ShoutDetailComponent (props){
    const {shoutId} = props.data; 

    useEffect(() => {
        handleMouseEvents(); 
    }, []);


    
    const [didLookup, setDidLookup] = useState(false); 
    const [shout, setShout] = useState(null); 
    const handleBackendLookup = (response, status)=>{
        
        if(status === 200){
            setShout(response); 
            
        }else{
            alert("An error occured finding this shout"); 
        }
    }
    useEffect(()=>{
        if(didLookup === false){
            apiShoutDetail(shoutId, handleBackendLookup); 
            setDidLookup(true); 
        }
    },[didLookup,setDidLookup,shoutId])

    return shout === null ? null : <Shout shout={shout} className ='my-5 py-5 px-5 border rounded text-dark'/>
} 

  



  
