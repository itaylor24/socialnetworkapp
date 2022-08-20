import React from 'react'; 
import {apiShoutCreate} from './lookup'


export function ShoutCreateForm(props){
    const {didShout} = props; 
    const textAreaRef = React.createRef(); 
 
    const handleBackendUpdate = (response, status) =>{
        //api response handler
        if(status === 201){
            didShout(response); 
        }else{
            
            alert("An error occurred, please try again."); 
        }
    }

    const handleSubmit = function (evt){
        //api request 
        //evt.preventDefault(); 
        const newValue = textAreaRef.current.value;
        apiShoutCreate(newValue,handleBackendUpdate); 
        textAreaRef.current.value = ' '
    }

    
    return <div className = 'col-12 mb-3'>
    <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} placeholder="Shout something..."required className='form-control'></textarea>
        <button type='submit' className='boost-button my-3'>Shout</button>

    </form>
</div>
}