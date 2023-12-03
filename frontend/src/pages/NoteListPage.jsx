import React, { useEffect, useState } from 'react'
import ListItem from '../components/ListItem';
import AddButton from '../components/AddButton';

const NoteListPage = () => {
    let [notes, setNotes] = useState([]);
    useEffect(() => {
        fetchData()
    }, [])
    let fetchData = async () => {
        let getData = await fetch('http://127.0.0.1:8000/api/notes/')
        let data = await getData.json()
        setNotes(data)
    }
    return (
        <div className="notes">
            <div className="notes-header">
                <h2 className='notes-title'>&#9782; Notes</h2>
                <p className="notes-count">{notes.length}</p>
            </div>
            <div className='notes-list'>
                {notes.map((note) => (<ListItem key={note.id} note={note} />))}
            </div>
            <AddButton />
        </div>
    )
}

export default NoteListPage