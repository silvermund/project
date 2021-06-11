import React from 'react'
import { UserMenu as Menu } from '../common'
import './table.style.css'

const Item = ({children}) => (<>
    <h1>Item</h1>
    <Menu/>
    {children}
</>)

export default Item