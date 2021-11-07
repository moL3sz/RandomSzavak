import { useState } from "react";
import {useCookies} from "react-cookie"


export default function TokenGeneration(){
    const [cookies, setCookie] = useCookies(['access_token'])
    const [token, setToken] = useState(cookies.access_token ? cookies.access_token : "")
    const widthOffset = 15;
    const DEFAULT_LENGTH = 64+widthOffset;
    const generateToken = ()=>{
        fetch("https://random-magyar-words-api.herokuapp.com/generate_token",{
          method:"GET"
        })
        .then(res => res.json())
        .then(res=>{
            const [year,month,day] = res.experation_date.split("-").map(e => parseInt(e))
            const expires_date = new Date(year,month-1,day,12)
            if(!cookies.access_token){
                setCookie("access_token",res.access_token,{path:"/",expires:expires_date})
            }
            setToken(res.access_token)
        })
    }

    const CopyToken = ()=>{
        if(token === ""){
            return
        }
        //send a request to the server to generate a token for us,
        //agree with the user to store the token in the cookie
    }
    return(
        <div className="div-token-gen">
            <div className="token-place" style={{
            }}>
                {
                    token != "" ? <div className="current-token">{token}</div> : <div className="current-token">
                        Nincs még token generálva.
                    </div>
                }
                <div className="copy-token">
                    <i className="fa fa-copy" onClick={CopyToken}></i>
                </div>
            </div>
            <div className="generate-token">
                <button onClick={generateToken} className="token-generate-button">Generálás</button>
            </div>
            
        </div>
    )
}