import React from 'react'; 
import {apiShoutAction} from './lookup'

export function ActionBtn(props){
    const {shout,action,didPerformAction} = props; 
    const likes = shout.likes ? shout.likes: 0; 
    //const [likes, setLikes] = useState(shout.likes ? shout.likes : 0); 
    //const [userLike, setUserLike] = useState(shout.userLike === true ? true: false); 
    const actionDisplay = action.display ? action.display: "Action"; 
    const display = action.type === 'like' ? `${likes} ${action.display}` : actionDisplay; 
    const handleActionBackendEvent = (response, status) =>{
        
        if((status === 200 || status === 201) && didPerformAction){
            didPerformAction(response,status); 

        }
        
    
        /*
        if(action.type === 'like'){
            if(userLike === true){
                
                 
                
            }else{
                setUserLike(true); 
                setLikes(shout.likes+1); 
            }
            

        }*/ 
        
        
    }
    let buttonStatus; 
    let buttonMethod; 

    if(action.type === 'like'){
        buttonStatus = !shout.did_like ? 'unlike-button' : 'like-button' ; 
        buttonMethod = !shout.did_like ? 'like' : 'unlike'; 
    }else if(action.type === 'boost'){
        buttonStatus = 'boost-button' ; 
        buttonMethod = 'boost'; 
    }else if(action.type === 'reply'){
        buttonStatus = 'reply-button' ; 
        buttonMethod = 'reply'; 
    }
    

    
    
    
    const handleClick = (event)=>{
        
        event.preventDefault(); 
        event.stopPropagation(); 
        apiShoutAction(shout.id, buttonMethod, handleActionBackendEvent)  
    
    }

    
    return <button onClick = {handleClick} className={buttonStatus ? buttonStatus : ' button mb-3'}> {display} </button>  
    
  }



export function DeleteBtn(props){

    const {shout,didPerformAction} = props; 
    //const [likes, setLikes] = useState(shout.likes ? shout.likes : 0); 
    //const [userLike, setUserLike] = useState(shout.userLike === true ? true: false); 
    const handleActionBackendEvent = (response, status) =>{
        
        if((status === 200 || status === 201) && didPerformAction){
            didPerformAction(response,status); 

        }
        
    
        /*
        if(action.type === 'like'){
            if(userLike === true){
                
                 
                
            }else{
                setUserLike(true); 
                setLikes(shout.likes+1); 
            }
            

        }*/ 
        
        
    }
   
    
    
    
    const handleClick = (event)=>{
        
        event.preventDefault(); 
        event.stopPropagation(); 
        apiShoutAction(shout.id, '', handleActionBackendEvent)  
    
    }

    return <button onClick = {handleClick} className={'delete-button button'}> Delete </button>  
    

}