import React,{useState} from "react";
export default function Terminal(props){

    const CopyCommand = ()=>{
        const command = document.getElementById("command").textContent;
        navigator.clipboard.writeText(command)
        setCopied(true)
    }
    const [copied, setCopied] = useState(false)
    return ( 
        <div className="tool-container">
            <div className="tool-type">
                {props.type}
            </div>
            <div className="terminal-builtin">
                <span className="prompt">$ </span>
                <span dangerouslySetInnerHTML={{__html: props.command}} id="command" className="command"></span>
                <div className="copy-command">
                    <i class="fa fa-copy" onClick={CopyCommand}></i>
                </div>
            </div>
            {
                copied ? <span className="clipboard-success">
                    Command copied! <i class="fa fa-check"></i>
                </span> : ""
            }
            <h3 className="p-title">Paraméterek</h3>
            <div className="parameters">
                <div className="param">
                    <span>size</span>
                </div>
                <div className="opt">opcionális</div>
                <div className="p-desc">Üres érték esetén az alapértelmezett értek 10. Ez a paraméter adja meg hogy összesen mennyi szóval térjen vissza a API. Ha kevesebb szó létezik mint amennyit megadott akkor a maximális lehetséges szómennyiséggel tér vissza.</div>
                
                <div className="param">
                    <span>l</span>
                </div>
                <div className="opt">opcionális</div>
                <div className="p-desc">Ha üres akkor random hosszúságuakat választ ki. Ez a paraméter beállítja, hogy azokat a szavakat listázza ki amelyeknek a hossza ennyi.</div>
                <div className="param">
                    <span>sw</span>
                </div>
                <div className="opt">opcionális</div>
                <div className="p-desc">
                    Ha az érték nem üres akkor azokat az szavakat adja vissza amelyek ezzel kezdődnek.
                </div>
                <div className="param">
                    <span>access_token</span>
                </div>
                <div className="opt">szükséges</div>
                <div className="p-desc">
                    Az előbbiekben generált használati tokent kell megadni, hogy az API teljes szolgáltatását tudja használni.
                </div>
            </div>
        </div>

    );
}