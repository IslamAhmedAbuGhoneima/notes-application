import React from 'react'
import { Link } from 'react-router-dom'
let getTime = (note) => {
    let date = new Date(note.updated).toLocaleDateString();
    return date;
}
let getTitle = (note) => {
    if (note.note.length > 45) return note.note.slice(0, 45) + '...';
    else return note.note;
}
const ListItem = ({ note }) => {
    return (
        <Link to={`/note/${note.id}`}>
            <div className="notes-list-item">
                <h3>{getTitle(note)}</h3>
                <p><span>{getTime(note)}</span></p>
            </div>
        </Link>
    )
}

export default ListItem