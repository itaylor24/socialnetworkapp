import {backendLookup} from '../lookup'; 

export function apiShoutCreate(newShout, callback){
    backendLookup("POST","/shouts/create/",callback,{content:newShout})
}
export function apiShoutList(username,callback,nextUrl){
    let endpoint = '/shouts/'
    if(username!== ""){
       endpoint = `/shouts/?username=${username}`
    } 
    if(nextUrl!==null &&  nextUrl!== undefined){
        endpoint = nextUrl.replace("http://localhost:8000/api",""); 
    }

    backendLookup("GET",endpoint, callback)
}

export function apiShoutAction(shoutId, action, callback){
    const data = {id: shoutId, action: action}
    backendLookup("POST","/shouts/action/", callback, data)
}

export function apiShoutDetail(shoutId,callback){
    backendLookup("GET",`/shouts/${shoutId}`, callback)
}

export function apiShoutFeed(callback,nextUrl){
    let endpoint = '/shouts/feed'
    if(nextUrl!==null &&  nextUrl!== undefined){
        endpoint = nextUrl.replace("http://localhost:8000/api",""); 
    }
 
    backendLookup("GET",endpoint, callback)
}