import React, {useState, useEffect} from 'react' 
import { apiProfileDetail , apiProfileFollowToggle} from './lookup';
import { handleMouseEvents } from '../shouts/handleEvents';
import { UserPicture} from './components';
import { displayCount } from '../shouts/utils';

function ProfileBadge(props){
    const {profile, didFollowToggle, profileLoading} = props; 
    let currentAction = profile && profile.is_following === true ? "unfollow": "follow"; 
    currentAction = profileLoading ? "loading" : currentAction; 

    const handleFollowToggle = (evt) =>{
        evt.preventDefault(); 
        if(didFollowToggle && !profileLoading){
            didFollowToggle(currentAction); 
        }
    }
    return profile ? <div>
        <UserPicture username={profile.username} />
        <p className="link ">{profile.displayname} {" "}<span className="text-muted">@{profile.username}</span></p>
        <p className="mx-5"><span className="follow-status mx-4">{displayCount(profile.follower_count)} {profile.follower_count === 1 ? "follower" : "followers"}</span>{" "}<span className="follow-status">{displayCount(profile.following_count)} following</span></p>
        <button onClick={handleFollowToggle} className={"button " + (profile.is_following === true ? "unfollow-button": "follow-button")}>{profile.is_following === true ? "Unfollow": "Follow"}</button>
        <p>{profile.bio}</p>
        </div> : null 

}
export function ProfileBadgeComponent(props){
    const {username} = props.data; 
    //lookup 

    
    useEffect(() => {
        handleMouseEvents(); 
    }, []);


    
    const [didLookup, setDidLookup] = useState(false); 
    const [profile, setProfile] = useState(null); 
    const [profileLoading, setProfileLoading] = useState(false); 

    const handleBackendLookup = (response, status)=>{
        console.log(response); 
        if(status === 200){
            setProfile(response); 
            console.log("PROFILELOOKUP?")
        }
    }
    useEffect(()=>{
        if(didLookup === false){
            apiProfileDetail(username, handleBackendLookup); 
            setDidLookup(true); 
        }
    },[didLookup,setDidLookup,username])

    const handleFollowAction = (action)=>{
        console.log(action); 
        apiProfileFollowToggle(username,action,(response, status)=>{
            console.log(response); 
            setProfileLoading(false);
            if(status === 200){
                setProfile(response); 
            }
            
        }); 
        setProfileLoading(true); 
    }
    return didLookup === false ? "Loading..." : profile ? <ProfileBadge profile = {profile} didFollowToggle={handleFollowAction} profileLoading={profileLoading}/>: null 
}