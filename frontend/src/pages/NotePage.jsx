import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'

const NotePage = () => {
    const param = useParams();
    const [note, setNote] = useState({})
    const getNote = async () => {
        if (param.id === 'new') return;
        let note = await fetch(`http://127.0.0.1:8000/api/notes/${param.id}/`)
        let data = await note.json()
        return setNote(data)
    }
    useEffect(() => {
        getNote()
    }, []);
    const createNote = async () => {
        await fetch(`http://127.0.0.1:8000/api/notes/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }
    const updateNote = async () => {
        await fetch(`http://127.0.0.1:8000/api/notes/${param.id}/`,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(note)
            }
        )
    }
    let deleteNote = async () => {
        await fetch(`http://127.0.0.1:8000/api/notes/${param.id}/`, {
            method: 'DELETE',
            'headers': {
                'Content-Type': 'application/json'
            }
        })
        window.history.go(-1)
    }

    const handelSubmit = () => {
        if (param.id !== 'new' && note.note === '') {
            deleteNote()
        } else if (param.id !== 'new') {
            updateNote()
        } else if (param.id === 'new' && note.note !== null) {
            createNote()
        }
        window.history.go(-1)
    }
    return (
        <div className='note'>
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handelSubmit} />
                </h3>
                {
                    param.id !== 'new' ?
                        <button onClick={deleteNote}>Delete</button> :
                        <button onClick={handelSubmit}>Done</button>
                }
            </div>
            <textarea onInput={(e) => {
                setNote({ ...note, note: e.target.value })
            }} value={note.note}></textarea>
        </div>
    )
}

export default NotePage;