import React from 'react'; 
import { toCorrectDate } from '../shouts/utils';



export function UserLink(props){
    const {user,displayName,username,timestamp} = props; 
    const nameDisplay = displayName; 

    const handleUserLink = (evt)=>{
        evt.preventDefault(); 
        evt.stopPropagation(); 
        window.location.href= `/profile/${username}`
    } 

    return <span className=" py-2 link"><span>{nameDisplay}<span className="text-muted">{" "}<span className="user-link" onClick={handleUserLink}>@{username}</span> {" | "} {toCorrectDate(timestamp)}</span></span>{" "}{user.is_following === true &&<span className="following-badge button"> Following</span>}</span>
}
export function UserPicture(props){
    const handleUserLink = (evt)=>{
        evt.preventDefault(); 
        evt.stopPropagation(); 
        window.location.href= `/profile/${username}`
    } 
    const {username} = props; 
    return <span onClick= {handleUserLink} className='circle bg-dark text-white mx-3 profile'>{username[0].toUpperCase()}</span>
}