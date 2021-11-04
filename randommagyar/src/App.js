import logo from './logo.svg';
import './App.css';
import {useState} from "react"
import $ from "jquery"

const DEFAULT_SIZE = 10;
const DEFAULT_STARTWITH = "*"
const DEFAULT_LENGTH = "*"






function App() {
  const [words, setWords] = useState({"words":[]})
  const [sortByName_ASC_DESC, setSortName_ASC_DESC] = useState(true) //true ASC, false DESC
  const [sortByLenght_ASC_DESC, setSortLenght_ASC_DESC] = useState(true) 

  const sortWordsByName = () =>{
    const currentWords = words
    currentWords.words.sort( (a, b) => a.localeCompare(b, 'hu', {ignorePunctuation: true}));
    if(!sortByName_ASC_DESC){
      currentWords.words.reverse();
    }
    setSortName_ASC_DESC(!sortByName_ASC_DESC)
    console.log(currentWords.words)
    setWords(currentWords)
  }
  const sortWordsByLength = ()=>{
    const currentWords = words
    
    currentWords.words.sort((a,b) => {
      return sortByLenght_ASC_DESC ? a.length-b.length : b.length-a.length
    }) 
    setSortLenght_ASC_DESC(!sortByLenght_ASC_DESC)

    setWords(currentWords)
  }


  const setGridTemplate = (size) =>{
    const numCol = parseInt(size/10) <= 5 ? parseInt(size/10) : 5
    console.log(numCol)
    $(".words-list").css("grid-template-columns",`repeat(${numCol},7em)`)
  }


  const getWords = ()=>{
    const numberOfWords = document.getElementById("number-of-words").value;
    const startWith = document.getElementById("word-startwith").value;
    const length = document.getElementById("word-length").value;

    const N = numberOfWords != "" ? numberOfWords : DEFAULT_SIZE;
    const sW = startWith != "" ? startWith : DEFAULT_STARTWITH;
    const l = length != "" ? length : DEFAULT_LENGTH;
    const formData = {
      size: N,
      sw: sW
    }
    const url = `http://127.0.0.1:5000/getwords/${N}/${sW}/${l}`
    fetch(url,{
      method:"GET",
      mode:"cors",
    })
    .then(res => res.json())
    .then(res =>{
      //make the wordlist columns
      setGridTemplate(res.words.length)
      setWords(res)
    })

    
  }
  return (
    <div className="content">
      <div className="generator">
        <div className="generator-title">
          <h2>Random magyar szó generator</h2>
        </div>
        <div className="use-generator">
          <div className="filters">
            <label htmlFor="number-of-words">Szó mennyiség</label>
            <label htmlFor="word-startwith">Mivel kezdődjön</label>
            <label htmlFor="word-length">Szó hossz</label>
            <label htmlFor="start"></label>
            <input type="text" id="number-of-words"/>
            <input type="text" id="word-startwith"/>
            <input type="text" id="word-length"/>

            <button className="mehet-fetch" onClick={getWords}>Mehet</button>
          </div>
        </div>
      </div>
      <div className="generated-words">
        <h2 style={
          {
            textDecoration:"underline",
            textAlign:"center"      
          }}> Generált szavak</h2>
          <div className="words-sorter" style={
            {
              marginBottom: "20px"
            }
          }>
            <h2>Rendezés: </h2>
            <div className="sort-by-name">
              Név: <i className={!sortByName_ASC_DESC ? "fa fa-sort-amount-asc" : "fa fa-sort-amount-desc"} onClick={sortWordsByName}></i>
            </div>
            <div className="sort-by-length">
              Hossz: <i className={!sortByLenght_ASC_DESC ? "fa fa-sort-amount-asc" : "fa fa-sort-amount-desc"} onClick={sortWordsByLength}></i>
            </div>
          </div>
        <div className="words-list">
          {
            words.words.map(word => {
              return (
                <div className="word-item">
                  {word}
                </div>
              )
            })
          }
        </div>
      </div>
    </div>
  );
}

export default App;
