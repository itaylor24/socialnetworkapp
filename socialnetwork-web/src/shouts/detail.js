import React, {useEffect, useState} from 'react'; 
import {ActionBtn} from './buttons'; 
import { handleMouseEvents } from './handleEvents';

import {UserLink, UserPicture} from '../profiles'; 

export function ParentShout(props){
    const {shout} = props;  

    return <div className='row mt-5 mb-5 '>
        <div className="col-11 mx-auto p-3 border shout-clickable shout-parent">
            <p className='mb-0 mb-3 small text-muted'>Boost</p>
            <Shout hideActions className='col-12' type="shout-parent" shout={shout.parent}/>
        </div>
    </div>
}
export function Shout(props){
    const {shout,didShout,hideActions} = props
    const [actionShout,setActionShout] = useState(props.shout ? props.shout : null); 
    //const [shoutChildren, setShoutChildren] = useState(shout.children ? shout.children: null); 
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    const path = window.location.pathname; 

    const match = path.match(/(?<shoutid>\d+)/);
    const urlShoutId = match ? match.groups.shoutid: -1; 
    const isDetail = `${shout.id}` === `${urlShoutId}`; 

    const handleLink = (event) =>{
        event.preventDefault(); 
        event.stopPropagation(); 
        window.location.href= `/${shout.id}`;  
    }
    

    const handlePerformAction = (newActionShout, status)=>{
        if(status === 200){
            setActionShout(newActionShout)
        }else if (status === 201){
            if(didShout){
                didShout(newActionShout); 
            }

        }
        
        
    }
    
    
   
    useEffect(()=>{
        handleMouseEvents(); 
    },[]); 

    /*const handlePerformReplyAction = (newShoutChild, status)=>{
        const tempShoutChildren = newShoutChild.children; 
        setShoutChildren(tempShoutChildren); 
        
    }*/ 

    return <div className={props.type === 'shout-parent' || isDetail===true ? "": "shout-clickable"} onClick={isDetail === true ? null: handleLink}>
        
         
        <div className={className}>

                
            
                

            {/*<div className ="d-flex flex-column align-items-end mb-4">{(shout.is_same_user && !shout.thread_parent && hideActions !== true) && <DeleteBtn shout = {actionShout}/>}</div>*/}
         

                <div>
                    
                    <p><UserPicture username={shout.username}/>{" "}<UserLink includeFullName={true} user={shout.user} username={shout.username} displayName={shout.user.displayname ? shout.user.displayname : shout.user_display_name} timestamp={shout.timestamp}/></p>
                    <p className="d-flex mt-2 mb-4 py-2 text-wrap mx-4">{shout.content && shout.content} </p>
                    {
                    shout.parent && 
                    <ParentShout shout={shout} />
                    
                    }
                </div>
                
                { !shout.thread_parent && <div className="btn-group">
                {(actionShout && hideActions !== true ) && <React.Fragment>
                        <ActionBtn shout = {actionShout} didPerformAction = {handlePerformAction} action={{type:"like",display:"Likes"}}/>
                        <ActionBtn shout = {actionShout} didPerformAction = {handlePerformAction} action={{type:"boost",display:"Boost"}}/>
                        {/*<ActionBtn shout = {actionShout} didPerformAction = {handlePerformReplyAction} action={{type:"reply",display:"Reply"}}/>*/}
                       
                    </React.Fragment>}   

                    
                </div>}
                {/*
                {shoutChildren && shoutChildren.length > 0 && <div className="mt-5">{shoutChildren.length} {shoutChildren.length === 1 ? "Reply" : "Replies"}  </div>}
                <div className="mt-5">
                    
                    {
                        
                        shoutChildren && shoutChildren.map((item,index)=>{
                            return <Shout shout={item} key={`${index}-{item.id}`} className='py-5 px-5 mb-2 border text-dark shout-object' />
                    })}
                    
                        
                </div>*/}

                </div>
            
            </div>
            
}