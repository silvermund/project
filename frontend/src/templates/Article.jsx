import React from 'react'
import { UserMenu as Menu } from '../common'
import './table.style.css'

const Article = ({children}) => (<>
    <h1>Article</h1>
    <Menu/>
    {children}
</>)

export default Article