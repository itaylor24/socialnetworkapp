import React, {useEffect, useState} from 'react'; 
import {apiShoutList} from './lookup'
import {Shout} from './detail'
import {handleMouseEvents} from './handleEvents'; 

export function ShoutsList(props){
    const {filterUsername,didShout} = props; 
    const [shoutsInit, setShoutsInit] = useState([]); 
    const [shouts, setShouts] = useState([]); 
    const [nextUrl, setNextUrl] = useState(null); 
    const [shoutsDidSet, setShoutsDidSet] = useState(false); 
    

    useEffect(()=>{
        const final = [...props.newShouts].concat(shoutsInit); 
        if(final.length !== shouts.length){
            setShouts(final); 
        }
        handleMouseEvents(); 
        
    },[props.newShouts,shouts,shoutsInit]) 


    /*useEffect(()=>{
        document.addEventListener('scroll', function(e) {
            let documentHeight = document.body.scrollHeight;
            let currentScroll = window.scrollY + window.innerHeight;
            // When the user is [modifier]px from the bottom, fire the event.
            let modifier = 20; 
            let canLoad; 

            

            
              
            if(currentScroll + modifier > documentHeight) {
                handleLoadNext(); 
                window.scrollBy({top:-400,left:0,behavior:'instant'}); 
                console.log("??????");
                canLoad = false; 
                 
            }
           
        }); 
        console.log("YO IM DONE"); 
    },[]);*/  

    useEffect(()=>{
        
        if(shoutsDidSet === false){
            const handleShoutListLookup = (response, status)=>{
            if(status===200){ 
                setNextUrl(response.next)
                setShoutsInit(response.results);
            
                setShoutsDidSet(true); 
            }else{
            }
            
            }
            
            if(filterUsername){
                apiShoutList(filterUsername,handleShoutListLookup);
            }else{
                apiShoutList("",handleShoutListLookup);
            }
            
            
        }
        
        
    },[shoutsInit, shoutsDidSet, setShoutsDidSet,filterUsername,shouts]); 


    const handleDidBoost = (newShout) =>{

        didShout(newShout); 
        const updatedShoutsInit = [...shoutsInit]
        updatedShoutsInit.unshift(newShout); 
        setShoutsInit(updatedShoutsInit);

        const updateFinalShouts = [...shouts]
        updateFinalShouts.unshift(newShout); 
        setShouts(updateFinalShouts); 
        window.location.reload(); 

        
    }

    const handleLoadNext = () =>{
        //evt.preventDefault(); 
        
        if(nextUrl!==null){
           
            const handleLoadNextResponse = (response,status)=>{
                if(status===200){
                    setNextUrl(response.next); 
                    const tempShoutsInit = shoutsInit.concat(response.results); 
               
                    setShoutsInit(tempShoutsInit); 
                    setShouts(tempShoutsInit); 
             
                }
            }
            if(filterUsername){
                apiShoutList(filterUsername,handleLoadNextResponse,nextUrl); 
            }else{
                apiShoutList("",handleLoadNextResponse,nextUrl);
            }
            
        }
    }
   

    return <React.Fragment>
            {shouts.map((item,index)=>{
                return <Shout shout={item}  didShout = {handleDidBoost} key={`${index}-${item.id}`} className='my-5 py-5 px-5 border rounded text-dark' />
            })}
        {nextUrl != null && <button onClick={handleLoadNext} className="button">Load Next</button>}
        </React.Fragment>
    
    
        
}