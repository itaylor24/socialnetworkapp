import {backendLookup} from '../lookup'; 



export function apiProfileDetail(username,callback){
    backendLookup("GET",`/profiles/${username}/`, callback)
    console.log("WORKING?", username)
}
export function apiProfileFollowToggle(username,action,callback){
    let data = {"action":action}; 
    backendLookup("POST",`/profiles/${username}/follow/`, callback, data); 
    console.log("WORKING?", username)
}
