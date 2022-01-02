import React from "react";
import { Bar } from 'react-chartjs-2';

class DisplayData extends React.Component{
    constructor(props){
        super(props);
        this.list = props.dataSet;
    }


    render(){
        let returned = ``;
        this.list.forEach(element => {
            returned = returned + element.toStringExt() + "\n";
        });
        return <text><NewlineText text={returned}/></text>;
    }


}

function NewlineText(props) {
    const text = props.text;
    const newText = text.split('\n').map(str => <p>{str}</p>);
    
    return newText;
}

export default DisplayData;