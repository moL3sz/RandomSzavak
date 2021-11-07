


const commandList = {
    'curl':`curl -X POST -H 'Content-Type: application/json' -d '{
        "size":<span class="own-p">{szómennyiség:int}</span>,
        "l": <span class="own-p">{szóhossz:int}</span>,
        "sw": <span class="own-p">{szókezdet:string}</span>
        "access_token":<span class="own-p">{használati_token:string}</span> 
                                                              
    }'  https://random-magyar-words-api.herokuapp.com/getwords`
}
export default commandList;