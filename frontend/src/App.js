import Header from './components/Header';
import './App.css';
import NoteListPage from './pages/NoteListPage.jsx'
import { Route, Routes } from 'react-router-dom';
import NotePage from './pages/NotePage';
function App() {
  return (

    <div className="container dark">
      <div className="app">
        <Header />
        <Routes>
          <Route path='' element={<NoteListPage />} />
          <Route path='/note/:id' element={< NotePage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
