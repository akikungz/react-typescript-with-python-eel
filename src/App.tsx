import './App.css'

// @ts-ignore
const eel = window["eel"];

function App() {

  eel.stop()

  return (
    <>
      <button onClick={eel.stop}>Stop</button>
    </>
  )
}

export default App
export { eel }