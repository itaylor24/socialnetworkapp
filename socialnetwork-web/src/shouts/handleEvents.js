export function handleMouseEvents(){
    const parentShouts = Array.from(document.getElementsByClassName('shout-parent')); 

    parentShouts.forEach(shout=>{
      shout.addEventListener('mouseover',stopChild); 
      shout.addEventListener('mouseleave',enableChild); 
    })

    const shouts = Array.from(document.getElementsByClassName('shout-object')); 

    shouts.forEach(replyShout=>{
        replyShout.addEventListener('mouseover',stopParent); 
        replyShout.addEventListener('mouseleave',enableParent); 
      })
  }
  

function stopChild(evt){
    const child = evt.currentTarget.parentElement.parentElement.parentElement.parentElement; 
    child.classList.remove("shout-clickable"); 


}

function enableChild(evt){
    const child = evt.currentTarget.parentElement.parentElement.parentElement.parentElement; 
    child.classList.add("shout-clickable"); 
}

function stopParent(evt){
    const parent = evt.currentTarget.parentElement.parentElement.parentElement.parentElement; 
    parent.classList.remove("shout-clickable"); 


}

function enableParent(evt){
    const parent = evt.currentTarget.parentElement.parentElement.parentElement.parentElement; 
    parent.classList.add("shout-clickable"); 
}